def convert_to_12hour (hour, minute, period): 
    # conditional statement to check the period 
    if period == "pm" and hour != 12: # if its pm and the hour is not 12,12 is added to the hour.
        hour += 12
    elif period == "am" and hour == 12: #  If it's "am" and the hour is 12, the hour is set to 0.
        hour = 0
    return "{:02}{:02}".format(hour, minute)  # using the format function to return the time in correct format. 

print(convert_to_12hour(6,12,"am"))
print(convert_to_12hour(7,16,"pm"))