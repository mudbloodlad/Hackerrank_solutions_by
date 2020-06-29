import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    array = ar
    array.sort()           #sorting the array for simple solution
    elements = [array[0]]  # this will store distinct elements from the array
    occurence = list()     # it stores the number of occurence of an element 
    pairs = 0              # stores total number of pairs

    # creating an list of distinct elements from array  
    for i in range(len(array)-1): 
        if array[i]!=array[i+1]:
            elements.append(array[i+1])
#print(elements) // you can print the elements just to be sure about the distinct list

    # creating a list that holds the occurence number for each element 
    for i in range(len(elements)):
        check_for = elements[i]
        count = 0
        for j in range(len(array)):
        
            if array[j]==check_for:
                count+=1
        occurence.append(count)  
#print(occurence) // print the list of occurence numbers just to be sure 

    #finally counting the number of pairs... 
    for i in range(len(elements)):
        if occurence[i]>=2:
            pair = occurence[i]//2
            pairs = pairs+pair
    return pairs
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
