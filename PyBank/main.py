import os
import csv

# Settign a variable for the current file using os.path.join to allow for different operating systems
budget_csv = os.path.join('Resources', 'budget_data.csv')

# reading in the file and creating an iterator to access the data in the file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skil header row
    header = next(csvreader)

    # variable to determine number of months
    num_months = 0

    # variable to determine total net change
    total_net = 0

    # variable to store the month from the current row.
    current_month = 0

    # list to store the change from month to monthh
    change_per_month = []

    # Iterating through the file
    for i in csvreader:
        # Counting the number of months based on the number of rows
        num_months += 1

        # adding each new values to the total_net variable
        total_net += int(i[1])

        # Subtracting current month fron the next iteration then adding the change to the change_per_month list (this will be used to find the avg)
        change_per_month.append(int(i[1])-current_month)

        # setting current row values to current_month
        current_month = int(i[1])

    # using the  change values in the change_per_month to find the average, then rounding.
    avg_change = round(sum(change_per_month[1:])/len(change_per_month[1:]), 2)

    # finding max increase in the change_per_month list
    greatest_increase = max(change_per_month)

    # finding the decrease in the change_per_month list
    greatest_decrease = min(change_per_month)

    # Printing the output to the terminal
    print("Financial Analysis")
    print("----------------------------------------------------")
    print(f'Total Months: {int(num_months)}')
    print(f'Total: ${total_net} ')
    print(f'Average Change: ${avg_change} ')
    print(f'Greatest Increase in Profits: ${greatest_increase} ')
    print(f'Greatest Decrease in Profits: ${greatest_decrease} ')
    print("----------------------------------------------------")


# Writing the output to a text file
output_file = os.path.join("final_budget.txt")

with open(output_file, 'w') as text_file:
    text_file.writelines("Financial Analysis\n")
    text_file.writelines(
        f"--------------------------------------------------\n")
    text_file.writelines(f"Total Months: {int(num_months)}\n")
    text_file.writelines(f"Total: ${total_net}\n")
    text_file.writelines(f"Average Change: ${avg_change}\n")
    text_file.writelines(
        f"Greatest Increase in Profits: ${greatest_increase}\n")
    text_file.writelines(
        f"freatest Decrease in Profits: ${greatest_decrease}\n")
    text_file.writelines(
        "--------------------------------------------------")
