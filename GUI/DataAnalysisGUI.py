#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import DataAnalysisGUIui as baseui
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror

class DataAnalysisGUI(baseui.DataAnalysisGUIUI):
    def __init__(self, master=None):
        super().__init__(master)

        #global variables delclare here...
        self.file_path = ""

    def openFile(self):
        filepath = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        filepath = filepath[filepath.rfind('/')+1:]
        if filepath == "":
            app.fileName.set("No file selected")
            self.file_path = ""
        else:
            app.fileName.set(filepath)
            self.file_path = filepath

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

        #get boolean value of removing duplicate entry
        removeDuplicates = app.removeDuplicates.get()

        #get boolean value of parsing nil and N.A. responses in open-ended questions
        parseNilNaResp = app.parseNilNaResp.get()

        print(f"Responses file path is {self.file_path}.\nSpreadsheet header row is {headerRowNum}; data table first row is {dataFirstRow}; data table first col is {dataFirstCol}.\nTo remove duplicate entries: {removeDuplicates}.\nTo parse \"N.A.\" and \"nil\" open-ended responses: {parseNilNaResp}.")

if __name__ == "__main__":
    app = DataAnalysisGUI()
    app.run()
