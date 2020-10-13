n = int(input("Please Enter the number of steps: "))
m = 1
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(1,m+1):
        print("*",end="")
    m=m+2
    print("\r")
print("-----------------------------------------------")
m = 1
for i in range(1,n):
    m = m+2
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(1,m+1):
        print("*",end="")
    m = m-2
    print("\r")
print("-----------------------------------------------")
m = 1
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(1,m+1):
        print("*",end="")
    m=m+2
    print("\r")
m = 1
for i in range(1,n-1):
    m = m+2
for i in range(n-1):
    for k in range(i+1):
        print(" ",end="")
    for j in range(1,m+1):
        print("*",end="")
    m = m-2
    print("\r")
print("-----------------------------------------------")
