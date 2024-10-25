#Q1. Input marks of 3 subjects,calculate % and final result
# a=int(input("Enter marks of first subject:"))
# b=int(input("Enter marks of second subject:"))
# c=int(input("Enter marks of third subject:"))
# per=(a+b+c)*100/300
# if(per>=75):
#     print("Distinction")
# elif(per>=60 and per<75):
#     print("First Division")
# elif(per>=50 and per<60):
#     print("Second Division")
# else:
#     print("Fail")

#Q2. Input age and give result
# age=int(input("Enter age:"))
# if(age>=1 and age<=12):
#     print("Child")
# elif(age>=13 and age<=19):
#     print("Teenager")
# elif(age>=20 and age<=50):
#     print("Mature")
# else:
#     print("Old")

#Q3. Input alphabet and check whether it is vowel or consonant
# ch=input("Enter character:")
# if(ch=='a'or ch=='e'or ch=='i' or ch=='o' or ch=='u' or ch=='A'or ch=='E'or ch=='I' or ch=='O' or ch=='U'):
#     print("VOWEL")
# else:
#     print("CONSONANT")

#Q4. Input any month(1-12) and find season
# m=int(input("Enter month number:"))
# if(m==12 or m==1 or m==2):
#     print("WINTER")
# elif(m==3 or m==4 or m==5):
#     print("SPRING")
# elif(m==6 or m==7 or m==8):
#     print("SUMMER")
# elif(m==9 or m==10 or m==11):
#     print("AUTUMN")
# else:
#     print("INVENTED MONTH")

#Q5. Input any month(1-12) and year and find number of days in given month
# m=int(input("Enter month number:"))
# y=int(input("Enter year:"))
# if(m==4 or m==6 or m==9 or m==11):
#     print("30 DAYS")
# elif(m==2 and y%4==0):
#     print("29 DAYS")
# elif(m==2 and y%4!=0):
#     print("28 DAYS")
# else:
#     print("31 DAYS")

#Q6. Input marital status,gender and age and check whether the driver can be insured or not
# ma=input("Enter marital status:")
# g=input("Enter gender:")
# age=int(input("Enter age:"))
# if(ma=='married'):
#     print("CAN BE INSURED")
# elif(ma=='unmarried' and g=='male' and age>25):
#     print("CAN BE INSURED")
# elif(ma=='unmarried' and g=='female' and age>35):
#     print("CAN BE INSURED")
# else:
#     print("CANNOT BE INSURED")    

#Q7. Maximum out of 3 numbers
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if(a>b and a>c):
#     print("Maximum number is:",a)
# elif(b>a and b>c):
#     print("Maximum number is:",b)
# else:
#     print("Maximum number is:",c)