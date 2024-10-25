#Q1. Maximum out of 3 numbers
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if(a>b):
#     if(a>c):
#         print("Maximum number is:",a)
#     else:
#         print("Maximum number is:",c)
# else:
#     if(b>c):
#         print("Maximum number is:",b)
#     else:
#         print("Maximum number is:",c)    
        
#Q2. Maximum out of 4 numbers
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# d=int(input("Enter fourth number:"))
# if(a>b):
#     if(a>c):
#         if(a>d):
#             print("Maximum number is:",a)
#         else:
#             print("Maximum number is:",d)
#     else:
#         if(c>d):
#             print("Maximum number is:",c)
#         else:
#             print("Maximum number is:",d)
# else:
#     if(b>c):
#         if(b>d):
#             print("Maximum number is:",b)
#         else:
#             print("Maximum number is:",d)
#     else:
#         if(c>d):
#             print("Maximum number is:",c)
#         else:
#             print("Maximum number is:",d)

#Q3. Input marital status,gender and age and check whether the driver can be insured or not
# ma=input("Enter marital status:")
# if(ma=='married'):
#     print("Can be insured")
# else:
#     g=input("Enter gender:")
#     age=int(input("Enter age:"))
#     if(g=='male'):
#         if(age>25):
#             print("Can be insured")
#         else:
#             print("Cannot be insured")
#     else:
#         if(age>35):
#             print("Can be insured")
#         else:
#             print("Cannot be insured")

#Q4. Input any month(1-12) and year and find number of days in given month
# m=int(input("Enter month number:"))
# if(m==4 or m==6 or m==9 or m==11):
#     print("30 DAYS")
# elif(m==2):
#     y=int(input("Enter year:"))
#     if(y%4==0):
#         print("29 DAYS")
#     else:
#         print("28 DAYS")
# else:
#     print("31 DAYS")