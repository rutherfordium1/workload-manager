import os
import time
import psutil
import subprocess

# Install necessary packages
    ## lm-sensors
    os.system("sudo apt update -y")
    os.system("sudo apt-get install lm-sensors")
    ## python3-psutil
    os.system("sudo apt update -y")
    os.system("sudo apt-get install python3-psutil")
    ## cpufrequtils
    os.system("sudo apt update -y")
    os.system("sudo apt-get install cpufrequtils")
    ## linux-tools-common linux-tools-generic
    os.system("sudo apt update -y")
    os.system("sudo apt-get install linux-tools-common linux-tools-generic")

# Cooling-Aware Task-Allocation Policy

## Get the number of CPU cores
num_cores = psutil.cpu_count()

## Define a list of tasks to be allocated to CPU cores
tasks = ['task1', 'task2', 'task3', 'task4', 'task5']

## Loop through the tasks and allocate them to CPU cores based on temperature and usage
for i, task in enumerate(tasks):
    ### Get the current temperature and usage of each CPU core
    cpu_stats = psutil.cpu_percent(interval=1, percpu=True)
    core_temps = psutil.sensors_temperatures()['coretemp']

    ### Combine the temperature and usage data into a single list
    core_data = zip(core_temps, cpu_stats)

    ### Sort the cores by temperature and usage, in ascending order
    core_data.sort(key=lambda x: (x[0].current, x[1]))

    ### Allocate the task to the core with the lowest temperature and lowest usage
    cpu_core = core_data[0][0].label.split(" ")[1]

    ### Execute the task on the designated CPU core
    cmd = f"taskset -c {cpu_core} python {task}.py"  # Replace with the appropriate command to execute your task
    subprocess.Popen(cmd, shell=True)


# DYNAMIC CPU CLOCKING

## Set the governor to "ondemand"
os.system("sudo cpufreq-set -g ondemand")

## Set minimum and maximum frequency to 1.2GHz and 2.2 GHz respectively
os.system("sudo cpufreq-set -u 2200000")
os.system("sudo cpufreq-set -d 1200000")

while True:
    ### Get the current CPU utilization
    cpu-util = psutil.cpu_percent()

    ### Adjust the frequency based on the CPU utilization
    if cpu_util < 20:
        os.system("sudo cpufreq-set -f 1200000")
    if cpu_util < 50:
        os.system("sudo cpufreq-set -f 1600000")
    if cpu_util < 80:
        os.system("sudo cpufreq-set -f 2000000")
    if cpu_util < 100:
        os.system("sudo cpufreq-set -f 2200000")

    ### Print the current CPU utilization and frequency
    ferq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
    print(f"CPU Utilization: {cpu_util}% | CPU frequency: {freq}")

    ## Wait for the 5sec before checking the CPU utilization again
    time.sleep(5)
