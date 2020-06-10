weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))
bmi = round(weight/(height*height), 1)
print("Your BMI is {}".format(bmi))