#!/usr/bin/env python

def quicksort(arr,low,high):
    if low >= high:
        return
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot

    
##    i = low
##    j = low + 1
##    while j <= high:
##        if arr[j] < pivot:
##            temp = arr[i+1]
##            arr[i+1] = arr[j]
##            arr[j] = temp
##            i += 1
##        j += 1
##    arr[low] = arr[i]
##    arr[i] = pivot


    quicksort(arr,low,i-1)
    quicksort(arr,i+1,high)

if __name__ == "__main__":
    a = [15,423,3,67,78,32]
    quicksort(a,0,len(a)-1)
    print a
    










            
