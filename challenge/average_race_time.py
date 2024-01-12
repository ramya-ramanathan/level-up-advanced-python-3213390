# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    lines = races.splitlines()
    filter_fn = lambda x: "Jennifer Rhines" in x
    jr_itr = filter(filter_fn, lines)
    jr = [x for x in jr_itr]
    jr = [x.replace(' ', '').split("JenniferRhines") for x in jr]
    times = [x[0] for x in jr]
    return times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    racetimes = [x.replace(':', ' ').replace('.', ' ').split() for x in racetimes]
    totalm = totals = totalM = 0
    for time in racetimes:
        totalm += int(time[0])
        totals += int(time[1])
        try:
            totalM += int(time[2])
        except:
            totalM += 0

    totalM += totalm * 60 * 1000
    totalM += totals * 1000

    avg = int(totalM / len(racetimes))
    avgm = int(avg / 60000)
    avg = avg % 60000
    avgs = int(avg / 1000)
    avg = avg % 1000
    avgM = int(avg / 100)

    return "{0}:{1}.{2}".format(avgm, avgs, avgM)

