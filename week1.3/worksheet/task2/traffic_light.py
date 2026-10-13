"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mattis Evans
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

#print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime < maxtime:
    if state == "red":
        local_time = 0
        while local_time < 4 and systime < maxtime:
            print(f"Time {systime:03} State {state}")
            systime += 1
            local_time += 1
        state = "red_amber"
        continue
    if state == "red_amber":
        local_time = 0
        while local_time < 3 and systime < maxtime:
            print(f"Time {systime:03} State {state}")
            systime += 1
            local_time += 1
        state = "green"
        continue
    if state == "green":
        local_time = 0
        while local_time < 5 and systime < maxtime:
            print(f"Time {systime:03} State {state}")
            systime += 1
            local_time += 1
        state = "amber"
        continue
    if state == "amber":
        local_time = 0
        while local_time < 3 and systime < maxtime:
            print(f"Time {systime:03} State {state}")
            systime += 1
            local_time += 1
        state = "red"
        continue

# At the end of each step you should output the time and state using the statement on line 14