#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class DataAnalysisGUIUI:
    def __init__(self, master=None):
        # build ui
        self.mainWindow = tk.Tk(master)
        self.mainWindow.configure(takefocus=True)
        self.mainWindow.geometry("480x400")
        self.mainWindow.overrideredirect("false")
        self.mainWindow.resizable(False, False)
        self.mainWindow.title("Data Analysis Application")
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
        self.frameTitle = ttk.Label(self.optionFrame, name="frametitle")
        self.frameTitle.configure(compound="top", text='Input Parameters')
        self.frameTitle.pack(side="top")
        self.optionSubFrame1 = ttk.Labelframe(
            self.optionFrame, name="optionsubframe1")
        self.optionSubFrame1.configure(
            text='Spreadsheet data range', width=200)
        label1 = ttk.Label(self.optionSubFrame1)
        label1.configure(
            cursor="arrow",
            font="TkTextFont",
            justify="left",
            takefocus=False,
            text='Table header\nrow number')
        label1.pack(padx=5, side="left")
        entry1 = ttk.Entry(self.optionSubFrame1)
        self.headerRowNum = tk.StringVar()
        entry1.configure(
            exportselection=True,
            font="TkDefaultFont",
            state="normal",
            takefocus=False,
            textvariable=self.headerRowNum,
            width=5)
        entry1.pack(side="left")
        label2 = ttk.Label(self.optionSubFrame1)
        label2.configure(
            compound="top",
            cursor="based_arrow_down",
            justify="left",
            text='First data\nrow')
        label2.pack(padx=5, side="left")
        entry2 = ttk.Entry(self.optionSubFrame1)
        self.firstRow = tk.StringVar()
        entry2.configure(
            exportselection=True,
            font="TkDefaultFont",
            state="normal",
            takefocus=False,
            textvariable=self.firstRow,
            width=5)
        entry2.pack(side="left")
        label3 = ttk.Label(self.optionSubFrame1)
        label3.configure(
            compound="top",
            cursor="based_arrow_down",
            justify="left",
            relief="flat",
            state="normal",
            takefocus=False,
            text='First data\ncolumn')
        label3.pack(padx=5, side="left")
        entry3 = ttk.Entry(self.optionSubFrame1)
        self.firstColumn = tk.StringVar()
        entry3.configure(
            exportselection=True,
            font="TkDefaultFont",
            state="normal",
            takefocus=False,
            textvariable=self.firstColumn,
            width=5)
        entry3.pack(side="left")
        self.optionSubFrame1.pack(fill="x", pady=5, side="top")
        self.optionSubFrame2 = ttk.Labelframe(
            self.optionFrame, name="optionsubframe2")
        self.optionSubFrame2.configure(text='Data parsing options', width=200)
        frame1 = ttk.Frame(self.optionSubFrame2)
        frame1.configure(width=200)
        label4 = ttk.Label(frame1)
        label4.configure(text='Remove duplicate entries')
        label4.pack(padx=10, side="left")
        radiobutton1 = ttk.Radiobutton(frame1)
        self.removeDuplicates = tk.BooleanVar(value=True)
        radiobutton1.configure(
            compound="top",
            cursor="arrow",
            takefocus=False,
            text='Yes',
            value=True,
            variable=self.removeDuplicates)
        radiobutton1.pack(padx=5, side="left")
        radiobutton2 = ttk.Radiobutton(frame1)
        radiobutton2.configure(
            text='No',
            value=False,
            variable=self.removeDuplicates)
        radiobutton2.pack(padx=5, side="left")
        frame1.pack(fill="x", side="top")
        frame2 = ttk.Frame(self.optionSubFrame2)
        frame2.configure(width=200)
        label5 = ttk.Label(frame2)
        label5.configure(text='Analyze "nil"/"N.A."\nopen-ended responses')
        label5.pack(padx=10, side="left")
        radiobutton3 = ttk.Radiobutton(frame2)
        self.parseNilNaResp = tk.BooleanVar(value=True)
        radiobutton3.configure(
            compound="top",
            cursor="arrow",
            takefocus=False,
            text='Yes',
            value=True,
            variable=self.parseNilNaResp)
        radiobutton3.pack(padx=5, side="left")
        radiobutton4 = ttk.Radiobutton(frame2)
        radiobutton4.configure(
            text='No',
            value=False,
            variable=self.parseNilNaResp)
        radiobutton4.pack(padx=5, side="left")
        frame2.pack(fill="x", side="top")
        self.optionSubFrame2.pack(fill="x", pady=5, side="top")
        self.optionFrame.pack(fill="x", side="top")
        self.buttonFrame = ttk.Frame(self.mainWindow, name="buttonframe")
        self.buttonFrame.configure(borderwidth=2)
        self.aboutProgramBtn = ttk.Button(
            self.buttonFrame, name="aboutprogrambtn")
        self.aboutProgramBtn.configure(text='About Program')
        self.aboutProgramBtn.pack(padx=2, side="right")
        self.aboutProgramBtn.configure(command=self.aboutProgram)
        self.analyzeDataBtn = ttk.Button(
            self.buttonFrame, name="analyzedatabtn")
        self.analyzeDataBtn.configure(
            compound="top",
            cursor="arrow",
            default="normal",
            state="normal",
            takefocus=False,
            text='Analyze Data')
        self.analyzeDataBtn.pack(padx=2, side="right")
        self.analyzeDataBtn.configure(command=self.analyzeData)
        self.buttonFrame.pack(fill="x", pady=5, side="top")

        # Main widget
        self.mainwindow = self.mainWindow

    def run(self):
        self.mainwindow.mainloop()

    def openFile(self):
        pass

    def aboutProgram(self):
        pass

    def analyzeData(self):
        pass


if __name__ == "__main__":
    app = DataAnalysisGUIUI()
    app.run()
