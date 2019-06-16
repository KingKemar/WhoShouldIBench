import datetime

difficultySwitcher = {
        3: "Normal",
        4: "Heroic",
        5: "Mythic",
    }


def prepareboss(boss):
    for fight in boss:
        d =  datetime.timedelta(milliseconds=(fight.get('end_time')-fight.get('start_time')))
        s= "%s:%s" % (str(d)[2:4], str(d)[5:7])
        fight['length'] = s
        difficulty = fight.get('difficulty')
        fight['difficulty'] = difficultySwitcher.get(difficulty, 'Unknown Difficulty')
        percent = float(fight.get('bossPercentage'))/100
        if(percent > 0):
            fight['bossPercentage'] ="wipe : " +str(percent) + "%"
        else :
            fight['bossPercentage'] = "down"
        
    print (fight)
