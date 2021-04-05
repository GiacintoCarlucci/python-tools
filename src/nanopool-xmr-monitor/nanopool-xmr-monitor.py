import threading
import requests
import json
from os import system
from appModules import appConfig
from appModules import appStrings

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Miner
generalInfo = 'https://api.nanopool.org/v1/xmr/user'

def makeRequest(requestUrl,fields = []):
    for field in fields:
        requestUrl += '/'+ field
    response = requests.get(requestUrl)
    data = response.json()
    return data

def makeTable(data):
    headers = ''
    headerTab = ''
    values = ''
    valueTab = ''
    separator = '\t'
    for header in data:
        value = str(data[header])
        if len(header) < len(value):
            headerTab = ' '*(len(value)-len(header))
        headers += header + headerTab + separator
        headerTab = ''
        if len(value) < len(header):
            valueTab = ' '*(len(header)-len(value))
        values += value + valueTab + separator
        valueTab = ''
    return bcolors.OKCYAN + headers + bcolors.ENDC + '\n' + values

def listenGeneralInfo():
    # recall function every 5 mins
    threading.Timer(300.0, listenGeneralInfo).start()
    info = makeRequest(generalInfo,[appConfig.ADDRESS])

    system("clear")

    print(bcolors.HEADER + appStrings.banner + bcolors.ENDC)

    balance = info['data']['balance']
    unconfirmed = info['data']['unconfirmed_balance']
    hashrate = info['data']['avgHashrate']
    workers = info['data']['workers']

    print(bcolors.BOLD + appStrings.generalHeader + bcolors.ENDC)

    print(bcolors.OKBLUE + "Address:\t" + bcolors.ENDC + appConfig.ADDRESS[:10] + "..." + appConfig.ADDRESS[-8:])
    print(bcolors.OKGREEN + "Balance:\t" + bcolors.ENDC + balance)
    print(bcolors.WARNING + "Unconfirmed:\t" + bcolors.ENDC + unconfirmed)

    print(bcolors.BOLD + appStrings.hashratesHeader + bcolors.ENDC)

    print(makeTable(hashrate))

    print(bcolors.BOLD + appStrings.workersHeader + bcolors.ENDC)

    for worker in workers:
        print(bcolors.OKCYAN + '* ' + bcolors.ENDC + worker['id'] + '\t' +
              bcolors.OKCYAN + str(worker['rating']) + bcolors.ENDC)

listenGeneralInfo()
