from mycroft import MycroftSkill, intent_file_handler
import csv 
import pyaudio
import wave
import pandas as pd

class NewUserCreation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creation.user.new.intent')
    def handle_creation_user_new(self, message):
        info = self.create_user()
        self.speak_dialog('creation.user.new')
    
    def create_user(self):
        name = self.get_response("What is your name")
        playlist = self.get_response("what is your go-to playlist")
        artist = self.get_response("Who is your favorite artist?")
        self.speak_dialog("now we will take 5, 7 second samples of your voice")
        i = 0
        recordings = []
       

        while i < 5:
            file = start_recording(name, i)
            recordings.append(file)
            i += 1

        user_info = [
            name, playlist, artist, recordings]
            
        return user_info
        

       
        
    def test_function(self):
        test = 0
        return test


def create_skill():
    return NewUserCreation()

