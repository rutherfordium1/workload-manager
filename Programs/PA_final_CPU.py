import psutil
import subprocess
import time
from tasks import tasks

sorted_tasks = sorted(tasks, key=lambda x: x['priority'])

# Initialize core temperatures to zero
cpu_temperatures = [0] * psutil.cpu_count()

for task in sorted_tasks:
    # Get CPU usage for each core
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)

    # Combine core index, CPU usage, and temperature into a list of tuples
    data = list(zip(range(len(cpu_percentages)), cpu_percentages, cpu_temperatures))

    # Sort the data based on CPU usage and temperatures (in ascending order)
    sorted_data = sorted(data, key=lambda x: (x[1], x[2]))
    sorted_cores = [core for core, _, _ in sorted_data]

    # Extract the sorted core numbers
    sorted_core_numbers = [core for core, _, _ in sorted_data][:10]

    # Print the sorted data
    for core, usage, temp in sorted_data:
        print(f"Core {core}: {usage}% - Temperature: {temp}°C")

    # Form the taskset command
    command = ["taskset", "-c", ",".join(map(str, sorted_cores)), task["callout"]]

    # Print the task and assigned cores
    print(f"Running task '{task['name']}' on core(s): {sorted_core_numbers}")

    # Execute the command
    subprocess.run(command)

    # Wait for the task to complete
    time.sleep(5)  # Adjust the delay as needed

    # Update the CPU core temperature for the assigned cores of the executed task
    for core in sorted_core_numbers:
        cpu_temperatures[core] = task.get("temp", 0)

    # Wait for 5 seconds before proceeding to the next task
    time.sleep(5)
