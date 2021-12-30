def insertion_sort(arr):
    n=len(arr)
    key = 1
    working_index=0
    while key<n:
        if arr[key]<arr[key-1]:
            arr[key],arr[key-1]=arr[key-1],arr[key]
            working_index = key-1
            while working_index>0 and arr[working_index]<arr[working_index-1]:
                arr[working_index],arr[working_index-1]=arr[working_index-1],arr[working_index]
                working_index-=1
        print(f"After iteration number {key}: {arr}")
        key+=1

l = [3,9,4,8,1,2,6,8,7,5]
print(f"Non sorted list: {l}")
insertion_sort(l)
print(f"Sorted list: {l}")