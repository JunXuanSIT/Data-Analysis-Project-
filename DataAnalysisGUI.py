#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import DataAnalysisGUI_ui as baseui
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
import Global_Variables as glo_vars
import Data_Analysis_Main as main_program
import MCQ_Cleaning as MCQ_Cleaner
import tempfile
import os
import subprocess
import threading

class DataAnalysisGUI(baseui.DataAnalysisGUI_UI):
    def __init__(self, master=None):
        super().__init__(master)

        self.streamlit_process = None  # Store the Streamlit process reference
        glo_vars.excel_file_path = ""

        showinfo(title="Instructions", message=glo_vars.instructions)

        # Bind the close event to the on_closing method
        self.mainWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

    def openFile(self):
        glo_vars.excel_file_path = askopenfilename(
            filetypes=[("Excel *.xlsx;*.xls"), ("CSV files", "*.csv")]
        )
        filepath_onGUI = glo_vars.excel_file_path[glo_vars.excel_file_path.rfind('/')+1:]  # format the file path string for GUI display
        if glo_vars.excel_file_path == "":
            app.fileName.set("No file selected")
        else:
            app.fileName.set(filepath_onGUI)

    def showInstructions(self):
        showinfo(title="Instructions", message=glo_vars.instructions)

    def aboutProgram(self):
        showinfo(title="About", message=glo_vars.aboutMessage)

    def analyzeData(self):
        # throw error message and halt function if self.file-path is empty. same applies if text fields are empty
        if glo_vars.excel_file_path == "":
            showerror(message="No file selected!")
            return

        if app.firstRow.get() == "" or app.firstCol.get() == "":
            showerror(message="No spreadsheet data range is specified!")
            return

        # get spreadsheet table header row, first data row, first data column and question type row
        try:
            dataFirstRow = int(app.firstRow.get())
            dataFirstCol = int(app.firstCol.get())

            if dataFirstRow <= 0 or dataFirstCol <= 0:
                showerror(message="Spreadsheet row & column numbers must be greater than 0.")
                return

        except ValueError:
            showerror(message="Spreadsheet row & column numbers must be an integer greater than 0.")
            return

        # get int value for graph output type
        graphsOutputType = app.genGraphsOutputType.get()
        print(f"Graph output type selection: {graphsOutputType}")

        # parse spreadsheet to obtain data frame, df
        result = main_program.parse_data(dataFirstRow, dataFirstCol)
        if result != "success":
            showerror(message=result)
            return

        # Clean data for open-ended questions
        result = main_program.clean_open_ended_responses()
        if result != "success":
            showerror(message=result)
            return

        # Clean MCQ data
        result = MCQ_Cleaner.clean_mcq_data()
        if result != "success":
            showerror(message=result)
            return

        # Save the cleaned DataFrame to a temporary CSV file
        temp_csv_path = os.path.join(tempfile.gettempdir(), "cleaned_data.csv")
        glo_vars.df.to_csv(temp_csv_path, index=False)

        # Run Streamlit
        def run_streamlit():
            self.streamlit_process = subprocess.Popen(["streamlit", "run", "Output.py", "--", temp_csv_path])  # Pass the path to the cleaned data
            print("Streamlit process started.")

        streamlit_thread = threading.Thread(target=run_streamlit)
        streamlit_thread.start()

        print(glo_vars.mcqQuestions)

    def on_closing(self):
        """Handle the close event for Tkinter window."""
        if self.streamlit_process:
            # Terminate the Streamlit subprocess if it's running
            self.streamlit_process.terminate()
            self.streamlit_process = None
            print("Streamlit process terminated.")

        # Hide the Tkinter window and quit the main loop
        self.mainWindow.withdraw()  # Hides the window
        self.mainWindow.quit()       # Exits the main loop
        print("Tkinter window hidden and main loop exited.")

if __name__ == "__main__":
    app = DataAnalysisGUI()
    app.run()
