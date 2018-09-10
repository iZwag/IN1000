# Self-made task: Use dictionaries to store a database of minimum 3 stores, with a list of opening hours
# (at least when they close). Use the datetime package to check what day it is, and let the user
# input what store it wants to check. Then return the closing hours for that store for the given day.
# This has similarities with the food plan task, but introduces more challenge.

import datetime as dt

# Database of how long the stores hold open
opening_hours = {   "Vinmonopolet" : ["18:00", "18:00", "18:00", "18:00", "18:00", "15:00", "closed"],
                    "Kiwi" : ["23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "closed"],
                    "Storo Storsenter" : ["21:00", "21:00", "21:00", "21:00", "21:00", "19:00", "closed"]}

# Ask for store to check
store = input("Please enter the name of store, and I will tell you when it closes today: ")

# Find current day, ranging from 0 = monday, 1 = tuesday, 2 = wednesday and so on using the datetime library
day = dt.datetime.today().weekday()

# Checks if the store is in the database, and returns the closing time, unless its a day it holds closed.
if store in opening_hours:
    if opening_hours[store][day] == "closed":
        print("%s is closed today." % store)
    else:
        closed = opening_hours[store][day]
        print("%s closes at %s today." % (store, closed))
else:
    print("Sorry, there are no information available for that store.")


