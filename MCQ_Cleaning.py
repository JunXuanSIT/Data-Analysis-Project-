import pandas as pd
import Global_Variables as glo_var

def clean_mcq_data():
    df = glo_var.df

    # Retrieve mcqQuestions list from global var
    selected_columns = glo_var.mcqQuestions

    if not selected_columns:
        print("No MCQ columns found.")
        return

    mcq_columns = selected_columns
    #print(f"MCQ columns = {mcq_columns}")  # Print the selected columns

    # Perform data cleaning on selected columns
    try:
        for col in mcq_columns:
            if col in df.columns:
                # Check if column is numeric or not
                if pd.api.types.is_numeric_dtype(df[col]):
                    # Handle numeric columns (0-5)
                    df[col] = pd.to_numeric(df[col], errors='coerce')

                    # Define valid responses for numeric columns (0-5)
                    valid_responses = range(0, 6)

                    # Find rows with invalid responses
                    invalid_responses = ~df[col].isin(valid_responses)

                    # Calculate the average of the valid responses
                    valid_data = df[df[col].isin(valid_responses)][col]
                    if valid_data.empty:
                        print(f"No valid responses in column '{col}', unable to calculate average.")
                        continue  # Skip the column if no valid data

                    average_response = round(valid_data.mean())
                    print ({average_response})
                    # Replace invalid responses with the average
                    df.loc[invalid_responses, col] = average_response

                else:
                    # Handle string-based columns
                    # Replace empty strings with NaN
                    df[col] = df[col].replace("", pd.NA)

                    # Find rows with invalid responses (NaN)
                    invalid_responses = df[col].isna()

                    # Calculate the most common string (mode)
                    mode_value = df[col].mode()[0]  # Mode returns a list, take the first one (most common)

                    # Replace invalid (NaN) responses with the most common string
                    df.loc[invalid_responses, col] = mode_value

            else:
                print(f"Column '{col}' not found in the file.")

        return "success"
    
    except Exception as e:
        return f"Error cleaning open-ended responses with following error: {e}"
