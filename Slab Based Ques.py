#Q1. WAP to input electricity unit charges and calculate total electricity bill according to given conditions
# unit=int(input("Enter units:"))
# if(unit<=50):
#     amt=0.50*unit
# elif(unit>50 and unit<=150):
#     amt=50*0.50+(unit-50)*0.75
# elif(unit>150 and unit<=250):
#     amt=50*0.50+100*0.75+(unit-150)*1.20
# else:
#     amt=50*0.50+100*0.75+100*1.20+(unit-250)*1.50
# add=20*amt/100
# print("Total bill before additional is:",amt)
# print("Total bill after additional is:",amt+add)

#Q2. WAP to calculate tax the person has to pay,based on their income
# income=int(input("Enter income:"))
# if(income<250000):
#     tax=0
# elif(income>=250000 and income<500000):
#     tax=5*(income-250000)/100
# elif(income>=500000 and income<1000000):
#     tax=5*250000/100+10*(income-500000)/100
# else:
#     tax=5*250000/100+10*500000/100+(income-1000000)*15/100
# print("Tax to be paid is:",tax)