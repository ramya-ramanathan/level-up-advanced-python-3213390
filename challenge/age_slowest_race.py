# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import datetime

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_data_cols(line):
    time = line[3:14]
    athlete = line[14:56]
    race_date = line[56:73]
    dob = line[73:87]
    location = line[87:]
    cols = [time, athlete, race_date, dob, location]
    cols = [x.strip() for x in cols]
    return cols

def calc_age(dob, curr_date):
    d1 = datetime.datetime.strptime(curr_date, '%d %b %Y').date()
    d2 = datetime.datetime.strptime(dob, '%d %b %Y').date()
    delta = d1-d2
    nyrs = int(delta.days / 365.25)
    ndays = int(delta.days % 365.25)
    return '{0}y{1}d'.format(nyrs, ndays)
    
def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    player = "Jennifer Rhines"
    if player in line:
        cols = get_data_cols(line)
        print(cols)
    else:
        raise Exception('player is not expected')
    age = calc_age(cols[3], cols[2])
    return((age,cols[0]))

def min_time(t1, t2):
    t1_m = int(t1.split(':')[0])
    t2_m = int(t2.split(':')[0])
    if t1_m < t2_m:
        return t1   
    if t2_m < t1_m:
        return t2
    t1_s = int(t1.split(':')[1].split('.')[0])
    t2_s = int(t2.split(':')[1].split('.')[0])
    if t1_s < t2_s:
        return t1
    if t2_s < t1_s:
        return t2
    
    raise Exception("comparsion by milliseconds not implemented")
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    lines = races.split('\n')
    curr_min = '1000:1000.1000'
    for line in lines:
        try:
            (age, time) = get_event_time(line)
            print(min_time(curr_min, time))
            if min_time(curr_min, time) == time:
                ans=(age,time)
        except:
            continue
    
    return(ans)
