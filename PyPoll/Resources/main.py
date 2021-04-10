import os
import csv

election_data=os.path.join("election_data.csv")
#Setting array
candidates=[]






with open(election_data) as csvfile:
    csvReader=csv.reader(csvfile,delimiter=',')
    next(csvfile)
    for row in csvReader:
        candidates.append(row[2])
    
    total_votes=len(candidates)

#create list of candidates
eachcandidate= []
for x in candidates: 
    if x not in eachcandidate:
        eachcandidate.append(x)

print(eachcandidate)

#vote counting          
totalvotes_khan=0
totalvotes_correy=0
totalvotes_li=0
totalvotes_otooley=0


for x in candidates:
    if x == eachcandidate[0]:
        totalvotes_khan += 1
    elif x == eachcandidate[1]:
        totalvotes_correy += 1
    elif x == eachcandidate[2]:
        totalvotes_li += 1
    elif x == eachcandidate[3]:
        totalvotes_otooley += 1
#voting percentages
khanpercentage= round(totalvotes_khan/ total_votes *100)
correypercentage= round(totalvotes_correy/ total_votes *100)
lipercentage= round(totalvotes_li/ total_votes *100)
otooleypercentage= round(totalvotes_otooley/ total_votes *100)

WhoWon= max(totalvotes_khan,totalvotes_correy,totalvotes_li,totalvotes_otooley)

if totalvotes_khan > (totalvotes_correy and totalvotes_li and totalvotes_otooley):
    winner= "Khan"
elif totalvotes_correy > (totalvotes_li and totalvotes_otooley):
    winner="Correy"
elif totalvotes_li > (totalvotes_otooley):
    winner= "Li"
else:
    winner="O'Tooley" 

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f" Khan:     {khanpercentage}%   ({totalvotes_khan}) ")   
print(f" Correy:   {correypercentage}%  ({totalvotes_correy}) ")   
print(f" Li:       {lipercentage}%  ({totalvotes_li}) ")   
print(f" O'Tooley: {otooleypercentage}%    ({totalvotes_otooley}) ")   
print("----------------------------")
print(f"Winner: {winner} " )
print("----------------------------")
textoutput= os.path.join("Analysis", 'election_info.txt')
with open (textoutput, 'w', newline='') as summary:
        write=csv.writer(summary)
        write.writerows([
["Election Analysis"],
["----------------------------"],
[f"Total Votes: {WhoWon}"],
["----------------------------"],
[f"Khan:    {khanpercentage}%    ({totalvotes_khan})"],
[f"Correy:        {correypercentage}%       ({totalvotes_correy})"],
[f"Li:          {lipercentage}%         ({totalvotes_li})"],
[f"O'Tooley:      {otooleypercentage}%     ({totalvotes_otooley})"],
["----------------------------"],
[f"Winner:    {winner}  "]
     ])



        


    