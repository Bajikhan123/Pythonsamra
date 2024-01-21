# QNo 1 (Answer)

# Declare and initialize variables
num1 = 10
num2 = 20

# Calculate the sum
sum_result = num1 + num2

# Print the result
print("The sum of", num1, "and", num2, "is:", sum_result)

# QNo 2 (Answer)

# Create and initialize the variable
message = "Hello"

# Append another string
message += " World!"

# Print the result
print(message)

# QNo 3 (Answer)

# Define and initialize the variable
is_python_fun = True  # Change this to False if Python is not considered fun

# Print a statement based on the value of is_python_fun
if is_python_fun:
    print("Python is fun!")
else:
    print("Python might not be everyone's idea of fun.")

# QNo 4 (Answer)

# Create and initialize the list
fruits = ["Apple", "Banana", "Orange"]

# Print the original list
print("Original list of fruits:", fruits)

# Add a new fruit to the list
fruits.append("Grapes")

# Print the updated list
print("Updated list of fruits:", fruits)

# QNo 5 (Answer)

# Declare and initialize the variable with a floating-point value
price = 75.12

# Convert the floating-point value to an integer
price_integer = int(price)

# Print the original and converted values
print("Original price:", price)
print("Converted price (as integer):", price_integer)

# QNo 6 (Answer)

# Create and initialize the dictionary
student_info = {
    'name': 'Ali',
    'age': 20,
    'grade': 'A+'
}

# Print the dictionary
print("Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])

# QNo 7 (Answer)


# Get user input for age
user_age = input("Enter your age: ")

# Convert the input to an integer
age = int(user_age)

# Determine the age group and print a message
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# QNo 8 (Answer)


# Define and initialize the complex number
comp_num = 3 + 4j  # Example: 3 is the real part, 4 is the imaginary part

# Access and print the real and imaginary parts separately
print("Real part:", comp_num.real)
print("Imaginary part:", comp_num.imag)

# QNo 9 (Answer)

# Two strings to be concatenated
string1 = "Hello"
string2 = "World!"

# Combine strings using string concatenation
combined_string = string1 + " " + string2

# Use string interpolation to include the length in a print statement
print(f"The combined string is: {combined_string}. It has a length of {len(combined_string)} characters.")

# QNo 10 (Answer)


# Create and initialize the tuple
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Access and print the third day of the week (index 2)
third_day = days_of_week[2]
print("The third day of the week is:", third_day)
