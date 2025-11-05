# Program to calculate the length of a string without using len() function
text = input("Enter a string: ")

count = 0
for char in text:
    count += 1

print("Length of the string:", count)
