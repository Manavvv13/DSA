def compute(num):
    count = 0
    largestDigit = 0
    temp = num
    rev = 0

    while num > 0:
        lastDigit = num % 10
        if lastDigit > largestDigit:
            largestDigit = lastDigit
        rev = rev * 10 + lastDigit
        num = num // 10
        count += 1
    isPalindrome = temp == rev
    return count, largestDigit, isPalindrome


number = int(input("Enter a number: "))
count, largestDigit, isPalindrome = compute(number)
print("Number of digits:", count)
print("Largest digit:", largestDigit)
print("Palindrome" if isPalindrome else "Not Palindrome")
