def merge(l1, l2):
    sorted_arr = []
    arr1,arr2 = l1.copy(),l2.copy()
    while len(arr1)>0 and len(arr2)>0:
        sorted_arr.append(arr1.pop(0) if arr1[0]<arr2[0] else arr2.pop(0))
    sorted_arr += arr1
    sorted_arr += arr2        
    return sorted_arr

def merge_v2(arr1,arr2):
    sorted_arr = []
    i,j = 0,0
    n,m = len(arr1),len(arr2)
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    sorted_arr += [arr1[i:],arr2[j:]][j<m]
    return sorted_arr
    

def merge_sort(arr):
    n = len(arr)
    if n==1 or n==0:
        return arr
    current_left = merge_sort(arr[:n//2])
    current_right = merge_sort(arr[n//2:])
    return merge(current_left,current_right)

l = [3,2,2,5,2,1]
s = merge_sort(l)
print(s)