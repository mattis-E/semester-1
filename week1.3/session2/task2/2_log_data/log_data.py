# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file
lines = []
data = []
with open("site.log", "r") as file:
    lines = file.readlines()
    data = [l.strip().split(",") for l in lines]

# find all failed login attempts (POST /login with the response 401)
failed = [d for d in data if d[5] == "401" and d[4] == "POST /login"]
# and print these out in a human-readable format:
for f in failed:
    print(f"IP address {f[2]} failed to login at {f[1]} on {f[0]}")
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data