import subprocess
import time
import os
import psutil

# CPU temperature threshold in Celsius
TEMP_THRESHOLD = 70

# Start the power clamp
subprocess.Popen(["sudo", "modprobe", "msr"]) # load MSR kernel module
power_clamp = subprocess.Popen(["sudo", "intel_powerclamp", "-t", "3600"], stdout=subprocess.PIPE)

# Wait for a few seconds to let the power clamp stabilize
time.sleep(5)

# Get the maximum core temperature and frequency
output = subprocess.check_output(["sensors"], universal_newlines=True)
max_temp = max([float(line.split()[3][1:-2]) for line in output.splitlines() if "Core" in line])
output = subprocess.check_output(["cpufreq-info"], universal_newlines=True)
max_freq = float(output.splitlines()[0].split()[-1]) / 1000.0 # convert from kHz to GHz

# Get the number of CPU cores
num_cores = psutil.cpu_count(logical=False)

# Define the tasks
tasks = [
    {"name": "Task 1", "load": , "runtime": , 'script_path': '/path/to/your/script1.py'},
    {"name": "Task 2", "load": , "runtime": , 'script_path': '/path/to/your/script1.py'},
    {"name": "Task 3", "load": , "runtime": , 'script_path': '/path/to/your/script1.py'},
    {"name": "Task 4", "load": , "runtime": , 'script_path': '/path/to/your/script1.py'},
    {"name": "Task 5", "load": , "runtime": , 'script_path': '/path/to/your/script1.py'}
]

# Sort the tasks by deadline
tasks = sorted(tasks, key=lambda task: task["runtime"])

# Allocate tasks to CPU cores based on temperature and usage
allocated_tasks = {}
for task in tasks:
    # Find the available CPU core with the lowest temperature and usage
    min_temp = float("inf")
    min_usage = float("inf")
    min_core = None
    for core in range(num_cores):
        try:
            # Get the temperature and usage of the current CPU core
            output = subprocess.check_output(["sensors", "coretemp-isa-000{}".format(core)], universal_newlines=True)
            temp = float(output.split()[3][1:-2])
            usage = psutil.cpu_percent(percpu=True)[core]

            # Check if the current CPU core is available
            if temp < TEMP_THRESHOLD and usage < min_usage:
                min_temp = temp
                min_usage = usage
                min_core = core
        except (subprocess.CalledProcessError, IndexError):
            # Skip cores that are not available
            pass

    # If no available CPU core was found, wait and try again
    while min_core is None:
        time.sleep(1)
        for core in range(num_cores):
            try:
                # Get the temperature and usage of the current CPU core
                output = subprocess.check_output(["sensors", "coretemp-isa-000{}".format(core)], universal_newlines=True)
                temp = float(output.split()[3][1:-2])
                usage = psutil.cpu_percent(percpu=True)[core]

                # Check if the current CPU core is available
                if temp < TEMP_THRESHOLD and usage < min_usage:
                    min_temp = temp
                    min_usage = usage
                    min_core = core
            except (subprocess.CalledProcessError, IndexError):
                # Skip cores that are not available
                pass

    # Run the task
    freq = max_freq * (1.0 - task["load"])
    subprocess.Popen(["sudo", "cpufreq-set", "-c", str(min_core), "-f", "{:.2f}GHz".format(freq)])
    cmd = f"taskset -c {min_core} python {script_path}"  # Replace with the appropriate command to execute your task
    subprocess.Popen(cmd, shell=True)
    subprocess.Popen(["sudo", "cpufreq-set", "-c", str(min_core), "-f", "{:.2f}GHz".format(max_freq)])

    # Print task information
    print("Task '{}' completed in {:.2f} seconds".format(task["name"], task["runtime"]))

    # Print current CPU information
    output = subprocess.check_output(["sensors"], universal_newlines=True)
    temp = max([float(line.split()[3][1:-2]) for line in output.splitlines() if "Core" in line])
    output = subprocess.check_output(["cpufreq-info"], universal_newlines=True)
    freq = float(output.splitlines()[0].split()[-1]) / 1000.0 # convert from kHz to GHz
    power = float(power_clamp.stdout.readline().split()[-1][:-1]) / 1000.0 # convert from mW to W
    print("CPU temperature: {:.1f}°C, frequency: {:.2f}GHz, power usage: {:.1f}W".format(temp, freq, power))

# Terminate the power clamp
power_clamp.terminate()
