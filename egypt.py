a = int(input("a= "))
b = int(input("b= "))

i = 0

while b != 0:
    if(b % 2 == 1):
        i += a
    b //= 2
    a = a+a
    
print(i)