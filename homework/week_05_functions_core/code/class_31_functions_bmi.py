# Write a function named bmi(weight, height) that returns the Body Mass Index (BMI).
# Ek function bmi(weight, height) jo BMI return kare (weight / height**2).

def bmi(weight, height):
    bmi_index = weight / height**2
    return bmi_index

weight = 80
height = 1.8
final_bmi = bmi(weight, height)
print(f"final_bmi is: {final_bmi:.2f}")




