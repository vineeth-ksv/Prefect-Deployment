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
    for i in range(random.randint(3,6)):
        print(f"Starting Task - {i+1}")
        welcome()
        time.sleep(5)

if __name__ == '__main__':
    hello_world()