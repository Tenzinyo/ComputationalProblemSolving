"""
Created on Sat Dec 24 18:34:28 2022
@author: tenzinuden
"""
from button import Button 
from graphics import GraphWin, Point, Text, Circle, Rectangle, Entry

class Connect:
    def __init__(self):
        self.win=GraphWin('Game', 1000,1000)
        self.win.setBackground('red')
        self.play = Button(Point(250,150), Point(350,180), "Play")
        self.play.setFill(" blue")
        self.play.setTextColor(" rose")
        
    def game(self):
        self.gameTitle.draw(self.win)
        self.creatorName.draw(self.win)
        self.lineDecor.draw(self.win)
        self.askName1.draw(self.win)
        self.askName2.draw(self.win)
        self.box1.draw(self.win)
        self.box2.draw(self.win)
        self.name1 = self.box1.getText()
        self.name2 = self.box2.getText()
        self.play.draw(self.win)
        
    def start(self):
        click=self.win.getMouse()
        if self.play.contains(click):
            self.win.close()
            return 0
        return self.start()



def main():
    welcome_page=Connect()
    
        



        
        
            
