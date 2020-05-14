'''
Selection sort
step1:Strating the first element search for the smallest(biggest) element in the list of numbers
step2:Swap minimum(maximum) number with first element
step3:Take the sublist(ignore sorted part) and repeat step1 and 2 until all the elemnts are sorted
'''
n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements")) for x in range(n)]
print("Unsorted list:",li)
#ascending order
for j in range(len(li)):
    min_val=min(li[j:])#finding minimum value
    '''
    or without min functiion
    min_val=li[j]
    for i in range(j+1,(len(li)):
        if min_val<li[i]:
            min_val=li[i]
    '''
    min_inx=li.index(min_val)#stroing the index of minimum value
    li[j],li[min_inx]=li[min_inx],li[j]#swapping with the 0th position
    print(f'The list after {j+1} iteration:{li}')
print(f'Final sorted list:{li}')
#descending order
for j in range(len(li)):
    min_val=max(li[j:])#finding minimum value
    min_inx=li.index(min_val)#stroing the index of minimum value
    li[j],li[min_inx]=li[min_inx],li[j]#swapping with the 0th position
    print(f'The list after {j+1} iteration:{li}')
print(f'Final sorted list:{li}')
#for duplicate numbers
for j in range(len(li)):
    min_val=min(li[j:])#finding minimum value
    min_inx=li.index(min_val,j)#stroing the index of minimum value
    li[j],li[min_inx]=li[min_inx],li[j]#swapping with the 0th position
    print(f'The list after {j+1} iteration:{li}')
print(f'Final sorted list:{li}')

            
