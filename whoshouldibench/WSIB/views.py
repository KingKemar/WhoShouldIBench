from django.shortcuts import render
from whoshouldibench.settings import TEMPLATE_DIRS, WARCRAFTLOG_LINK, WARCRAFTLOG_PUBLICKEY
from WSIB.boss import prepareboss
from django.http import JsonResponse
import requests
import datetime
import json

HTMLFILE_INDEX = ''.join( TEMPLATE_DIRS ) + 'index.html'
HTMLFILE_FIGHTCHOICE = ''.join( TEMPLATE_DIRS ) + 'fight choice.html'
HTMLFILE_BOSSCHOICE = ''.join( TEMPLATE_DIRS ) + 'bosschoice.html'


def getFights(request):
    logcode = request.GET.get('logcode')
    fightsurl = WARCRAFTLOG_LINK+"/report/fights/"+logcode+"?api_key="+WARCRAFTLOG_PUBLICKEY
    response = requests.get(fightsurl)
    geodata = response.json()
    fightsjson = {}
    for fight in geodata['fights']:
        if fight.get('boss') is not 0:
            if fightsjson.get(fight.get('boss')):
                fightsjson.get(fight.get('boss')).append(fight)
            else:
                fightsjson[fight.get('boss')]= []
                fightsjson.get(fight.get('boss')).append(fight)
    fights =[]
    for key in fightsjson.keys():
        fights.append(fightsjson.get(key))
    return JsonResponse({'fights':fights})

def getFight(logcode, bossID):
    fights = getFights(logcode)
    return fights[bossID]

def index(request):
    return render(request,HTMLFILE_INDEX)

def reportView(request):
    reporturl = request.GET.get('loglink')
    reporturlArray = reporturl.split('/')
    logcode = reporturlArray[len(reporturlArray)-2]
    figths = getFights(logcode)
    return render(request,HTMLFILE_BOSSCHOICE, {'fights': figths, 'logcode': logcode })

def fightsView(request, logcode, bossId):
    boss = getFight(logcode, bossId)
    prepareboss(boss)
    return render(request,HTMLFILE_FIGHTCHOICE, {'boss': boss, 'logcode': logcode })
