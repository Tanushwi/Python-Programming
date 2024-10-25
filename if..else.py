#Q1. WAP to check whether number is odd or even
# num=int(input("Enter number:"))
# if(num%2==0):
#     print("Even")
# else:    
#     print("Odd")

#Q2. WAP to check whether number is positive or negative
# num=int(input("Enter number:"))
# if(num>=0):
#     print("Positive")
# else:
#     print("Negative")

#Q3. WAP to check whether the person can cast vote or not
# age=int(input("Enter age:"))
# if(age>=18):
#     print("Able to Vote")
# else:
# print("Not Able to Vote")

#Q4. WAP to find maximum out of 2 numbers
# a=int(input("Enter one number:"))
# b=int(input("Enter another number:"))
# if(a>=b):
#     print("Greatest number is:",a)
# else:
#     print("Greatest number is:",b)

#Q5. Input basic salary and then calculate bonus and total salary acc to given conditions.
# basic=int(input("Enter basic salary:"))
# if(basic>=10000):
#     bonus=0.10*basic
# else:
#     bonus=0.05*basic
# print("Bonus is:",bonus)
# print("Total Salary is:",basic+bonus)

#Q6. WAP to check whether year is leap or not
#METHOD-1
# y=int(input("Enter year:"))
# if(y%4==0):
#     print("LEAP")
# else:
#     print("NOT LEAP")

#METHOD-2
# y=int(input("Enter year:"))
# if((y%100==0 and y%400==0)or(y%100!=0 and y%4==0)):
#     print("LEAP")
# else:
#     print("NOT LEAP")

#Q7. Input CP and SP.Calculate profit or loss
# cp=int(input("Enter cost price:"))
# sp=int(input("Enter selling price:"))
# if(cp>=sp):
#     print("Loss of:",cp-sp)
# else:
#     print("Profit of:",sp-cp)

#Q8. Input previous reading,new reading and meter type.Calculate unit consumed and bill
# p=int(input("Enter previous reading:"))
# n=int(input("Enter new reading:"))
# m=input("Enter meter type:")
# if(m=='d'or m=='D'):
#     r=4.50
# else:
#     r=6.50
# u=n-p
# print("Unit consumed is:",u)
# print("Bill is:",u*r)

#Q9. Input gender and greet accordingly
# gender=input("Enter gender:")
# if(gender=='male'):
#     print("GOOD MORNING SIR")
# else:
#     print("GOOD MORNING MAM")