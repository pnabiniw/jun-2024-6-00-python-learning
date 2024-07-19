"""
1. How to swap two variables in python without using a third variable?
2. What will be the output of following code?
"""

a = 2
b = 3
a, b = b, a

names = ["Jon", "Jane", "Eren", "Ragnar", "Arya"]
print(list(enumerate(names, start=1)))

# How to loop in this enumerated data?
for index, value in enumerate(names):
    print(index)
    print(value)