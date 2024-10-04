import pandas as pd
from tkinter import Tk, Listbox, Button, simpledialog, END, MULTIPLE
from tkinter.filedialog import askopenfilename
import os

import Global_Variables as glo_var

def MCQ_Cleaning():

    # Now 'selected_columns' contains the columns the user selected
    """
    some instructions

    for dataframe variable, use glo_var.df
    access the mcq columns array, use glo_var.mcqQuestions

    return the cleaned df back to global variable
    
    --kok peng
    """
    # retrieving dataframe from global var
    df = glo_var.df
    # retrieving mcqQuestions list from global var
    selected_columns = glo_var.mcqQuestions

    if selected_columns:
        mcq_columns = selected_columns
        print(f"mcq_columns = {mcq_columns}")  # Print the selected columns

        # Perform data cleaning on selected columns
        for col in mcq_columns:
            if col in df.columns:
                # Convert the data in the relevant columns to numeric, forcing errors to NaN
                df[col] = pd.to_numeric(df[col], errors='coerce')

                # Define the valid responses range
                valid_responses = range(0, 6)  # Valid responses are 0-5

                # Find the rows with invalid responses
                invalid_responses = ~df[col].isin(valid_responses)

                # Calculate the average of the valid responses for this column
                average_response = round(df[df[col].isin(valid_responses)][col].mean())

                # Replace invalid responses with the average
                df.loc[invalid_responses, col] = average_response
            else:
                print(f"Column '{col}' not found in the file.")
        # Reset global var dataframe to the cleaned df
        glo_var.df = df