from mycroft import MycroftSkill, intent_file_handler


class NewUserCreation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creation.user.new.intent')
    def handle_creation_user_new(self, message):
        self.test_function()
        self.speak_dialog('creation.user.new')
        
    def test_function(self):
        test = 0
        return test


def create_skill():
    return NewUserCreation()

