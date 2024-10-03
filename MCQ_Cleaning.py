import pandas as pd
from tkinter import Tk, Listbox, Button, simpledialog, END, MULTIPLE
from tkinter.filedialog import askopenfilename
import os

def JX_MCQ_Cleaning():
    # Function to display the listbox for column selection
    #def select_columns_with_listbox(columns):
        # Create a new Tkinter window
        #listbox_window = Tk()
        #listbox_window.title("Select Columns for Data Cleaning")

        # Create a Listbox for selecting columns
        #listbox = Listbox(listbox_window, selectmode=MULTIPLE)
        #for col in columns:
        #    listbox.insert(END, col)  # Add each column to the Listbox
        #listbox.pack()

        # Initialize selected_columns variable
        #selected_columns = []

        # Function to confirm the selection and close the window
        #def confirm_selection():
        #    nonlocal selected_columns  # Use nonlocal to modify the variable defined in the outer scope
        #    selected_indices = listbox.curselection()  # Get selected indices
        #    selected_columns = [columns[i] for i in selected_indices]  # Get selected column names
        #    print(f"Selected Columns: {selected_columns}")  # Print selected columns for debugging
        #    listbox_window.quit()  # Close the window

        # Create and place the confirm button
        #confirm_button = Button(listbox_window, text="Confirm", command=confirm_selection)
        #confirm_button.pack()

        # Run the Tkinter main event loop
        #listbox_window.mainloop()

        # Destroy the window
        #listbox_window.destroy()

       # return selected_columns

    # Hide the root Tkinter window
    #root = Tk()
    #root.withdraw()

    # Prompt the user to select the file
    #file_path = askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    #if not file_path:
     #   raise FileNotFoundError("No file selected")

    # Prompt the user for the header row, header column, and data start row
    #header_row = simpledialog.askinteger("Input", "Enter the header row (1-based index):", minvalue=1)
    #header_column = simpledialog.askinteger("Input", "Enter the header column (1-based index):", minvalue=1)
    #data_start_row = simpledialog.askinteger("Input", "Enter the data row (1-based index):", minvalue=header_row + 1)

    # Load the Excel file
    #df = pd.read_excel(file_path, header=None)  # Read without specifying headers initially

    # Strip leading/trailing spaces from the specified header column and set it as the DataFrame's columns
    #df.columns = df.iloc[header_row - 1].str.strip()  # Use the specified header row for column names
    #df = df.iloc[data_start_row - 1:, header_column - 1:]  # Start from the specified data row and column

    # Print the actual column names for debugging purposes
    #print("Columns in the file:", df.columns)

    # Display listbox for column selection
    #selected_columns = select_columns_with_listbox(df.columns.tolist())  # Convert columns to a list for the listbox

    # Now 'selected_columns' contains the columns the user selected
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

        # Save the updated data to a new Excel file
        #output_file = 'updated_excel_file.xlsx'
        #df.to_excel(output_file, index=False)

        #print("Invalid responses have been replaced with the average value.")

        # Open the Excel file after saving
        #os.startfile(output_file)  # This works on Windows to open the file
    #else:
     #   print("No columns were selected.")
JX_MCQ_Cleaning()
