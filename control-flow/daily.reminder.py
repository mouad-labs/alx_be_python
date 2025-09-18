# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Use Match Case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an undefined priority"

# Modify based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
