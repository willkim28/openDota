import requests
import time
import json

url = 'https://api.opendota.com/api/'

gang = {
    'will': {
        'name': 'Will',
        'pid': '67798385'
    },

    'pat': {
        'name': 'Pat',
        'pid': '52147853'
    },

    'james': {
        'name': 'James',
        'pid': '84941438'
    },

    'tibi': {
        'name': 'Tibi',
        'pid': '72600614'
    }
}

'''
# Player matches
for pl in gang:
    pm = requests.get(url + 'players/' + gang[pl].get('pid') + '/matches')

    with open('data/%s.json' % pl, 'w') as f:
        f.write(pm.text)
    time.sleep(1)
'''

'''
# Player match info
for pl in gang:
    input_file = open('data/%s.json' % pl, 'r')
    json_array = json.load(input_file)
    match_list = []

    for item in json_array:
        matchId = {"match_id":None}
        matchId['match_id'] = item['match_id']
        match_list.append(matchId)

    with open('data/%sMatches.json' % pl, 'w') as f:
        json.dump(match_list, f)
'''

'''
# Filtered All Matches
for pl in gang:
    input_file = open('data/%sMatches.json' % pl, 'r')
    json_array = json.load(input_file)
    all_matches = []

    for match in json_array:
        matchId = {"match_id":None}
        matchId['match_id'] = match['match_id']
        all_matches.append(matchId)

with open('data/allMatches.json', 'w') as f:
    json.dump(all_matches, f)
'''

# Match GET
with open('data/allMatches.json', 'r') as f:
    json_array = json.load(f)

    for match in json_array:
        matchId = {"mid":None}
        matchId['mid'] = str(match['match_id'])
        am = requests.get(url + 'matches/' + matchId['mid'])
        with open('data/matches/%s.json' % matchId['mid'], 'w', encoding="utf8") as f:
            f.write(am.text)
        time.sleep(1)