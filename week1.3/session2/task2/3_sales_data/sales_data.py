# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
lines = []
with open("sales.csv", "r") as file:
    lines = file.readlines()

# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
largest_sale_amount = 0
largest_sale_day = ""
sale_amount_sum = 0
widget_counters = {"Widget A": 0, "Widget B": 0, "Widget C": 0, "Widget D": 0}
widget_list = [0, 0, 0, 0]
lines.pop(0)
for line in lines:
    line = line.split(",")
    # find largest sale day
    sale_amount_sum += int(line[2])
    if int(line[2]) > largest_sale_amount:
        largest_sale_amount = int(line[2])
        largest_sale_day = line[0]
    match line[1]:
        case "Widget A":
            widget_counters["Widget A"] += int(line[3])
            widget_list[0] += int(line[3])
        case "Widget B":
            widget_counters["Widget B"] += int(line[3])
            widget_list[1] += int(line[3])
        case "Widget C":
            widget_counters["Widget C"] += int(line[3])
            widget_list[2] += int(line[3])
        case "Widget D":
            widget_counters["Widget D"] += int(line[3])
            widget_list[3] += int(line[3])
widget_list.sort()

print(f"Largest sale amount: {largest_sale_amount} on {largest_sale_day}.")
print(f"Average sale amount: {sale_amount_sum / len(lines)}.")
print(f"Widget which has sold the most: {[key for key, val in widget_counters.items() if val == widget_list[3]]}")


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows