import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    number_of_months = 0
    total_profit_and_loss = 0
    greatest_increase = 0
    greatest_decrease = 0
    month_change = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        number_of_months += 1
        month_change = float(row[1])
        total_profit_and_loss += month_change
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]

    print("Financial Analysis")
    print("----------------------")       
    print(f"Total Months: {number_of_months}")
    print(f"Total: {total_profit_and_loss}")
    print(f"Average Change: ${round(total_profit_and_loss/number_of_months,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
     
outputFile = open("analysis.txt", "w")

outputFile.write("Financial Analysis\n")
outputFile.write("----------------------\n")       
outputFile.write(f"Total Months: {number_of_months}\n")
outputFile.write(f"Total: {total_profit_and_loss}\n")
outputFile.write(f"Average Change: ${round(total_profit_and_loss/number_of_months,2)}\n")
outputFile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${round(greatest_increase,2)})\n")
outputFile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${round(greatest_decrease,2)})\n")
outputFile.close()
