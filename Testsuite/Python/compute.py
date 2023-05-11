import time

def compute():
    # Perform some computation
    for i in range(10000000):
        _ = i**2

    # Sleep for a random duration
    time.sleep(5)

if __name__ == '__main__':
    compute()
