#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import DataAnalysisGUI_ui as baseui
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror

import Global_Variables as glo_vars
import Data_Analysis_Main as main_program
#import MCQ_Cleaning as mcq_cleaning

class DataAnalysisGUI(baseui.DataAnalysisGUI_UI):
    def __init__(self, master=None):
        super().__init__(master)

        glo_vars.excel_file_path = ""

    def openFile(self):
        glo_vars.excel_file_path = askopenfilename(
            filetypes=[("Excel *.xlsx;*.xls"), ("CSV files", "*.csv")]
        )
        filepath_onGUI = glo_vars.excel_file_path[glo_vars.excel_file_path.rfind('/')+1:] #format the file path string for GUI display
        if glo_vars.excel_file_path == "":
            app.fileName.set("No file selected")
        else:
            app.fileName.set(filepath_onGUI)

    def aboutProgram(self):
        showinfo(title="About", message="A program to extract survey responses data from Excel spreadsheets.\n\nIt parses and cleans the spreadsheet data, then analyzes the responses' patterns. In the end, it generates visualizations such as charts and tables.")

    def analyzeData(self):
        #throw error message and halt function if self.file-path is empty. same applies if text fields are empty
        if glo_vars.excel_file_path == "":
            showerror(message="No file selected!")
            return

        if app.headerRowNum.get() == "" or app.firstRow.get() == "" or app.firstColumn.get() == "":
            showerror(message="No spreadsheet data range is specified!")
            return

        #get spreadsheet table header row, first data row and first data column
        try:
            headerRowNum = int(app.headerRowNum.get())
            dataFirstRow = int(app.firstRow.get())
            dataFirstCol = int(app.firstColumn.get())

            if headerRowNum <= 0 or dataFirstRow <= 0 or dataFirstCol <= 0:
                showerror(message="Spreadsheet row & column numbers must be greater than 0.")
                return           
            if headerRowNum >= dataFirstRow:
                showerror(message="Spreadsheet header row is below or the same the first data row!")
                return
        
        except ValueError:
            showerror(message="Spreadsheet row & column numbers must be an integer greater than 0.")
            return

        #get int value for graph output type
        graphsOutputType = app.genGraphsOutputType.get()
        print(f"Graph output type selection: {graphsOutputType}")

        #parse spreadsheet to obtain data frame, df
        result = main_program.parse_data(headerRowNum, dataFirstRow)       
        if result != "success":
            showerror(message=result)
            return

        #data frame headers of open-ended responses to clean and lowercase
        openEndedRespHeaders = ['Biggest Factor for Changing Provider', 'Aspect for Improvement']

        # Clean data for open-ended header questions
        for header in openEndedRespHeaders:
            result = main_program.replace_invalid_responses(header)
            if result != "success":
                showerror(message=result)
                return

        print(glo_vars.df.head())
        
if __name__ == "__main__":
    app = DataAnalysisGUI()
    app.run()
