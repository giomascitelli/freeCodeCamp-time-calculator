def days_later(days_added):
    # Function that handles the representation of 'next day' or 'n days later' in the result
    if days_added == 1:
        return '(next day)'
    elif days_added > 1:
        return f'({days_added} days later)'
    else:
        return ''

def add_time(start, duration, st_day=False):
    dotw = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Parsing the times and determining the new period (AM/PM) based on the start period)
    start_hours, start_mins = start.split(":")
    
    if "12" in start_hours and "AM" in start_mins:
        start_hours = '0'
        
    start_mins, start_period = start_mins.split(" ")

    added_hours, added_mins = map(int, duration.split(":"))
    
    start_hours, start_mins = int(start_hours), int(start_mins)
    
    new_period = start_period
    
    if "PM" in start_period:
        start_hours += 12

    # Calculating total minutes and hours
    total_mins = start_mins + added_mins + ((start_hours + added_hours) * 60)
    new_mins = round(total_mins % 60)
    mins_left = total_mins

    # Calculating number of days difference and remaining minutes/hours
    days_diff = int((total_mins / 1440))
    
    if total_mins >= 1440:
        mins_left = total_mins % 1440
    
    hours_left = int(mins_left / 60)

    # Determining AM/PM and updating hours left
    if mins_left <= 720:
        new_period = "AM"
    else:
        new_period = "PM"
        hours_left = hours_left - 12
    
    if hours_left == 0:
        hours_left = 12

    # Result string
    result = f'{hours_left}:{new_mins:02} {new_period}'

    # Handling the next day/DOTW if True
    if st_day:
        st_day = st_day.lower()
        selected_day = int(((dotw.index(st_day)) + days_diff) % 7)
        current_day = dotw[selected_day]
        result += f', {current_day.capitalize()} {days_later(days_diff)}'
    else:
        result = " ".join((result, days_later(days_diff)))
        
    return result.rstrip()

