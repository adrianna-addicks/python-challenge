import os
import csv




#Files to load and output
csvpath=os.path.join('budget_data.csv')
file_to_output=os.path.join("budget_analysis.txt")
#Creating trackers for different data
totalmonths = 0
month_of_change = []
netchangelist = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999999999]
total_net = 0
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
  
 #Read the header row  
    csvheader= next(csvreader)
    
 #Extract first row to avoid appending netchange list   
    first_row= next(csvreader)
    totalmonths += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    
    for row in csvreader:
#Track total 
        totalmonths += 1
        total_net += int(row[1])
#Track the net change
        
        net_change=int(row[1])-prev_net
        prev_net=int(row[1]) 
        netchangelist += [net_change]
        month_of_change += [row[0]]
       
           
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






output = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {totalmonths}\n"
f"Total: ${total_net}\n"
f"Average  Change: ${net_monthly_avg:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print (output)
            
            
            
     
with open ("outputcsv.csv","w") as txt_file:
 txt_file.write(output)

                
            
               

  
    

        



