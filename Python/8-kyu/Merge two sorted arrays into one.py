def merge_arrays(arr1, arr2):
    merged_array = sorted(arr1 + arr2)
    
    merged_array_no_duplicates = list(set(merged_array))
    
    return sorted(merged_array_no_duplicates)
