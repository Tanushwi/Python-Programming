#Q1. Sum of digits of a number
# num=int(input("Enter the number:"))
# temp=num
# sum=0
# while(temp!=0):
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10
# print("Sum of digits of ",num," is:",sum)

#Q2. Reverse of a number
# num=int(input("Enter the number:"))
# temp=num
# sum=0
# while(num!=0):
#     digit=num%10
#     sum=sum*10+digit
#     num=num//10
# print("Reverse of ",temp," is:",sum)

#Q3. Number is Pallindrome or not
# num=int(input("Enter the number:"))
# temp=num
# sum=0
# while(num!=0):
#     digit=num%10
#     sum=sum*10+digit
#     num=num//10
# if(temp==sum):
#     print("PALLINDROME")
# else:
#     print("NOT PALLINDROME")

#Q4. Count the digits of a number
# num=int(input("Enter number:"))
# ctr=0
# temp=num
# while(temp!=0):
#     ctr+=1
#     temp=temp//10
# print("Total Digits of ",num," is:",ctr)

#Q5. Check whether the number is armstrong or not
# num=int(input("Enter number:"))
# ctr=0
# temp=num
# while(temp!=0):
#     ctr+=1
#     temp=temp//10
# sum=0
# temp=num
# while(num!=0):
#     digit=num%10
#     sum=sum+digit**ctr
#     num=num//10
# if(temp==sum):
#     print("ARMSTRONG")
# else:
#     print("NOT ARMSTRONG")

#Q6. Binary to decimal conversion
# num=int(input("Enter binary number:"))
# temp=num
# sum=0
# i=0
# while(num!=0):
#     digit=num%10
#     sum=sum+digit*2**i
#     i+=1
#     num=num//10
# print("DECIMAL VALUE OF ",temp," is:",sum)