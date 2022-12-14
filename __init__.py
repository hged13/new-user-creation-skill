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
        playlist = self.get_response("What is your first radio preference?")
        artist = self.get_response("Who is your favorite artist?")
        artist2 = self.get_response("What is a third radio preference?")
        response.append(name)
        response.append(playlist)
        response.append(artist)
        response.append(artist2)
        self.speak_dialog("now we will take 5, 7 second samples of your voice")
        i = 0
        recordings = []
        with self.file_system.open('wav.csv', "a") as my_file2:
            writer2 = csv.writer(my_file2)
            while i < 5:
                rec = self.start_recording(name, i)
                writer2.writerow([rec,name])
                i += 1
        return response

    def start_recording(self,name, num):
        dir = self.file_system.path
        namelite = name + str(num) + ".wav"
        filename = dir + "/" + namelite
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
     
def create_skill():
    return NewUserCreation()
