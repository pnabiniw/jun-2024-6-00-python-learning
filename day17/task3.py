"""
WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
import time

# @time_taken
def long_loop():
    for i in range(100000000):
        pass

start = time.time()
long_loop()
end = time.time()

print("Taken time is", end-start)





