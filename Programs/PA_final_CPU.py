import psutil
import subprocess
from tasks import tasks

sorted_tasks = sorted(tasks, key=lambda x: x['priority'])

for task in sorted_tasks:
    # Get CPU usage for each core
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)

    # Combine CPU usage and core indices into a list of tuples
    data = list(zip(range(len(cpu_percentages)), cpu_percentages))

    # Sort the data based on CPU usage (in descending order)
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    sorted_cores = [core for core, _ in sorted_data]

    # Extract the sorted core numbers
    sorted_core_numbers = [core for core, _ in sorted_data][:10]

    # Form the taskset command
    command = ["taskset", "-c", ",".join(map(str, sorted_cores)), task["callout"]]

    # Print the task and assigned cores
    print(f"Running task '{task['name']}' on core(s): {sorted_core_numbers}")

    # Execute the command
    subprocess.run(command)
