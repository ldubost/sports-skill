import json, requests, urllib, os
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import getLogger

baseurl = "https://wikiscores.cloud.xwiki.com/xwiki/bin/get/Sports"
sportsuri = "/Code/JSON?outputSyntax=plain"
alluri = "/Code/GamesJSON?outputSyntax=plain"
availableuri = "/Code/Features?outputSyntax=plain"

LOGGER = getLogger(__name__)

class Sports(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sports.intent')
    def handle_sports(self, message):
        LOGGER.info(message.data.get("sport", "tennis"))
        fullmsg = message.data.get("utterance")
        sport = message.data.get("sport", "tennis")
        player = message.data.get("player", "")
        if sport.find("volley")>=0:
            sport = "volleyball"
        if sport.find("soccer")>=0:
            sport = "football"
 
 
        type = "0" 
        if fullmsg.find("woman")>=0:
            type = "1"
        if fullmsg.find("women")>=0:
            type = "1"

        url = baseurl + sportsuri + "&sport=" + sport + "&player=" + urllib.parse.quote(player) + "&type=" + type
        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        data = resp.json()
        for key in data:
            LOGGER.info(key)
        sdata = json.dumps(data.get("text"))
        LOGGER.info(sdata)
        str = data.get("text")
        if (str==""):
            str = "I could not find any " + sport + " results for " + player;
            self.speak(str)
        elif data.get("lastResultsTexts"):
            for msg in data.get("lastResultsTexts"):
                self.speak(msg)
            for msg in data.get("nextGamesTexts"):
                self.speak(msg)
        else:
            self.speak(str)


    @intent_file_handler('latest.intent')
    def handle_latest(self, message):
        LOGGER.info(message.data.get("sport", "tennis"))
        fullmsg = message.data.get("utterance")
        sport = message.data.get("sport", "tennis")
        if sport.find("volley")>=0:
            sport = "volleyball"
        if sport.find("soccer")>=0:
            sport = "football"
 
        type = "0" 
        if fullmsg.find("woman")>=0:
            type = "1"
        if fullmsg.find("women")>=0:
            type = "1"

        url = baseurl + sportsuri + "&sport=" + sport + "&type=" + type;

        if fullmsg.find("latest")>=0:
            url = url + "&lastNb=3&nextNb=1"
        if fullmsg.find("next")>=0:
            url = url + "&nextNb=3&lastNb=0"

        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        data = resp.json()
        for key in data:
            LOGGER.info(key)
        sdata = json.dumps(data.get("text"))
        LOGGER.info(sdata)
        str = data.get("text")
        if (str==""):
            str = "I could not find any " + sport + " results for " + player;
            self.speak(str)
        elif data.get("texts"):
            for msg in data.get("texts"):
                self.speak(msg)
        elif data.get("lastResultsTexts"):
            for msg in data.get("lastResultsTexts"):
                self.speak(msg)
            for msg in data.get("nextGamesTexts"):
                self.speak(msg)
        else:
            self.speak(str)

    @intent_file_handler('latestall.intent')
    def handle_latest(self, message):
        fullmsg = message.data.get("utterance")

        url = baseurl + alluri;

        if fullmsg.find("latest")>=0:
            url = url + "&status=finished&nb=3"
        if fullmsg.find("next")>=0:
            url = url + "&status=future&nb=3"

        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        data = resp.json()
        for key in data:
            LOGGER.info(key)
        sdata = json.dumps(data.get("text"))
        LOGGER.info(sdata)
        str = data.get("text")
        if (str==""):
            str = "I could not find any " + sport + " results";
            self.speak(str)
        elif data.get("texts"):
            for msg in data.get("texts"):
                self.speak(msg)
        elif data.get("lastResultsTexts"):
            for msg in data.get("lastResultsTexts"):
                self.speak(msg)
            for msg in data.get("nextGamesTexts"):
                self.speak(msg)
        else:
            self.speak(str)

    @intent_file_handler('available.intent')
    def handle_available(self, message):
        fullmsg = message.data.get("utterance")
        url = baseurl + availableuri
        if fullmsg.find("competitions")>=0:
            url = url + "&type=competitions"
        else:
            url = url + "&type=sports"

        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        data = resp.json()
        str = data.get("text")
        self.speak(str)

def create_skill():
    return Sports()

