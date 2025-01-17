def count_and_largest(num):
    count = 0
    largestDigit = 0

    while num > 0:
        lastDigit = num % 10 
        if lastDigit > largestDigit:
            largestDigit = lastDigit
        num = num // 10 
        count += 1  
    return count, largestDigit


number = 987654
count, largestDigit = count_and_largest(number)
print("Number of digits:", count)          
print("Largest digit:", largestDigit)     
