






#Define the bae class player
class player:
    def play(self):
        print("the player is playing cricet.")

#Define the derived class Batsman
class Batsman(player):
    def play(self):
        print("the batsman is batting.")

 # Define the derived vlass bowler
class bowler(player):
      def play(self):
          print("The bowler is bowling.")

#creat objects of batsman and bowler classes
batsman = Batsman()
bowler = bowler()

# call the play() method for each object
batsman.play()
bowler.play()

