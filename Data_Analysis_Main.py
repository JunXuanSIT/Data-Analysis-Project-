import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

import Global_Variables as glo_vars

# Function to parse excel with checks
def parse_data(firstDataRow, firstDataCol):
    rowsSkipped = []
    for rowToSkip in range(2, firstDataRow-1): #initialze list of skipped rows, in between the header and question type row (rows 0 and 1) and the first data row
        rowsSkipped.append(rowToSkip)

    colsSkipped = []
    for colToSkip in range(0, firstDataCol-1):
        colsSkipped.append(colToSkip)

    try:
        #open excel spreadsheet, create data frame and remove unwanted rows
        if glo_vars.excel_file_path.lower().endswith(('.xlsx', '.xls')):
            glo_vars.df = pd.read_excel(glo_vars.excel_file_path, header=0, skiprows=rowsSkipped)
        elif glo_vars.excel_file_path.lower().endswith('.csv'):
            glo_vars.df = pd.read_csv(glo_vars.excel_file_path, header=0, skiprows=rowsSkipped)

        #remove unwanted cols
        glo_vars.df = glo_vars.df.drop(glo_vars.df.columns[colsSkipped], axis=1)

        #get the question type row and group all the question headers into the question type
        headersList = list(glo_vars.df.columns.values)
        questionTypeList = list(glo_vars.df.iloc[0].values)

        # Initialize typeIndex
        typeIndex = 0

        # Initialize found flags
        found_mcq = False
        found_open_ended = False

        # Loop through the question types
        for type in questionTypeList:
            if type.lower() == "multiple choice":
                glo_vars.mcqQuestions.append(headersList[typeIndex])
                found_mcq = True  
            elif type.lower() == "open ended":
                glo_vars.openEndedQuestions.append(headersList[typeIndex])
                found_open_ended = True  
            typeIndex += 1

        # After the loop, check if no valid question types were found
        if not found_mcq and not found_open_ended:
            return f"Error: No valid 'multiple choice' or 'open ended' question types found.\nPlease add a table row below table headers in your excel spreadsheet with corresponding qeustion types; either 'multiple choice' or 'open ended'."


        #remove the question type row
        glo_vars.df = glo_vars.df.drop(axis=0, labels=[0])
        return "success"

    except Exception as e:
        return f"Error parsing spreadsheet with following error: {e}"
    
# Function to convert open-ended responses to lowercase and replace invalid responses
def clean_open_ended_responses():
    replace_values = {"nil", "n.a.", "idk", "na"}
    try:
        for questionHeader in glo_vars.openEndedQuestions:
            # Convert to lowercase
            glo_vars.df[questionHeader] = glo_vars.df[questionHeader].str.lower()
            # Replace invalid responses
            glo_vars.df[questionHeader] = glo_vars.df[questionHeader].replace(replace_values, "No concerns expressed")
        return "success"
    
    except Exception as e:
        return f"Error cleaning open-ended responses with following error: {e}"