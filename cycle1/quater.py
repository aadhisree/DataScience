import math
a=int(input("enter the number of a:"))
b=int(input("enter the number of b:"))
c=int(input("enter the number of c:"))
dis = b*b-4*a*c
d=2*a
if dis < 0:
    print("the equation has no real root")
elif dis ==0:
    root= -b/d
    print(f"equation have 1 root; {round(root,2)}")
else:
    root1= (-b+math.sqrt(dis))/d
    root2= (-b-math.sqrt(dis))/d
    print("equation have 2")
    print("root1=",round(root1,2))
    print("root2=",round(root2,2))