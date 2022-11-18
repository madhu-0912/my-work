#importing the predefined directories
from collections import defaultdict
from fileinput import filename                 
from heapq import nlargest
from tokenize import Ignore


step = 4
result = 5
data=[]
data1=[]
#defining the file reading function
def readfile():
    try:  #using try expect function 
        with open("19806820.txt") as file:
            for ln,l in enumerate(file):
                if ln % step == 0:  #accessing the only speech lines
                    data.append(l)  # apending the speechlines to data
        return data         #returning speech lines to the functions
    except:
        print("ERROR/ in file name.")

data1 = [x[:-1] for x in readfile()] #here this line is to remove'/n'
print(data1)
 

discussion=defaultdict(list)     #defining dictionaries as discussion                          
for line in data1:       # Iterating through the speech lines                              
    seperator=line.split(":")      #splitting the speech lines using  ":"                            
    if len(seperator)!=0:
        discussion[seperator[0]]=0    # assigning zero initially to directory    
       #Counting the speech words of each speaker                           
for words in data1:

    val=words.split(":")        
    if len(val)>1:
        a=val[1].split(" ")                             
        discussion[val[0]]+=len(a)-1
del discussion["Sridhar Nomula"]        #Delete fun is used to ignore/delete professor speech
print("\nspeakers and their wordcount\n")       
for key,value in discussion.items():                             
    print(key,":",value)                # printing all speakers names and their word count

top5 = nlargest(result, discussion, key=discussion.get) # n largest fun is used for sorting dictionaries through its value so we are choosing top 5 speakers
           
print("\nTop 5 Spekers are: \n")
for val in top5:                                   
    print(val,":",discussion[val])          #Printing the final result of top 5 speakers for word count                                                                 