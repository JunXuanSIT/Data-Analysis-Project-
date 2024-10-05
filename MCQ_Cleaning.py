import pandas as pd
import Global_Variables as glo_vars

def clean_mcq_data():
    df = glo_vars.df
    selected_columns = glo_vars.mcqQuestions

    if selected_columns:
        for col in selected_columns:
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
                print(f"Column '{col}' not found in the DataFrame.")

        # Reset global var dataframe to the cleaned df
        glo_vars.df = df
        return "success"
    else:
        return "No MCQ columns found."

