import os
import csv




#Files to load and output
csvpath=os.path.join('HW02_budget_data.csv')
file_to_output=os.path.join("budget_analysis.txt")
#Creating trackers for different data
totalmonths = 0
month_of_change = []
netchangelist = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999999999]
total_net = 0
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
  
 #Read the header row  
    csvheader= next(csvreader)
   #  first_row= next(csvreader)
   #  print(first_row)
 #Extract first row to avoid appending netchange list   
    totalmonths += 1
    
   
    count=0
    for row in csvreader:
#Track total 
        print(row)
#         totalmonths += 1
#         total_net += int(row[1])
# #Track the net change
#         net_change=int(row[1])-previousnet
#         previousnet=int(row[1]) 
#         netchangelist += [net_change]
#         month_of_change += [row[0]]
#         count += 1
#         print(count)
#         if count == len(csvreader)-3:
#            break
#Calculate the greatest increase
if net_change > greatest_increase[1]:
     greatest_increase[0]=row[0]
     greatest_increase[1]=net_change
        #Calculate the greatest decrease 
if net_change < greatest_decrease[1]:
     greatest_decrease[0]=row[0]
     greatest_decrease[1]=net_change 
        #Calculate average net change
     net_monthly_avg=sum(netchangelist)/len(netchangelist)
        #Generate output summary
#      output=(
#             f"Financial Analysis\n"
#             f"----------------------------\n"
#             f"Total Months:{totalmonths}\n"
#             f"Total: ${total_net}\n"
#             f"Average Change: ${net_monthly_avg:.2f}\n"
#             f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
#             f"Greatest Decrease in Profts: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
#             #Print the output
# print(output)
# with open (csvpath,"w") as txt_file:
#                 txt_file.write(output)

                
            
               

  
    

        



