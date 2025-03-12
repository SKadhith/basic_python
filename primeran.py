def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Prime numbers:", [num for num in range(start, end + 1) if is_prime(num)])
