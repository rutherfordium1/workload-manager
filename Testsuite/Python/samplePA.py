import subprocess
import time

# Define the tasks
tasks = [
    {"name": "Task 1", "load": 0.3, "deadline": 10},
    {"name": "Task 2", "load": 0.5, "deadline": 15},
    {"name": "Task 3", "load": 0.2, "deadline": 5},
    {"name": "Task 4", "load": 0.7, "deadline": 20},
    {"name": "Task 5", "load": 0.4, "deadline": 12}
]

# Allocate tasks to CPU cores based on load
allocated_tasks = {}
for task in tasks:
    # Find the CPU core with the lowest load
    min_load = float("inf")
    min_core = None
    for core in range(num_cores):
        load = get_cpu_load(core)  # Function to get CPU load of a core
        if load < min_load:
            min_load = load
            min_core = core

    # If no available CPU core was found, wait and try again
    while min_core is None:
        time.sleep(1)
        for core in range(num_cores):
            load = get_cpu_load(core)  # Function to get CPU load of a core
            if load < min_load:
                min_load = load
                min_core = core

    # Assign the task to the selected CPU core
    allocated_tasks[task["name"]] = min_core
    set_cpu_load(min_core, task["load"])  # Function to set CPU load of a core

# Run the tasks
for task in tasks:
    task_name = task["name"]
    core = allocated_tasks[task_name]
    script = task["script"]
    print(f"Running {task_name} on CPU core {core}")

    # Run the task using subprocess
    subprocess.Popen(["python3", "name"])

    time.sleep(task["deadline"])  # Sleep for the task's deadline duration

    # Reset the CPU load after task completion
    set_cpu_load(core, 0)  # Function to set CPU load of a core
    print(f"Task {task_name} completed")
