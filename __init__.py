from mycroft import MycroftSkill, intent_file_handler


class NewUserCreation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creation.user.new.intent')
    def handle_creation_user_new(self, message):
        name = self.create_user()
        self.speak_dialog('creation.user.new')
    
    def create_user(self):
        name = self.get_response("What is your name")
        return name
        
    def test_function(self):
        test = 0
        return test


def create_skill():
    return NewUserCreation()

