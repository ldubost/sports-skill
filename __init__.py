import json, requests, urllib
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import getLogger

baseurl = "http://localhost:8080/xwiki/bin/get/Players/ViewResults/JSON?outputSyntax=plain"

LOGGER = getLogger(__name__)

class Sports(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sports.intent')
    def handle_sports(self, message):
        LOGGER.info(message.data.get("player", "nadal"))
        fullmsg = message.data.get("utterance")
        type = "0" 
        if fullmsg.find("woman")>=0:
            type = "1"
        if fullmsg.find("women")>=0:
            type = "1"
        url = baseurl + "&player=" + urllib.parse.quote(message.data.get("player" , "nadal")) + "&type=" + type
        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        data = resp.json()
        for key in data:
            LOGGER.info(key)
        sdata = json.dumps(data.get("text"))
        LOGGER.info(sdata)
        str = data.get("text")
        self.speak(str)


def create_skill():
    return Sports()

