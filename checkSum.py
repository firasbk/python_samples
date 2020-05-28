# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Firas Bou Karroum May 28,2020
def checkSum(numbers, k):
    i = 0
    j = 0
    while i < len(numbers)-1:
        j = i + 1
        while j < len(numbers)-1:
            if(numbers[i] + numbers[j] == k):
                return True
            j+=1
        i+=1
    return False

k=17
l=4
numbers= [10, 15, 3, 7, 8]
print(" The result of checkSum for 17 is: ", checkSum(numbers,k) )
print(" The result of checkSum for 4 is: ", checkSum(numbers,l) )
        
    
