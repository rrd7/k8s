#lst = []
 
# number of elements as input
#n = int(input("Enter number of elements : "))
 
# iterating till the range
#for i in range(0, n):
 #   ele = int(input())
 
  #  lst.append(ele) # adding the element
     
#print(lst)

import enquiries

options = ['Do Something 1', 'Do Something 2', 'Do Something 3']
choice = enquiries.choose('Choose one of these options: ', options)

print(choice)
