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
class Chips:
    def __init__(self,win):
        self.win=win
        self.x=0
        self.y=0
        self.drawn=False
        self.chip1=Circle(Point(500,500),10)
        self.chip2=Circle(Point(0,0),10)
        self.chip1.setFill('orange')
        self.chip1.setFill('cyan')
        
    def drawAt(self,dx1,dy1,dx2,dy2):
        self.chip1.move(dx1,dy1)
        self.chip2.move(dx2,dy2)
        if not self.drawn:
            self.drawn=True
            self.chip1.draw(self.win)
            self.chip2.draw(self.win)
            self.x+=dx1
            self.x+=dx2
            self.y+=dy1
            self.y+=dy2
    
    def getX1coord(self):
        return self.chip1.getCenter().getX()
    
    def getX2coord(self):
        return self.chip2.getCenter().getX() 
    
    def getY1coord(self):
        return self.chip1.getCenter().getY() 
    
    def getY2coord(self):
        return self.chip2.getCenter().getY()

class Board:
    def __init__(self,win,index):
        self.win=win
        self.x=0
        self.y=0
        self.drawn=False
        self.rectangle=Rectangle(Point(800,800))
        for c in index(range(1,80)):
            self.circle=Circle(Point(self.x,self.y),10)
        self.rectangle.setFill('blue')
        self.cirlce.setFill('red')
        



def main():
    welcome_page=Connect()
    
        



        
        
            
