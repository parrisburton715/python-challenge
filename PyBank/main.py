import os
import csv

# Path to collect data from the Resources folder

data = os.path.join(r'PyBank\Resources\Budget_data.csv')
output = os.path.join('analysis', 'budget_analysis.csv')

total_months = 0

# Read in the csv file
with open(data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Split the data on commas
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    total_months +=1

    # Loop through the data
    for row in csvreader:
        total_months +=1

      # Print the total number of months
        print(f"Total Months: {total_months}")  

       # Initialize variables
        total_profit_losses = 0

        # Path to collect data from the Resources folder

        data = os.path.join(r'PyBank\Resources\Budget_data.csv')
        output = os.path.join('analysis', 'budget_analysis.csv')

        # Read the budget_data.csv file

with open(data) as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)
    
    # Iterate through each row in the dataset
    for row in csvreader:
        profit_loss = int(row[1])
        total_profit_losses += profit_loss

# Print the net total amount of "Profit/Losses" over the entire period
print(f"Net Total Amount of Profit/Losses: ${total_profit_losses}") 

# Path to the budget data CSV file
data = os.path.join(r'PyBank\Resources\Budget_data.csv')
output = os.path.join('analysis', 'budget_analysis.csv')

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the budget data CSV file
with open(data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the total profit/losses
        total_profit_losses += int(row[1])

        # Track the dates
        dates.append(row[0])

        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            profit_loss_changes.append(int(row[1]) - previous_profit_loss)
        
        previous_profit_loss = int(row[1])

# Calculate the average of the changes in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")

# Output the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_profit_losses}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")

print("Results have been saved to 'financial_analysis.txt'.")


# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_change_list = []
greatest_increase_date = ""
greatest_increase_amount = 0

# Read data from the CSV file
with open(data, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        total_months += 1
        total_profit_losses += int(row[1])
        
        # Calculate profit change
        if total_months > 1:
            profit_change = int(row[1]) - previous_profit_loss
            profit_change_list.append(profit_change)
            
            # Check for greatest increase in profits
            if profit_change > greatest_increase_amount:
                greatest_increase_amount = profit_change
                greatest_increase_date = row[0]
        
        previous_profit_loss = int(row[1])

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount} )")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_change_list = []
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Read data from the CSV file
with open(data, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        total_months += 1
        total_profit_losses += int(row[1])
        
        # Calculate profit change
        if total_months > 1:
            profit_change = int(row[1]) - previous_profit_loss
            profit_change_list.append(profit_change)
            
            # Check for greatest decrease in profits
            if profit_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_change
                greatest_decrease_date = row[0]
        
        previous_profit_loss = int(row[1])

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount} )")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

                                                                  