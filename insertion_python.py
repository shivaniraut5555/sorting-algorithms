'''
Insertion Sort
it is a simple sorting algorithm that final sorted array list one item at a time
step1:Consider the first element to be sorted and the rest to be unsorted
step2:Take the first element in the unsorted part(u1) and compare it with sorted part elements(s1)
step3: if u1<s1 then insert u1 in the correct index,else leave it as it is
step4:Take next elementin the unsorted part and compare with sorted elements
step5:Repeat 3 and 4 until all the elements are sorted
'''
n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements:")) for x in range(n)]
print("Unsorted list:",li)
for i in range(1,len(li)):
    curr_ele=li[i]#taking current elemntas ith index
    pos=i#saving the position of current element
    while(curr_ele<li[pos-1] and pos>0):#for descending order curr_ele>li[pos-1]
        li[pos]=li[pos-1]
        pos=pos-1
    li[pos]=curr_ele
    print(f'After {i} iteration :',li)    
print("Sorted array:",li)    
print("Sorted array:",li)
