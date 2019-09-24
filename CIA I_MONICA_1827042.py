#!/usr/bin/env python
# coding: utf-8

# In[17]:


#1. Suppose the traffic police department approaches you with the problem of monitoring the speed of drivers to get real time information. 
#The permitted speedlimit is 70 kmph. 
#For every 5 km above the speed limit (70), the driver is awardedone demerit point.
#For example, if the speed is 80, 2 demerit points are awarded. 
#If the driver gets more than 12 points, his/her license will be suspended. 
#Take the speed as input and print information regarding adherence to speed limit, demeritpoints (if any), and whether the license has to be suspended

currentspeed= int(input("Please enter the currentspeed: "))
if currentspeed <= 70:
    print("Good, Driving within speed limit at speed of:" ,currentspeed)
else:
    demeritpoints = (currentspeed-70)//5
    if demeritpoints <= 12:
        print("Your currentspeed is more than 70, your demerit point is:",demeritpoints)
    else:
        print("Your demeritpoints have exceeded 12, so your license has been suspended")


# In[18]:


#2. Suppose a printer approaches you to automate the process of printing banners,business cards and letter heads to some extent. 
#His problem is simply to check if atleast 2 uppercase letters exist in the first four characters of the matter provided byhis clients 
#and, if so, convert the entire string to uppercase. 
#Help the printer to automate this process.

content= raw_input("Please input the content: ")
uppercase = 0
i=0
for i in range(4):
    if content[i].upper() == content[i]:
        uppercase += 1
if uppercase<2:
    print(content)
else:
    print(content.upper())


# In[19]:


# 4. A small shop owner in India wants to find the optimum number of notes (Sample ofnotes: 5, 10, 20, 50, 100, 200, 500, 1000, 2000) in a given amount of money he hascollected. 
#Help him get the answer.

def countCurrency(amount):
    notes = [2000,1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Currency Count -> ")
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print("No of Notes of",i, "is", j)
       
amount= int(input("Please enter the amount: "))
countCurrency(amount)


# In[16]:


#3 A mathematician wants to find the sum of the square of all the positive integers smaller than a specified number.
# He wants to repeat this process for 15 givennumbers.
# But he only wants to print every third sum from the list of 15 sums and discard it. 
#He wants to repeat this process until the list becomes empty. Help him toachieve his objective.

def sumofsquares(n):
    number_total=[]
    for a in n:
        number_total.append(sum([i*i for i in range(1,a)]))
    while len(number_total) > 2:
        temp = number_total[:]
        for ind, a in enumerate(temp, 1):
            if ind > 0:
                if ind%3 == 0:
                    number_total.remove(a)
        print (temp)
    print(number_total[0],number_total[1])
   
if __name__=="__main__":
    n=[int(input("Enter the number{}:".format(i))) for i in range(15)]
    sumofsquares(n)
    


# In[ ]:




