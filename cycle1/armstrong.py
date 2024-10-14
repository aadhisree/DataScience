limit=1000
for num in range(1,limit):
    str_n=str(num)
    count=len(str_n)
    sum=0
    for i in str_n:
        sum +=int(i) ** count
    if sum ==num:
        print(num)
