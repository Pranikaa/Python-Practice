weekly_expences = {
    'Sunday' : 1000,
    'Monday' : 2000,
    'Tuesday' : 1500, 
    'Wednesday' : 20,
    'Thursday' : 100,
    'Friday' : 5000,
    'Saturday' : 1500
}

Total_exp = weekly_expences['Sunday'] + weekly_expences['Monday'] + weekly_expences['Tuesday'] + weekly_expences['Wednesday'] + weekly_expences['Thursday'] + weekly_expences['Friday'] + weekly_expences['Saturday']
Avg_exp = Total_exp / 7
#print(f"{weekly_expences['Friday']}")
print(weekly_expences)
print(f"The total expences for a sunday is {weekly_expences['Sunday']}")
print(f"The total expenses for the week is {Total_exp}")
print(f"The Average expence for the week: {Avg_exp}")