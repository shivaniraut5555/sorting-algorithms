'''
Merge Sort algorithm follows divide and comquer technique which works in three ways
divide:divide the list into subparts
conquer:find the result from all the subparts
combine:merge all the subparts to fom the final result

step1:split the sorted list
step2:compare  each of the elements and group them
step3:repeat step 2 until whole list is merged and sorted
'''

def merge_asc(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        merge_asc(lefthalf)
        merge_asc(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]: # for descending order lefthalf[i] > righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    return li

n=int(input("Enter the number of elements:"))#input of elements of list 
li=[int(input("Enter elements:")) for x in range(n)]
print("Unsorted list:",li)
print('List in ascending order is:',merge_asc(li))
