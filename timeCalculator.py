def add_time(start, duration, week_start = ''):
    #defining initial variables
    start_l = list(start)
    duration_l = list(duration)
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    ##### Calculating Time Jump #####
    #extracting times in usable format
    AMPM = str(start_l.pop(-2)+start_l.pop(-1))
    #removing puntcuation
    del start_l[-1], start_l[-3]
    t_mins = int(start_l.pop(-2))*10 + int(start_l.pop(-1))
    t_hours = int(''.join(start_l))
    #converting to 24hr 
    if AMPM == 'PM':
        t_hours += 12
        day_change = True
    else: 
        day_change = False

    #extracting duration
    days = 0 #setting default value for days
    duration_mins = int(''.join(duration_l[-2:]))
    del duration_l[-3:]
    duration_hours = int(''.join(duration_l))

    #converting to larger units
    if duration_mins >=60:
        duration_hours += duration_mins//60
        duration_mins -= 60
    if duration_hours >= 24:
        days += duration_hours//24
        duration_hours = duration_hours%24
    
    #adding and then converting down again
    t_mins += duration_mins
    t_hours += duration_hours
    if t_mins >= 60:
        t_hours+=1
        t_mins-=60
    if t_hours >= 24:
        days += t_hours//60
        t_hours -= 24

    #setting AMPM
    if t_hours > 11:
        AMPM = 'PM'
        if t_hours !=12:
            t_hours-=12
    else:
        if t_hours == 0: 
            t_hours+=12
        AMPM = 'AM'

    if day_change and AMPM == 'AM':
        days += 1

    ##### Calculating weekday #####
    #making week_start input case insensitive
    weekday = week_start.lower()
    if weekday in days_of_week:
        shifted = days_of_week.index(weekday) + days
        if shifted > 6:
            shifted = shifted%7
        weekday = days_of_week[shifted]
        weekday = weekday.capitalize()
        
    ##### Formatting output string #####
    new_time = f'{t_hours}:{t_mins} {AMPM}'
    if t_mins < 10:
        new_time = f'{t_hours}:0{t_mins} {AMPM}'
        
    #adding weekday if required
    if len(week_start)>0:
        new_time += f', {weekday}'
    #if n days later then state
    if days > 1:
        new_time += f' ({days} days later)'
    elif days == 1:
        new_time += ' (next day)'

    #returning final time
    return new_time

if __name__ == '__main__':
    print(add_time('8:16 PM', '466:02', 'tuesday'))
