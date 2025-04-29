import json

# Load the JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the JSON data
print("Name:", data["name"])
print("Age:", data["age"])
print("Email:", data["email"])
print("Address:", data["address"]["street"], data["address"]["city"])
