#Load dependencies
import csv
import os
#set initial variables
months=0
sumprofit=0
changesprofit=[] 
#Open file
file = os.path.join("Resources", "budget_data.csv")
with open(file) as budget:
    budget_data=csv.reader(budget)
    header=next(budget_data)
    #Begin analysis row by row  
    for row in budget_data:
        # The total number of months included in the dataset
        months+=1
        # The net total amount of "Profit/Losses" over the entire period
        sumprofit+=int(row[1])
        # The changes in "Profit/Losses" over the entire period
        if months>1:
            pnew=int(row[1])
            changesprofit.append(pnew-pold)
            pold=pnew
            # The greatest increase in profits (date and amount) over the entire period        
            if changesprofit[months-2]>max:
                max=changesprofit[months-2]
                maxmonth=row[0]
            # The greatest decrease in profits (date and amount) over the entire period    
            if changesprofit[months-2]<min:
                min=changesprofit[months-2]
                minmonth=row[0]
        #Set starting values        
        else:
            pold=int(row[1])
            max=0
            min=0
# Average of P/L changes
average_changes=round(sum(changesprofit)/len(changesprofit), 2)            
# Print summary/write summary text file to root (not to resource on purpose)
savepath = os.path.join("budget_summary.txt")
lines_list=["Financial Analysis of budget_data",
            "----------------------------",
            f'Total Months: {months}',
            f'Total: ${sumprofit}',
            f'Average Change: ${average_changes}',
            f'Greatest Increase in Profits: {maxmonth} (${max})',
            f'Greatest Decrease in Profits: {minmonth} (${min})']
with open(savepath, 'w') as summary:
    for line in lines_list:
        summary.write(line)
        summary.write('\n')
        print(line)
    
# Analysis should align with the following results:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# Print and export results as text file.