task = input("Enter your task")
priority = input("priority (high, medium, low):")
time_bound = input("Is it time-bound (yes or no):")

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: you need to complete {task}")
        else:
            print(f"Note: you need to complete {task}")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")