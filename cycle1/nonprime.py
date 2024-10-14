start = int(input("enter the starting number:"))
end = int(input("enter the ending number:"))
print("non prime numbers are:")
for num in range(start, end + 1):
    if num > 1:
        flag = False
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print(num, end=" ")