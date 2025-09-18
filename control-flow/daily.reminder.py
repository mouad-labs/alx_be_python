Task = input("What is your task?:")
Priority = input("Task’s priority (high, medium, low):")
Time_bound = input("Is the task is time-bound (yes or no):")

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