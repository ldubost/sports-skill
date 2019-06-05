from mycroft import MycroftSkill, intent_file_handler


class Sports(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sports.intent')
    def handle_sports(self, message):
        self.speak_dialog('sports')


def create_skill():
    return Sports()

