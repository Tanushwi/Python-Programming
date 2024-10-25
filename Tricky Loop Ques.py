#Q1. Fibonna Series up to n numbers
# n=int(input("Enter value of n:"))
# a=int(input("Enter value of a:"))
# b=int(input("Enter value of b:"))
# c=0
# while(a<=n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#Q2. Print Prime Numbers up to n numbers
# n=int(input("Enter n:"))
# for num in range(1,n+1):
#     ctr=0
#     for i in range(2,num):
#         if(num%i==0):
#             ctr=1
#             break
#     if(ctr==0 and num!=1):
#         print(num)

#Q3. Out of n numbers if number is even then do its cube else square
# n=int(input("Enter n:"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(i,":",i*i*i)
#     else:
#         print(i,":",i*i)

#Q4. Out of n numbers count the numbers which end with 7
# n=int(input("Enter n:"))
# ctr=0
# for i in range(1,n+1):
#     if(i%10==7):
#         ctr+=1
# print("Total numbers which end with 7 are:",ctr)

#Q5. Out of n numbers count the numbers which are divisible by 7
# n=int(input("Enter n:"))
# ctr=0
# for i in range(1,n+1):
#     if(i%7==0):
#         ctr+=1
# print("Total numbers which are divisible by 7 are:",ctr)

#Q6. Solve the series 1+1/1!+2/2!+3/3!+......
# n=int(input("Enter n:"))
# sum=1
# for i in range(1,n+1):
#     fact=1
#     for j in range(i,0,-1):
#         fact=fact*j
#     sum=sum+i/fact
# print("Sum of the series is:",sum)

#Q7. Solve the series 1+1/1!+3/3!+......+n/n!
# n=int(input("Enter n:"))
# sum=1
# for i in range(1,n+1,2):
#     fact=1
#     for j in range(i,0,-1):
#         fact=fact*j
#     sum=sum+i/fact
# print("Sum is:",sum)

#Q8. Out of given n numbers count numbers which are prime
# n=int(input("Enter n:"))
# count=0
# for num in range(1,n+1):
#     ctr=0
#     for i in range(2,num):
#         if(num%i==0):
#             ctr=1
#             break
        
#     if(ctr==0 and num!=1):
#         count=count+1
# print("Total prime numbers up to ",n," numbers are:",count)