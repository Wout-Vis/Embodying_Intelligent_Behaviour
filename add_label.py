import pandas as pd

# Function to add a new column with a label and replace NaN values with 0
def add_label_column(csv_file, label_name, label_value, output_file):
    # Read the existing CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Replace NaN values with 0
    df = df.fillna(0)

    # Add a new column with the specified label name and value
    df[label_name] = label_value

    # Save the updated DataFrame to a new CSV file (or overwrite the existing one)
    df.to_csv(output_file, index=False)

    print(f"NaN values replaced with 0 and column '{label_name}' added with value '{label_value}' to {output_file}.")

# Example usage
input_csv = './pullupRAW.csv'     # Your existing CSV file
output_csv = './pullupRAW.csv'   # Output CSV file with the added column
add_label_column(input_csv, 'Label', 'pullup', output_csv)
