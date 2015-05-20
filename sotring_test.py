## A test of my new sorting algorithm

##Create some test data

<<<<<<< HEAD
obj_list = [2,4,6,1,2,9,4,2,4,6,4,6,78,89,4,3,2,3,4,54,6,7,67,4,3,2,1, 99,100,42894,455,6,6,7,7,5,4,32,12,6.5,23,43,4,5,6,7,8,8,9]
=======
obj_list = [2,4,6,1,2,9,4,2,4,6,4,6,78,89,4,3,2,3,4,54,6,7,67,4,3,2,1, 99,100,5,6,67,7,5,4,3,2,1,1,2,3,3,4,23,4,56,10,4,3,23,3]
>>>>>>> 96feaa70e1def9cb0e3614d3836a26a600b31382

import time, random


## generate a list of 10,000 random integers
for i in range(14):
    obj_list.append(random.randint(0, 1000))

##begin the time trial
start = time.time()

##TODO: Find the lowest Number (this means it can account for negative numbers)
x = 0
#N <- 0
n = 0
s = len(obj_list)
#WHILE N <> LEN(List)
while n != s:

    #I <- N
    #Highest <- 0
    #HighestPos <- 0
    highest_pos, highest = 0, 0
    i = n
    #WHILE I <> LEN(List)
    while i != s:
        #IF List[I] > Highest THEN
        if obj_list[i] > highest:
            
            #Highest <- List[I]
            highest = obj_list[i]
           
            #HighestPos <- I
            highest_pos = i
        #I++
        i += 1
        x += 1
    #TMP <- List[N]
    tmp = obj_list[n]
    #List[N] <- Highest
    obj_list[n] = highest
    #list[HighestPos] <- TMP
    obj_list[highest_pos] = tmp
    #N++
    n += 1

#print(obj_list)
print(x)
print("Completed in", time.time()-start, "seconds")

##In summary:
## This program finds the largest item in a list, and puts it at the start
## Then it finds the next largest item in the list, ignoring the item at the beginning of the list, because efficiency
## then it does the same thing again, each time ignoring the repositioned items.
## EDIT: not faster then bubblesort
