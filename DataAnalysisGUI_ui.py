#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class DataAnalysisGUI_UI:
    def __init__(self, master=None):
        # build ui
        self.mainWindow = tk.Tk(master)
        self.mainWindow.configure(takefocus=True)
        self.mainWindow.overrideredirect("false")
        self.mainWindow.resizable(False, False)
        self.mainWindow.title("Survey Responses Grapher")
        self.fileFrame = ttk.Frame(self.mainWindow, name="fileframe")
        self.fileFrame.configure(borderwidth=2, cursor="arrow", width=200)
        self.frameTtitle = ttk.Label(self.fileFrame, name="framettitle")
        self.frameTtitle.configure(
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            justify="left",
            text='Survey Responses Data File')
        self.frameTtitle.pack(pady=5, side="top")
        self.openFileBtn = ttk.Button(self.fileFrame, name="openfilebtn")
        self.openFileBtn.configure(
            compound="top",
            cursor="arrow",
            default="active",
            state="normal",
            takefocus=False,
            text='Open File')
        self.openFileBtn.pack(padx=20, side="left")
        self.openFileBtn.configure(command=self.openFile)
        self.fileNameLabel = ttk.Label(self.fileFrame, name="filenamelabel")
        self.fileName = tk.StringVar(value='No file selected.')
        self.fileNameLabel.configure(
            relief="flat",
            text='No file selected.',
            textvariable=self.fileName)
        self.fileNameLabel.pack(padx=10, side="left")
        self.fileFrame.pack(fill="x", side="top")
        self.optionFrame = ttk.Frame(self.mainWindow, name="optionframe")
        self.optionFrame.configure(borderwidth=2)
        self.optionSubFrame1 = ttk.Labelframe(
            self.optionFrame, name="optionsubframe1")
        self.optionSubFrame1.configure(
            text='Spreadsheet data range', width=200)
        frame2 = ttk.Frame(self.optionSubFrame1)
        frame2.configure(height=200, width=200)
        label1 = ttk.Label(frame2)
        label1.configure(
            font="TkTextFont",
            justify="left",
            takefocus=False,
            text='First data\nrow')
        label1.pack(padx=5, side="left")
        entry1 = ttk.Entry(frame2)
        self.firstRow = tk.StringVar()
        entry1.configure(
            exportselection=True,
            font="TkDefaultFont",
            state="normal",
            takefocus=False,
            textvariable=self.firstRow,
            width=5)
        entry1.pack(side="left")
        label2 = ttk.Label(frame2)
        label2.configure(
            compound="top",
            justify="left",
            text='First data \ncolumn')
        label2.pack(padx=5, side="left")
        entry2 = ttk.Entry(frame2)
        self.firstCol = tk.StringVar()
        entry2.configure(
            exportselection=True,
            font="TkDefaultFont",
            state="normal",
            takefocus=False,
            textvariable=self.firstCol,
            width=5)
        entry2.pack(side="left")
        frame2.pack(fill="x", side="top")
        frame4 = ttk.Frame(self.optionSubFrame1)
        frame4.configure(height=200, width=200)
        label6 = ttk.Label(frame4)
        label6.configure(
            text='Note: Ensure spreadsheet headers are on the first row.')
        label6.pack(side="top")
        frame4.pack(fill="x", side="top")
        self.optionSubFrame1.pack(fill="x", pady=5, side="top")
        self.optionSubFrame2 = ttk.Labelframe(
            self.optionFrame, name="optionsubframe2")
        self.optionSubFrame2.configure(text='Graph output options', width=200)
        frame1 = ttk.Frame(self.optionSubFrame2)
        frame1.configure(width=200)
        label4 = ttk.Label(frame1)
        label4.configure(text='Generate graphs\nin form(s) of')
        label4.pack(padx=10, side="left")
        radiobutton5 = ttk.Radiobutton(frame1)
        self.genGraphsOutputType = tk.IntVar(value=0)
        radiobutton5.configure(
            compound="top",
            text='Images to\nexport',
            value=0,
            variable=self.genGraphsOutputType)
        radiobutton5.pack(padx=2, side="left")
        radiobutton1 = ttk.Radiobutton(frame1)
        radiobutton1.configure(
            text='Display on \nGUI window',
            value=1,
            variable=self.genGraphsOutputType)
        radiobutton1.pack(padx=2, side="left")
        radiobutton6 = ttk.Radiobutton(frame1)
        radiobutton6.configure(
            text='Both \ntypes',
            value=2,
            variable=self.genGraphsOutputType)
        radiobutton6.pack(padx=2, side="left")
        frame1.pack(fill="x", side="top")
        self.optionSubFrame2.pack(fill="x", pady=5, side="top")
        self.optionFrame.pack(fill="x", side="top")
        self.buttonFrame = ttk.Frame(self.mainWindow, name="buttonframe")
        self.buttonFrame.configure(borderwidth=2)
        button2 = ttk.Button(self.buttonFrame)
        button2.configure(text='About Program')
        button2.pack(padx=2, side="right")
        button2.configure(command=self.aboutProgram)
        button1 = ttk.Button(self.buttonFrame)
        button1.configure(text='How to use')
        button1.pack(padx=2, side="right")
        button1.configure(command=self.showInstructions)
        button3 = ttk.Button(self.buttonFrame)
        button3.configure(text='Analyze Data')
        button3.pack(padx=2, side="right")
        button3.configure(command=self.analyzeData)
        self.buttonFrame.pack(fill="x", pady=5, side="top")

        # Main widget
        self.mainwindow = self.mainWindow

    def run(self):
        self.mainwindow.mainloop()

    def openFile(self):
        pass

    def aboutProgram(self):
        pass

    def showInstructions(self):
        pass

    def analyzeData(self):
        pass


if __name__ == "__main__":
    app = DataAnalysisGUI_UI()
    app.run()
