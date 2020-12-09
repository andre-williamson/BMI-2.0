# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi= weight / (height * height) 
BMI = round(bmi)

if BMI < 18:
     print(f"you are{BMI} underweight")
elif BMI > 18:
    print(f" you are {BMI} normal weight ")
elif BMI < 25:    
    print(f" you are {BMI} normal weight ")
elif BMI > 25:
  print(f" you are {BMI} overweight ")
elif BMI < 30:
    print(f"you are {BMI} overweight")
elif BMI > 30:
    print(f"you are {BMI} are OBESE")                       
elif BMI < 35:
  print(f" you are {BMI} Fat as fuck ")
else:
  print(" you fat as f")                                                                               
