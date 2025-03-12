def find_missing_numbers(arr, n):
    full_set = set(range(1, n + 1))  
    given_set = set(arr)  
    missing_numbers = sorted(list(full_set - given_set))
    return missing_numbers
n = 10  
arr = [1, 2, 4, 5, 7, 8, 10] 
missing = find_missing_numbers(arr, n)
print("The missing numbers are:", missing)

