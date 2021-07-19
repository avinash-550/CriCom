# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:52:52 2021

@author: AVINASH
"""
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal
import sys
from ui import *
from fetch import *
import threading
from time import sleep
import pyttsx3
from random import choice
import pygame
    
STOP_THREADS = False


def audio(res, excite = 0, t=0):
    """Coverts text commentary to audio"""
    
    # set up tts engine
    engine = pyttsx3.init()
    engine.setProperty('rate', choice([i for i in range(125,135,1)]) + 30*excite)
    engine.setProperty('volume', choice([0.4,0.5]) + 0.4*excite)
    if 'ballinfo' in res:
        engine.say(res['ballinfo'])
    engine.runAndWait()

    
    # play the crowd noise
    noise = {0:"\casual.mp3", 1: "\excited.mp3"}
    crowd = 'S:\personal projects\cricket bot\sounds' + noise[excite] 
    pygame.init()
    sound = pygame.mixer.Sound(crowd)
    pygame.mixer.Sound.play(sound)
    sleep(1)
    
    if 'commentary' in res:
        engine.say(res['commentary'])
    if t:
        engine.say("Score after "+ res['over']+ " overs.")
        engine.say(res['Ascore'])
        engine.say(res['Bscore'])
    engine.runAndWait()
    
    
def calexcite(s):
    # calculates if excitement is one or not
    if "OUT" in s or "FOUR" in s or "SIX" in s:
        return 1
    return 0

class MyForm(QDialog):
    # signals to change ui through emitters
    updatestatus = pyqtSignal(str)
    updateA = pyqtSignal(str)
    updateB = pyqtSignal(str)
    updateCommentary = pyqtSignal(str)
    updateScoreA = pyqtSignal(str)
    updateScoreB = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.ui  = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_action)
        self.updatestatus.connect(self.ui.status.setText)
        self.updateA.connect(self.ui.teama.setText)
        self.updateB.connect(self.ui.teamb.setText)
        self.updateScoreA.connect(self.ui.scorea.setText)
        self.updateScoreB.connect(self.ui.scoreb.setText)
        self.updateCommentary.connect(self.ui.commentary.setText)
        self.show()
        
    def start_action(self):
        m = self.ui.matchinput.toPlainText()
        # using threads to avoid freezing ui
        self.thread = threading.Thread(target = self.perpetual)
        self.thread.daemon = True
        self.thread.setDaemon(True)
        self.thread.start()
         
        
        
    def set_value(self, A, B, scoreA, scoreB, status, commentary):
        self.ui.status.setText("Status: "+ status)
        self.ui.teamb.setText(B)
        self.ui.teama.setText(A)
        self.ui.commentary.setText('"' + commentary + '"')
        self.ui.scorea.setText(scoreA)
        self.ui.scoreb.setText(scoreB)
        
    def perpetual(self):
        self.updatestatus.emit("Please wait...") 
        # fetch score
        c = Commenter(self.ui.matchinput.toPlainText())
        if c.check_availability():
            self.updatestatus.emit("Starting...")
        else:
            self.updatestatus.emit("Match not live.")
            return 
            
        t = 0  
        score_comment = 0
        prev_o = "0.01"
        prev_c = "x"
        while True:
            res = c.scrap()
            if prev_o!= res['over'] and prev_c!=res['commentary']:
                
                try:
                    self.updateA.emit(res['A'])
                    self.updateB.emit(res['B'])
                    self.updateScoreA.emit(res['Ascore'])  
                    self.updateScoreB.emit(res['Bscore'])
                    self.updatestatus.emit("Overs: "+ res['over'] + "\n-----------\nStatus: "+ res['status'])
                    if 'commentary' in res:
                        self.updateCommentary.emit('Commentary: \n'+ res['ballinfo']+"\n"+ "\n" +'"' +res['commentary']+ ' "')
                    prev_o = res['over']
                    prev_c = res['commentary']
                    if(t==3):
                        score_comment = 1
                    audio(res, calexcite(res['ballinfo']),score_comment )
                except:
                    break
                
            sleep(10)
            if t == 3:
                t = 0
            t += 1
            score_comment = 0
            
            global STOP_THREADS
            if STOP_THREADS:
                c.end()
                break
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    t = app.exec_()
    STOP_THREADS= True # killing threads before quitting
    sys.exit(t)
    
        
    