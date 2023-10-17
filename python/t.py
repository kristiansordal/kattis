import random


# Function to generate a random integer between 2 and 100
def generate_random_number():
    return random.randint(2, 100)


# Function to generate a list of random numbers between 2 and 100
def generate_random_numbers(count):
    return [generate_random_number() for _ in range(count)]


# Function to write space-separated numbers to a file
def write_numbers_to_file(file, numbers):
    file.write(" ".join(map(str, numbers)))
    file.write("\n")


# Generate the three random numbers for x, y, and z
x = generate_random_number()
y = generate_random_number()
z = generate_random_number()

# Generate x, y, and z space-separated numbers
x_numbers = generate_random_numbers(x)
y_numbers = generate_random_numbers(y)
z_numbers = generate_random_numbers(z)

# Write the data to the file
with open("t.txt", "w") as file:
    file.write(f"{x} {y} {z}\n")
    write_numbers_to_file(file, x_numbers)
    write_numbers_to_file(file, y_numbers)
    write_numbers_to_file(file, z_numbers)

print("Data has been written to t.txt")
