import pandas as pd

# Function to add a new column with a label and replace NaN values with 0
def add_label_column(csv_file, label_name, label_value, output_file):
    df = pd.read_csv(csv_file)
    df = df.fillna(0)
    df[label_name] = label_value
    df.to_csv(output_file, index=False)

    print(f"NaN values replaced with 0 and column '{label_name}' added with value '{label_value}' to {output_file}.")

input_csv = './pullupRAW.csv'     # Your existing CSV file
output_csv = './pullupRAW.csv'   # Output CSV file with the added column
add_label_column(input_csv, 'Label', 'pullup', output_csv)
