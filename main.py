from heapsort import heapSort

arr = list(map(int,input("enter the unsorted array:").split()))
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])
print()
print("*****","ABHISHANK PANDEY","181500011","GLA UNIVERSITY","SECTION-I","CLASS ROLL.NO-02", sep="\n")
