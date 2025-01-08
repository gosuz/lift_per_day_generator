# Task: Generate a training program that tells me the reps, sets for the lift and day

# Set 1RM
# Get numbers for each lift (based off 1RM)
# hard code the 1RM for now.
# Output all numbers and lifts.
    # Then reorganize to show which lift for which day
    # Loop twice and have one off day (Sunday)
    # Lists or dictionaries?? probably dictionary is better choice

# dictionary of lift and 1RM
    # lift_info {
        # BP: ____kg
        # SQ: ____kg
        # RDL: ____kg
        # WPU: ____kg (added weight)
    # }

one_rms = {
    "bp": 15,
    "sq": 50,
    "rdl": 55,
    "wpu": 10 # the weight is added weight
}

SETS = "3~5 sets"

weeks = {'1': 75, '2': 80, '3': 90}

def reps_for_week(week):
    int_week = int(week)
    if (int_week%3 != 0):
        # print("reps = 3")
        reps = 5
    else:
        # print("reps = 5")
        reps = 3
    return reps

print("-------------------------------------------------------------")

# The input should be an integer e.g. 75, 100, 85 etc.
def lifts_weight_calculator(week_percentage):
    # Should convert whole number to percentge
    # print(f"This is the week percentage: {week_percentage}")
    weights_for_week = {}
    # print(f"This is weights_for_week: {weights_for_week}")
    for lift in one_rms:
        # value = f"{lift.upper()}: {one_rms[lift]}"
        # print(f"This is the value: {value}")
        # create a key value pair
        # print(lift)
        # print(f"This is the lift: {lift}")
        # print(f"This is the one_rms: {one_rms[lift]}")
        # print(f"This is the one_rms: {one_rms[lift]} week_percentage/100: {(week_percentage)/100}")
        weight_for_lift = one_rms[lift] * (week_percentage/100)
        weights_for_week[lift.upper()] = weight_for_lift

    # Display the values using a loop. And use the dictionary to directly display it
    for lift, weight in weights_for_week.items():
            print(f"{lift}: {weight}")
        # display_lift = f"{lift.upper()} : {weights_for_week[lift.upper()]}"
    return weights_for_week
            # print(f"{lift.upper()}: {weights_for_week}")


    # 15 (only returns 15)

            # numbers have to be adjusted based on the percentage
            # make the numbers into percentages (create a function for this)
            # num_percentage = one_rm100    # 50/100 = 0.5


    # percentage is the week's percentage
    # 1rm * (percentage_num/100)
    # weights_for_week = 50kg * (75/100)
    # BP: 50 => BP: 0.5
    #

for week_num in weeks:
    int_week_num = int(week_num)
    print(f"week {int_week_num}") # week 1
    print(f"3~5 sets x {reps_for_week(int_week_num)}reps")
    # print(f"This is weeks[week_num]{weeks[week_num]}%") #gives back the string of 1
    print(lifts_weight_calculator(weeks[week_num]))
    print("----------------------------------------------")
