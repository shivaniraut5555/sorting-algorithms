'''
Quicksort 
it uses divide and conquer technique
divide:divide the list into subparts
conquer:find the result from all the subparts
combine:merge all the subparts to fom the final result

In this sort we choose any pivot element from the list(first/randam/last/mid or median(first,mid,last)) and sort recusively till all the smaller elements elements from pivot comes 
to the left side and larger elements comes to the right side

When pivot element is last index of the list,swap with the left index 
When pivot element is first index of the list,swap with the right index
step1:Select the pivot element
step2:Findout the correct position of pivot element in the list by rearranging it
step3:Divide the list based on pivot element
step4:Sort the sublist recursively
'''

def pivot_place(li,first,last):
    pivot=li[first]
    left=first+1
    right=last
    flag=1
    while True:
        while left<=right and li[left]<=pivot:#for descending order li[left]>=pivot
            left=left+1
        while left<=right and li[right]>=pivot:#for descdending order li[right]<=pivot
            right=right-1
        if left>right:
            break
        else:
            li[left],li[right]=li[right],li[left]
    li[first],li[right]=li[right],li[first]
    return right

def quick(li,first,last):
    if first<last:
        p=pivot_place(li,first,last)
        quick(li,first,p-1)
        quick(li,p+1,last)

n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements:")) for x in range(n)]
print("Unsorted list:",li)
quick(li,0,n-1)
print('List in ascending order is:',li)

