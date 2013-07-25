class Room:
    def enterRoom(self, player):
        self.playerName = player
        print self.entryMessage

        next = raw_input("> ")
        
        message, nextRoom = self.performRoom(next)
        
        if (message):
            print message
        
        if (nextRoom):
            nextRoom.enterRoom(player)
        else:
            print "You died, %s. Great job!" % player
