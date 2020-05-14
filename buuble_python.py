'''
Bubble sort
Some times reffred as sinking sort,is a simple sorting algorithm which sorts n number of elements in the 
list by comparing the each pair of adjacent items and swaps them if they are in wrong order
step1: Starting with the first element (index=0)cpompare the current element wih the next element of the list
step2:If the current element is greater/lesser than the next element of the list swap them
step3:If the current element is less than the next element,move to the next element,repeat step 1
'''

n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements:")) for x in range(n)]
print("Unsorted list:",li)
#ascending order
for j in range(len(li)-1):
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            li[i],li[i+1]=li[i+1],li[i] #swapping of number in the list
    print(f'The list after {j+1}th iteration:{li}')
print(f'Final sorted list:{li}')
#descdeing order
for j in range(len(li)-1):
    for i in range(len(li)-1):
        if li[i]<li[i+1]:
            li[i],li[i+1]=li[i+1],li[i] #swapping of number in the list
    print(f'The list after {j+1}th iteration:{li}')
print(f'Final sorted list:{li}')
