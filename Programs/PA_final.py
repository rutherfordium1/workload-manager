import psutil
import subprocess
from tasks import tasks

sorted_tasks = sorted(tasks, key=lambda x: x['priority'])

for task in sorted_tasks:
    # Get CPU usage for each core
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)

    # Get CPU temperatures for each core
    cpu_temperatures = psutil.sensors_temperatures()["coretemp"]

    # Combine core index, CPU usage, and temperature into a list of tuples
    data = list(zip(range(len(cpu_percentages)), cpu_percentages, cpu_temperatures))

    # Sort the data based on CPU usage and temperatures (in descending order)
    sorted_data = sorted(data, key=lambda x: (x[1], x[2].current), reverse=True)
    sorted_cores = [core for core, _ in sorted_data]

    # Extract the sorted core numbers
    sorted_core_numbers = [core for core, _ in sorted_data][:10]

    for core, usage, temp in sorted_data:
        print(f"Core {core}: {usage}% - Temperature: {temp.current}°C")

    # Form the taskset command
    command = ["taskset", "-c", ",".join(map(str, sorted_cores)), task["callout"]]

    # Print the task and assigned cores
    print(f"Running task '{task['name']}' on core(s): {sorted_core_numbers}")

    # Execute the command
    subprocess.run(command)

    # Wait for 5 seconds before proceeding to the next task
    time.sleep(5)
