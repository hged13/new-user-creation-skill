from mycroft import MycroftSkill, intent_file_handler
import csv 
import pyaudio
import wave
import pandas as pd

class NewUserCreation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info(self.file_system.path)
        

    @intent_file_handler('creation.user.new.intent')
    def handle_creation_user_new(self, message):
        line = self.create_user() 
        with self.file_system.open('log.csv', "a") as my_file:
            writer = csv.writer(my_file)
            writer.writerow(line)
         
         
        self.speak_dialog('creation.user.new')
    
    def create_user(self):
        response = []
        name = self.get_response("What is your name")
        playlist = self.get_response("what is your go-to playlist")
        artist = self.get_response("Who is your favorite artist?")
        response.append(name)
        response.append(playlist)
        response.append(artist)
        self.speak_dialog("now we will take 5, 7 second samples of your voice")
        i = 0
        return response
     

def create_skill():
    return NewUserCreation()

