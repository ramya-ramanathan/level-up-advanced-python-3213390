from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()


medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals_lines = [ x.split(';') for x in olympics.split('\n') ]
medals_header = medals_lines[0]
medals_map = []
for x in medals_lines[1:-1]:
    curr_tuple = list(zip(medals_header,x))
    curr_map = {header:val for header,val in curr_tuple}
    medals_map.append(curr_map)

medals = [medal(**m)for m in medals_map]

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    kw_tuples = kwargs.items()
    ret = []
    for medal in medals:
        medal_details = medal._asdict().items()
        kw_tuples_not_match = [x for x in kw_tuples if x not in medal_details]
        if(len(kw_tuples_not_match)==0):
            ret.append(medal)
    
    return ret

        
