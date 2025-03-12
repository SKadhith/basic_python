def digital_root(n):
    while n >= 10:  
        n = sum(int(digit) for digit in str(n))  
    return n  

num = int(input("Enter a number: "))  
result = digital_root(num)  
print("Digital root:", result) 
