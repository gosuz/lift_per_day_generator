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

one_rm = {
    "bp": 15,
    "sq": 50,
    "rdl": 55,
    "wpu": 10 # the weight is added weight
}

SETS = "3~5 sets"
# reps = # if its not a week divisible by 3, then set it to 5 reps,
# # if its divisible by 3 give set it as 3 reps

weeks = [1,2,3,4,5,6]
# loop through
# for x in week:
#     print(x)

def reps_for_week(weeks):
    for week in weeks:
        if (week%3 != 0):
            print("reps = 3")
            reps = 3
        else:
            print("reps = 5")
            reps = 5
    return reps

reps_for_week(weeks)

# variable of sets
# reps_wk_1_to_2
# reps_wk_3
# percentages (changes with week) - loop 3 times and include calucaltions:
    # loop 1 = 75%
    # loop 2 = 80%
    # loop 3 = 90%

# reps are the same for week

# Display all lifts w/ wk number, sets, reps, percentages, and each lift with percentage
