from mycroft import MycroftSkill, intent_file_handler


class Codesys(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('codesys.intent')
    def handle_codesys(self, message):
        self.speak_dialog('codesys')


def create_skill():
    return Codesys()

