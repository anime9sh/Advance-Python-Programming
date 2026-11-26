import csv

# Data to be written
Animesh = [
    ["Hello my name is Animesh Rawas"],
    ["My department is CSE"],
    ["I am from CSE Department"]
]

# Create and write to CSV file
with open("ani.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(ani)

print("CSV file created successfully.")

# Read data from CSV file
with open("ani.csv", "r") as file:
    lines = file.readlines()

# Display the data
for line in lines:
    print(line.strip())
