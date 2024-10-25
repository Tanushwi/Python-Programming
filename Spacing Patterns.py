# Q1.
#   *
#  ***
# *****
# n=1
# sp=2
# for i in range(1,4):
#     for j in range(sp):
#         print(" ",end='')
#     for j in range(1,n+1):
#         print("*",end='')
#     sp=sp-1
#     n=n+2
#     print()
    
# Q2
#     1
#    121
#   12321
#  1234321
# 123454321
# sp=4
# for i in range(1,6):
#     for j in range(sp):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     sp=sp-1
#     print()

# Q3. 
#     1
#    212
#   32123
#  4321234
# 543212345
# sp=4
# for i in range(1,6):
#     for j in range(sp):
#         print(" ",end='')
#     for j in range(i,0,-1):
#         print(j,end='')
#     for j in range(2,i+1):
#         print(j,end='')
#     sp=sp-1
#     print()

# Q4.
# 1234554321
# 1234  4321
# 123    321
# 12      21
# 1        1
# sp=0
# n=int(input("Enter n:"))
# for i in range(0,n):
#     for j in range(1,n-i+1):
#         print(j,end='')
#     for j in range(sp):
#         print(" ",end='')
#     for j in range(n-i,0,-1):
#         print(j,end='')
#     sp=sp+2
#     print()




