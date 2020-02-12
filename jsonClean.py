import os
import json

dir = "D:\Will\Documents\Projects\openDota\data\matches1\\"

for filename in os.listdir(dir):
    jsonFile = open(dir + filename, 'r', encoding="utf8")
    v = json.load(jsonFile)
    jsonFile.close()
    match = {}
    match['match_id'] = v['match_id']
    match['barracks_status_dire'] = v['barracks_status_dire']
    match['barracks_status_radiant'] = v['barracks_status_radiant']
    match['dire_score'] = v['dire_score']
    match['first_blood_time'] = v['first_blood_time']
    match['game_mode'] = v['game_mode']
    match['radiant_gold_adv'] = v['radiant_gold_adv']
    match['radiant_xp_adv'] = v['radiant_xp_adv']
    match['radiant_score'] = v['radiant_score']
    match['start_time'] = v['start_time']
    match['tower_status_dire'] = v['tower_status_dire']
    match['tower_status_radiant'] = v['tower_status_radiant']
    match['skill'] = v['skill']
    match['patch'] = v['players'][0]['patch']
    print(match['patch'])

'''
match
	id	
	raxDire	
	raxRadi	
	scoreDire	
	firstBlood	
	gameMode	
	advGold	
	advXp	
	scoreRadi	
	startTime	
	towerDire	
	towerRadi	
	skill	
	patch	
	throw	
	comeback	
	loss	
	win

objective
	type	
	time	
	slot	
	playerSlot	
	key	
	id

objectives
	matchId	
	objectiveId

teamfight
	id	
	teamfightPlayerId	
	start	
	end	
	deaths

teamfightPlayer
	id	
	deaths	
	buybacks	
	damage	
	healing	
	goldDelta	
	xpDelta	
	xpStart	
	xpEnd

teamfights
    matchId	
	teamfightId
'''