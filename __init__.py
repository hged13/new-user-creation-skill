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
            file = self.start_recording(name, i)
            recordings.append(file)
            i += 1

        user_info = [
            name, playlist, artist, recordings]
            
        return user_info
   
    def start_recording(self, name, num)
       filename = name + str(num) + ".wav"
        frames = 1024
        FORMAT = pyaudio.paInt16
        channels = 1
        sample_rate = 22050
        record_seconds = 7
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=frames)
        frames2 = []
        self.speak_dialog("Recording...")
            for i in range(int(44100 / frames * record_seconds)):
            data = stream.read(frames)

            frames2.append(data)
        self.speak_dialog("Finished recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames2))
        wf.close()
        return filename
        

       
        
    def test_function(self):
        test = 0
        return test


def create_skill():
    return NewUserCreation()

