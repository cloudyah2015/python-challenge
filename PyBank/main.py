# -*- coding: UTF-8 -*-


# Dependencies
import csv
import os

# Files to load and output
file_to_load = "/Users/Claudia/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# Ensure the 'analysis' folder exists
output_folder = os.path.join(os.getcwd(), "analysis")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

file_to_output = os.path.join(output_folder, "budget_analysis.txt")

# Debugging: Print file paths
print(f"File to load: {file_to_load}")
print(f"File to output: {file_to_output}")

# Check if the input file exists
if not os.path.exists(file_to_load):
    print(f"Error: The file '{file_to_load}' does not exist.")
else:
    # Define variables
    total_months = 0
    total_net = 0
    net_change_list = []
    previous_month_profit_loss = 0
    greatest_increase = ["", 0]  # [Month, Amount]
    greatest_decrease = ["", 0]  # [Month, Amount]

    try:
        # Open and read the CSV
        with open(file_to_load) as financial_data:
            reader = csv.reader(financial_data)

            # Skip the header row
            header = next(reader)

            # Process each row
            for row in reader:
                try:
                    # Increment month counter
                    total_months += 1

                    # Track the total net amount
                    total_net += int(row[1])

                    # Calculate net change
                    current_month_profit_loss = int(row[1])
                    if total_months > 1:
                        net_change = current_month_profit_loss - previous_month_profit_loss
                        net_change_list.append(net_change)

                        # Update greatest increase and decrease
                        if net_change > greatest_increase[1]:
                            greatest_increase = [row[0], net_change]
                        if net_change < greatest_decrease[1]:
                            greatest_decrease = [row[0], net_change]

                    previous_month_profit_loss = current_month_profit_loss

                except ValueError as e:
                    print(f"Error processing row {row}: {e}")

        # Calculate average change
        average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

        # Generate output
        output = (
            f"Financial Analysis\n"
            f"----------------------------\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change: ${average_change:.2f}\n"
            f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
            f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
        )

        # Print output to terminal
        print(output)

        # Write output to file
        with open(file_to_output, "w") as txt_file:
            txt_file.write(output)

        print(f"Analysis saved to {file_to_output}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
