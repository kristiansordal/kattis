import random


# Function to generate a random double point in the format "x y"
def generate_random_point():
    x = round(random.uniform(0, 10), 2)
    y = round(random.uniform(0, 10), 2)
    return f"{x} {y}"


# Generate a random n between 1 and 10
n = random.randint(2, 100)

# Specify the number of times to repeat the process
m = 5  # You can change this value as needed

# Open the file 't.txt' for writing
with open("t.txt", "w") as file:
    # Write the random n to the file
    file.write(f"{n}\n")

    # Write n random double points to the file
    for _ in range(n):
        random_point = generate_random_point()
        file.write(f"{random_point}\n")

    # Repeat the process 'm' times
    for _ in range(m):
        n = random.randint(1, 10)
        file.write(f"{n}\n")
        for _ in range(n):
            random_point = generate_random_point()
            file.write(f"{random_point}\n")

    # Write 0 to the file at the end
    file.write("0\n")

print("File 't.txt' has been created.")
