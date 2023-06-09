weight = float(input())
height = float(input())

bmi = weight / (height * height)
    
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print('Normal weight')
elif bmi >= 25:
    print('Overweight')