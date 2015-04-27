## A test of my new sorting algorithm

##Create some test data

obj_list = [2,4,6,1,2,9,4,2,4,6,4,6,78,89,4,3,2,3,4,54,6,7,67,4,3,2,1, 99,100]

import time

##begin the time trial
start = time.time()

#N <- 0
n = 0
#WHILE N <> LEN(List)
while n != len(obj_list):

    #I <- N
    #Highest <- 0
    #HighestPos <- 0
    highest_pos, highest = 0, 0
    i = n
    #WHILE I <> LEN(List)
    while i != len(obj_list):
        #IF List[I] > Highest THEN
        if obj_list[i] > highest:
            
            #Highest <- List[I]
            highest = obj_list[i]
           
            #HighestPos <- I
            highest_pos = i
        #I++
        i += 1
    #TMP <- List[N]
    tmp = obj_list[n]
    #List[N] <- Highest
    obj_list[n] = highest
    #list[HighestPos] <- TMP
    obj_list[highest_pos] = tmp
    #N++
    n += 1

print(obj_list)

print("Completed in", time.time()-start, "seconds")

##In summary:
## This program finds the largest item in a list, and puts it at the start
## Then it finds the next largest item in the list, ignoring the item at the beginning of the list, because efficiency
## then it does the same thing again, each time ignoring the repositioned items.