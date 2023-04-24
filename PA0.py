import os
import psutil
import time

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

# COOLING-AWARE TASK ALLOCATING

def get_cpu_temperature():
    res = os.popen('sensor').readlines()
    for line in res:
        if 'Core 0' in line:    # Assumes temperature reading is on Core 0
            return float(line.split('+')[1].split('C')[0])
        return 0

while True
            temp = get_cpu_temperature()
            if temp > 70:   # Adjust the temperature threshold as needed
                os.system('tasket -c 0-3 command1')     # Allocate command1 to CPUs 0-3
            else
                os.system('tasket -c 4-7 command2')     # Allocate command2 to CPUs 4-7

time.sleep(60)  # Sleep interval

# DYNAMIC CPU CLOCKING

# Set the governor to "ondemand"
os.system("sudo cpufreq-set -g ondemand")

# Set minimum and maximum frequency to 1.2GHz and 2.2 GHz respectively
os.system("sudo cpufreq-set -u 2200000")
os.system("sudo cpufreq-set -d 1200000")

while True:
    # Get the current CPU utilization
    cpu-util = psutil.cpu_percent()

    # Adjust the frequency based on the CPU utilization
    if cpu_util < 20:
        os.system("sudo cpufreq-set -f 1200000")
    if cpu_util < 50:
        os.system("sudo cpufreq-set -f 1600000")
    if cpu_util < 80:
        os.system("sudo cpufreq-set -f 2000000")
    if cpu_util < 100:
        os.system("sudo cpufreq-set -f 2200000")

    # Print the current CPU utilization and frequency
    ferq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
    print(f"CPU Utilization: {cpu_util}% | CPU frequency: {freq}")

    # Wait for the 5sec before checking the CPU utilization again
    time.sleep(5)
