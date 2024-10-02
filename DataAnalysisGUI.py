#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import DataAnalysisGUI_ui as baseui
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror

from Global_Variables import *
import Data_Analysis_Main as main_program
import MCQ_Cleaning as mcq_cleaning

class DataAnalysisGUI(baseui.DataAnalysisGUI_UI):
    def __init__(self, master=None):
        super().__init__(master)

    def openFile(self):
        excel_file_path = askopenfilename(
            filetypes=[("Excel files", "*.xlsx;*.xls"), ("CSV files", "*.csv")]
        )
        filepath_onGUI = excel_file_path[excel_file_path.rfind('/')+1:] #format the file path string for GUI display
        if excel_file_path == "":
            app.fileName.set("No file selected")
        else:
            app.fileName.set(filepath_onGUI)

    def aboutProgram(self):
        showinfo(title="About", message="A program to extract survey responses data from Excel spreadsheets.\n\nIt parses and cleans the spreadsheet data, then analyzes the responses' patterns. In the end, it generates visualizations such as charts and tables.")

    def analyzeData(self):
        #throw error message and halt function if self.file-path is empty. same applies if text fields are empty
        if self.file_path == "":
            showerror(message="No file selected!")
            return

        if app.headerRowNum.get() == "" or app.firstRow.get() == "" or app.firstColumn.get() == "":
            showerror(message="No spreadsheet data range is specified!")
            return

        #get sheet data table selection; table header row, start of table coordinates
        try:
            headerRowNum = int(app.headerRowNum.get())
            dataFirstRow = int(app.firstRow.get())
            dataFirstCol = int(app.firstColumn.get())

            if headerRowNum <= 0 or dataFirstRow <= 0 or dataFirstCol <= 0:
                showerror(message="Spreadsheet row & column numbers must be greater than 0.")
                return
        
        except ValueError:
            showerror(message="Spreadsheet row & column numbers must be an integer greater than 0.")
            return

        #get int value for graph output type
        graphsOutputType = app.genGraphsOutputType

        print(f"Responses file path is {excel_file_path}.\nSpreadsheet header row is {headerRowNum}; data table first row is {dataFirstRow}; data table first col is {dataFirstCol}.\nGraph output type selection: {graphsOutputType}")

if __name__ == "__main__":
    app = DataAnalysisGUI()
    app.run()
