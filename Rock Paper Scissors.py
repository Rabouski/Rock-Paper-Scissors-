import random
import turtle
mec = ["Paper","Rock","Scissors"]
t = turtle.Turtle()
screen = turtle.Screen()
skibidi = input("Hello there! Would you like to play Rock, Paper, or Sciccors? (Yes / No)")

def main():
    
    if skibidi == "yes":
            
        print("Very well then")
        print("!!!RULES!!!")
        print("You just have to win by how many points you want to add")
        print("")
        hawk = input("So how many Points should the winning cap be?")
        Score = int(hawk)
        oppScore = 0
        UserScore = 0

        while True:
            user = input("Rock Paper or Scissors?")

            
            while user not in  {"rock", "paper", "scissors","Rock", "Paper", "Scissors"}:
                user = input("I said, Rock Paper or Scissors! 😡")

            #Ai mechanic
            def diddyParty():
                babyOil = random.randint(0,2)
                return mec[babyOil]
            skibidicard = diddyParty()
            print("I will say... " + skibidicard)

        #Gameplay
            # Tie func
            if user.lower() == skibidicard.lower():
                    print("\nTie!!!")
                    print("\n Your Score: " + str(UserScore) + " My Score: " + str(oppScore))
                    screen.bgcolor("Yellow")
            

            elif (user == "Scissors" or user == "scissors") and skibidicard == "Paper":
                UserScore = UserScore + 1
                print("\nYou got a point")
                print("\n Your Score: " + str(UserScore) +" My Score: " + str(oppScore))
                screen.bgcolor("green")

            elif (user == "Rock" or user == "rock") and skibidicard == "Scissors":
                print("\nYou got a point")
                UserScore = UserScore + 1
                print("\n Your Score: " + str(UserScore) +" My Score: " + str(oppScore))
                screen.bgcolor("green")

            elif (user == "Paper" or user == "paper") and skibidicard == "Rock":
                UserScore = UserScore + 1
                print("\nYou got a point")
                print("\n Your Score: " + str(UserScore) +" My Score: " + str(oppScore))
                screen.bgcolor("green")

            
            
            
            else:
                print("\nHaha, you lost")
                oppScore += 1
                print("\n Your Score: " + str(UserScore) +" My Score: " + str(oppScore))
                screen.bgcolor("red")

            if oppScore >= Score:
                print("Wow, you lost to a computer")
                screen.bgcolor("red")
            if UserScore >= Score:
                print("YAY YOU WON 🥳🥳🥳🥳🥳🥳🥳🙌🙌🙌🙌🙌")
                screen.bgcolor("green")
    else:
        print("LOOOSER 👎👎👎👎")
        

            
            
main()