from datetime import datetime  # Import datetime module

# Ask user input for date
user_date_str = input("Enter a specific date (dd/mm/yyyy): ")

# Convert user input (string) to a datetime object
# Convert user input to datetime object
user_date = datetime.strptime(user_date_str, "%d/%m/%Y")

# Get current date
current_date = datetime.now()

# Calculate age
age = current_date.year - user_date.year

if age > 0:
    print(f"Age is {age}")  # Print age
elif age < 0:
    print("Invalid date entered")  # Print error message
