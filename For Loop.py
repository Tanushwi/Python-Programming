#Q1. Sum of first n natural numbers
# n=int(input("Enter n:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("Sum of natural numbers is:",sum)

#Q2. Table of a number
# n=int(input("Enter number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

#Q3. Factorial of a number
# n=int(input("Enter number:"))
# fact=1
# for i in range(n,0,-1):
#     fact=fact*i
# print("Factorial of ",n," is:",fact)

#Q4. Sum and average of n numbers
# n=int(input("Enter n:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("Sum is:",sum)
# print("Average is:",sum/n)

#Q5. Count odd and even
# n=int(input("Enter n:"))
# o=0
# e=0
# for i in range(1,n+1):
#     if(i%2==0):
#         e+=1
#     else:
#         o+=1
# print("Total odds is:",o)
# print("Total evens:",e)
  
#Q6. Sum of factors
# n=int(input("Enter n:"))
# sum=0
# for i in range(1,n+1):
#     if(n%i==0):
#         sum=sum+i 
# print(sum) 

#Q7. Check whether the number is prime or not
# num=int(input("Enter number:"))
# ctr=0
# for i in range(2,num):
#     if(num%i==0):
#         ctr=1
#         break
# if(ctr==0):
#     print("PRIME")
# else:
#     print("NOT PRIME")

#Q8. Fibonacci Series
# a=int(input("Enter value of a:"))
# b=int(input("Enter value of b:"))
# for i in range(10):
#     print(a)
#     c=a+b
#     a=b
#     b=c