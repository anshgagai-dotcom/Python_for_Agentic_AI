"""✍️ Homework — Pehle pseudocode likho (kaagaz), PHIR code
Ek number lo aur batao woh positive, negative ya zero hai.
Ek list of marks lo aur unka average nikalo.
1 se 20 tak ke numbers mein se sirf 3 ke multiples print karo."""



# Take a number as input and print whether it is Positive, Negative, or Zero.

"""Take a number.
If the number is greater than 0
    Print "Positive"

Else if the number is less than 0
    Print "Negative"
Else
    Print "Zero" """


n = int(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")






# Take a list of marks and calculate the average of all the marks.

"""Take a list of marks.
Set total to 0.
For each mark in the list
    Add the mark to total.
Divide total by the number of marks.
Print the average."""


marks = [40, 55, 70, 90]
total = 0
for m in marks:
    total = total + m
average = total / len(marks)
print(average)






# Print only the multiples of 3 from 1 to 20.

"""Start from 1.
Go up to 20.
For each number
    If the number is divisible by 3
        Print the number."""



for n in range(1, 21):
    if n % 3 == 0:
        print(n)

        