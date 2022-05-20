age=int(input("Enter your age\n"))
sex=input("Enter sex (M|f)")
a=int(input("Enter the number of days\n"))
if age>=18 and age<30 and sex is 'M':
 b=a*700
 print("Your total wages is rupees only:",b)
elif age>=18 and age<30 and sex is 'F':
 c=a*750
 print("Your total wages is rupees only:",c)
elif age>=30 and age<45 and sex is 'M':
 d=a*800
 print("Your total wages is rupees only:",d)
elif age>=30 and age<45 and sex is 'F':
 e=a*750
 print("Your total wages is rupees only:",e)
else:
 print("Your total wages is 1000 rupees only:")

