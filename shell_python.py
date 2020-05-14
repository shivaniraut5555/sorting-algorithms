'''
Shell sort
By breaking the original list into a number of smaller sublists,each sublist is sorted using the insertion sort
It will move the items nearer to its original index
step1:Take the list of numbers
step2:Find out the gap(turnacted division 2)/incrementor
step3:Create the sublist based on gap and sort them using insertion sort algorithm
step4:reduce gap and repeat step3
step5:stop when gap is 0
'''
def shell_asc(li):
    gap=len(li)//2#turncated gap
    while(gap>0):
        for i in range(gap,len(li)):
            curr_ele=li[i]
            pos=i
            while(pos>=gap and curr_ele<li[pos-gap]):#comparison with index gap, for descending order " curr_ele>li[pos-gap]):"
                li[pos]=li[pos-gap]
                pos=pos-gap
            li[pos]=curr_ele
        print(f'In the gap {gap} list is:{li}')
        gap=gap//2#reducing gap
    return li
n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements:")) for x in range(n)]
print("Unsorted list:",li)
print('List in ascending order is:',shell_asc(li))
