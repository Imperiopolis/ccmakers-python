from sys import exit
from room import Room

class GoldRoom(Room):
    def __init__(self):
        self.entryMessage = "This room is full of gold.  How much do you take?"
    
    def performRoom(self, next):
        if "0" in next or "1" in next:
            how_much = int(next)
        else:
            return ["Man, learn to type a number.", None]
        
        if how_much < 50:
            print ["Nice, you're not greedy, you win!", None]
            exit(0)
        else:
            return ["You greedy bastard!", None]

class BearRoom(Room):
    def __init__(self):
        self.bearMoved = False
        
        self.entryMessage = """
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?"""
    
    def performRoom(self, next):
        if next == "take honey":
            return ["The bear looks at you then slaps your face off.", None]
        elif next == "taunt bear" and not self.bearMoved:
            self.bearMoved = True
            print "The bear has moved from the door. You can go through it now."
            return self.performRoom(raw_input("> "))
            # return ["The bear has moved from the door. You can go through it now.", self]
        elif next == "taunt bear" and self.bearMoved:
            return ["The bear gets pissed off and chews your leg off.", None]
        elif next == "open door":
            if (self.bearMoved):
                return ["", GoldRoom()]
            else:
                print "The bear stands in your way, %s." % self.playerName
                return self.performRoom(raw_input("> "))
        else:
            print "I got no idea what that means."
            return self.performRoom(raw_input("> "))

class CthuluRoom(Room):
    def __init__(self):
        self.entryMessage = """
Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?"""

    def performRoom(self, next):
        if "flee" in next:
            return ["", StartingRoom()]
        elif "head" in next:
            return ["Well that was tasty!", None]
        else:
            return ["", None]

class StartingRoom(Room):
    def __init__(self):
        self.entryMessage = """
You are in a dark room.
There is a door to your right and left.
Which one do you take?"""
        
    def performRoom(self, next):
        if next == "left":
            return ["", BearRoom()]
        elif next == "right":
            return ["", CthuluRoom()]
        else:
            return ["You stumble around the room until you starve.", None]

print "What is your name, adventurer?"
playerName = raw_input("> ")

StartingRoom().enterRoom(playerName)
