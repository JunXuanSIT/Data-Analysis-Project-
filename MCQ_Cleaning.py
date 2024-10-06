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

    # Perform data cleaning on selected columns
    try:
        for col in mcq_columns:
            if col in df.columns:
                # Classify columns as numeric or string-based based on the column's contents
                if pd.to_numeric(df[col], errors='coerce').notna().mean() > 0.5:
                    # Column is classified as predominantly numeric
                    print(f"Column '{col}' classified as numeric.")

                    # Force the column to be numeric, converting non-numeric values to NaN
                    df[col] = pd.to_numeric(df[col], errors='coerce')

                    # Define valid responses for numeric columns (1-5)
                    valid_responses = range(1, 6)

                    # Find rows with invalid responses
                    invalid_responses = ~df[col].isin(valid_responses)

                    # Calculate the average of the valid responses
                    valid_data = df[df[col].isin(valid_responses)][col]
                    if valid_data.empty:
                        print(f"No valid responses in column '{col}', unable to calculate average.")
                        continue  # Skip the column if no valid data

                    average_response = round(valid_data.mean())
                    print(f"Replacing invalid responses in column '{col}' with average: {average_response}")

                    # Replace invalid responses with the average
                    df.loc[invalid_responses, col] = average_response

                    # Fill any remaining NaN values with the average before converting to int
                    df[col] = df[col].fillna(average_response).astype(int)

                else:
                    # Column is classified as string-based
                    print(f"Column '{col}' classified as string-based.")

                    # Replace empty strings or numbers with NaN
                    df[col] = df[col].replace("", pd.NA)
                    df[col] = df[col].apply(lambda x: x if isinstance(x, str) else pd.NA)

                    # Find rows with invalid responses (NaN or incorrect types)
                    invalid_responses = df[col].isna()

                    # Calculate the most common string (mode)
                    if not df[col].dropna().empty:
                        mode_value = df[col].mode()[0]  # Mode returns a list, take the first one (most common)
                        print(f"Replacing invalid responses in column '{col}' with the most common string: {mode_value}")

                        # Replace invalid responses (NaN) with the most common string
                        df.loc[invalid_responses, col] = mode_value
                    else:
                        print(f"No valid text responses in column '{col}', unable to determine most common value.")
            else:
                print(f"Column '{col}' not found in the file.")

        return "success"
    
    except Exception as e:
        return f"Error cleaning MCQ responses with the following error: {e}"
