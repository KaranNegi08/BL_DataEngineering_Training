import time
import math

def stop_watch():
    input("Click enter to start the timer. ")
    start_time= time.time()

    input("Click enter to stop the timer. ")
    end_time= time.time()

    elapsed = end_time - start_time
    print(f"The time between start and end click is {elapsed:.2f}")


stop_watch()

