#KONLAN GISELE YENNULOM
#ASSIGNMENT_2
#DEQUES


import random #importing the random function to generate a set of random numbers when needed
class Deque:# creation of a deque class
    def __init__(self,array,arrayLength,currentLength): #creation of a function that will contain the variables responsible for checking the arrays and array lengths
        if len(array)>arrayLength:#an if statement to check that the array is not more than the array length
            return error#an error statement
        self.array=array
        self.arrayLength=arrayLength
        self.currrentLength=array.Length #assigning the respective variables      
    def isEmpty(self): #function to check if the array is empty or not
        return len(self.array)==0 #a return statement to return zero if the array is emty
    def isFull(self):#function to check if the array is full or 
        return len(self.array)==self.length#a return statement to return the length of the array.
    def getLength(self):#a getter to obtain the length of the array
        return len(self.currentLength)
    def addToFront(self,x):#a function to add a number to the front of the array
        if self.array==self.arrayLength:#if statement to tell us the array is full 
            return ('array is already full')
        self.array.insert(0,x)#inserting zero in the position of x when necessary
    def addToBack(self,x):#a function to add a number to the back of the array
        if self.array==self.arrayLength:#if statement to tell us the array is full
            return ('array is already full')
        self.array.append(x)#statement to add on to the array if it is not full
    def removeFromFront(self):#a function to delete any number from the front
        self.array.pop(0)#a statement to remove the preferred number from the front
    def removeFromBack(self):#a function to delete any number from the back
        self.array.pop()#a statement to remove the preferred number from the back
    def halfFull(s):#a function to divide the array into equal halves
        halfFull=list(range(rand.randint(1,100)//2))#statement with the formular to make the array half full


        
#INTERPOLATION


def interSearch(array,target_num): #the creation of a function that takes 2 parameters that is the array and the target number we are looking for
    lowest_number=0 #the lowest number of the array is zero
    highest_number=(len(array)-1)#the highest number of the array is the total length of the array minus one since indexing starts from zero
    while lowest_number<=highest_number and target_num>=array[lowest_number] and target_num<=array[highest_number]:#while loop to ensure that the target is in the sorted array
        index = lowest_number + int(((float(highest_number - lowest_number) / ( array[highest_number] - array[lowest_number])) * ( target_num- array[lowest_number]))) #the constant formula for finding the index using interpolation by estimating the midpoint.
        if array[index] == target_num:#a target is reached when the index of the input array goes with the target number and the index is returned 
            return index
        elif array[index] < target_num:#for each target being inputted, if the value of the target is larger than the index of the targetted value of the array, the program does a re-evaluation using the left part formula of the sub array
            lowest_number = index + 1; #the lowest value becomes the index that is found plus one
        else:
            highest_number = index - 1;# else,for every target inputted, if the value of the target is smaller than the index of the target value of the array, python re-evaluates using the right part formula of the sub array
    return -1 #-1  is retunred if the target does not exist
print(interSearch([1,2,3,4,5,6,7,8],6))

#interpolation search function 

# If x is present in array[0..n-1], 
#return its index otherwise it returns -1
import time#importing time to be able to obtain the time
import random #importing random for random numbers
def interpolation_search(ordered_list, term,nearest_mid):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None
    
    return False
TimeInter=[] #variable for the time interval
for e in range(1,6):#for loop to go through the list for 5 different runs
    Time_for_starting=time.time()#intializing a variable for time
    List_Test = random.sample(range(1,32767),100)#variable to test the list of random numbers generated
    New_List=sorted(List_Test)#a variable created to sort out the new list for the new set of numbers
    print(New_List)#to print out the new list
    X= int(input("type in you number: "))#variable initialized to input your preferred number by the user
    print(interpolation_search(New_List,100,X))
    Time_for_ending=time.time()#variable to initialize the time it ends
    Interval=(Time_for_ending-Time_for_starting)*1000#variable to initialize the interval between the starting time and ending time
    TimeInter.append(Interval)#used to add or append the interval list
print ("after trying 5 times,the msecs for N=100 is: " (TimeInter)//5)

TimeInter=[]
for a in range(1,6):
    Time_to_start=time.time()
    test_List = random.sample(range(1,32767),1000)
    newList=sorted(testList)
    print(NewList)
    Y= int(input("enter your number: "))
    print(InterSearch(NewList,1000,Y))
    Time_to_end= time.time()
    Interval=(Time_to_end-Time_to_start)*1000
    TimeInter.append(Interval)
print (sum(TimeInter)//5)

TimeInter=[]
for i in range(1,6):
    startingTime=time.time()
    testingList = random.sample(range(1,32767),5000)
    NewList=sorted(testlist)
    print(NewList)
    Z= int(input("enter number: "))
    print(InterSearch(NewList,5000,Z))
    endingTime= time.time()
    Interval=(endingTime-startingTime)*1000
    TimeInter.append(Interval)
print (sum(TimeInterval)//5)

'''Repeated time code with similar variable names to repeatedly run for 1000 and 5000'''





#Binary Search


import random #importing random to generate random numbers
import time #importing time to enable the time function run
def binary_Search(seq,target): #function for the binarySearch
    lo=0 #initializing the lowest number to zero
    hi=len(seq)-1#initializing the highest number to the length of the sequence minus one
    been_Found=False #a variable to see if the number has been found
    while lo<=hi and not beenFound:
        mid_point=(lo+hi)//2 #used to find the middlepoint of the numbers but adding the lowest and highest numbers and dividing by 2
        if seq[mid_point]==target:#if statement to determine if the sequence of the midpoint is equal to the target
            been_Found=True #if so, then the target has been found
        else:
            if target<seq[mid_point]: #if the target is less than the sequence midpoint
                hi=mid_point-1#then the highest number will be the midpoint minus one
            else:
                lo=mid_point+1#else the lowest number will be the midpoint plus one.
    return been_Found #a return statement to end the while loop

Time_Interval=[]#variable for the time interval
for i in range(1,6):#for loop to go through the list for 5 different runs
    start_Time=time.time()#a variable to start the time 
    TestList = random.sample(range(1,32767),100)#a test variable to generate a set of random numbers to be tested
    NewList=sorted(testlist)#a variable to create a new list and sort it out
    print(NewList)#to print the new list
    X= int(input("Input number: "))#to input the preferred number by the user
    print(binary_Search(NewList,X))
    endTime= time.time()#to end the time
    Interval=(end_Time-start_Time)*1000#to obtain the interval
    Time_Interval.append(Interval)
print (sum(Time_Interval)//5)#to get the sum of the time interval
Time_Interval=[]
for i in range(1,6):
    start_Time=time.time()
    TestList = random.sample(range(1,32767),1000)
    NewList=sorted(testlist)
    print(NewList)
    X= int(input("enter number: "))
    print(InterpolationSearch(Newlist,1000,X))
    end_Time= time.time()
    Interval=(end_Time-start_Time)*1000
    Time_Interval.append(Interval)
print (sum(Time_Interval)//5)

TimeInter=[]
for i in range(1,6):
    starTime=time.time()
    testlist = random.sample(range(1,32767),5000)
    newList=sorted(testlist)
    print(newList)
    X= int(input("input number: "))
    print(InterSearch(Newlist,5000,X))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    TimeInter.append(Interval)
print (sum(TimeInter)//5)

'''Repeated time code with similar variable names to repeatedly run for 1000 and 5000'''







