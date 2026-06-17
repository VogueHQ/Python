'''BMI Calculator
Take the user's weight (in kg) and height (in meters) as input. Calculate BMI using:
BMI = weight / (height * height)
Then print the category:

Below 18.5 → Underweight
18.5 to 24.9 → Normal weight
25 to 29.9 → Overweight
30 or above → Obese'''


# w = int(input("Enter your weight in kg: "))
# h = int(input("Enter your height in meters: "))

# bmi = (w/(h*h))
                                        #this is the code by me
# if(bmi<18.5):
#     print("Underweight")
# elif(bmi>=18.5 and bmi<=24.9):
#     print("Normal weight")
# elif(bmi>=25 and bmi<=29.9):
#     print("Overweight")
# elif(bmi>=30):
#     print("Obese")



w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))

bmi = w / (h * h)
                            #code by claude
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")



# understood completly
