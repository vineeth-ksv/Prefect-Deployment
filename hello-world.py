from prefect import flow, task
from datetime import datetime
import random
import time

@task
def welcome():
    print(f"Hello World!!")
    print(f"Current timestamp: {datetime.now()}")

@flow(log_prints=True)
def hello_world():
    n = random.randint(3,6)
    print(f"number of tasks generated - {n}")
    for i in range(n):
        print(f"Starting Task - {i+1}")
        welcome()
        time.sleep(5)

if __name__ == '__main__':
    hello_world()