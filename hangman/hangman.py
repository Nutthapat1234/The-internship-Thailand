class Hangman:
    def __init__(self):
        self.num_catagory =  5
        self.score = 0
        self.game_end = False
        self.highScore_text = ""
        self.highScore_point = 0
        self.level_pass = ""
        self.guess_time = 10
    def gameStart(self):
        self.loadHighScore()
        print("Welcome to the hangman game !!!")
        print("1.Animal catagory")
        print("2.Country catagory")
        print("3.Athlete catagory")
        print("4.Flower catagory")
        print("5.food catagory")
        print("6.High Score")
        print("7.Close game")
        catagory = input("Select Catagory:")
        while not (catagory.isnumeric() and int(catagory) <= self.num_catagory+2):
            print("Your selected categogry is invalid, Please select again")
            catagory = input("Select Catagory:")
        if catagory in self.level_pass:
            print("You are already pass this category.")
            self.gameStart()
        elif catagory == '1':
            self.openCategory("animal_catagory.txt", catagory)
        elif catagory == '2':
            self.openCategory("country_catagory.txt",catagory)
        elif catagory == '3':
            self.openCategory("athlete_catagory.txt",catagory)
        elif catagory == '4':
            self.openCategory("flower_catagory.txt",catagory)
        elif catagory == '5':
            self.openCategory("food_catagory.txt",catagory)
        elif catagory == '6':
            print("\n"+self.highScore_text)
            input("press any key to back to menu")
            self.gameStart()
        elif catagory == '7':
            print("Thank you for playing hangman game")

    def openCategory(self, filename, user_input):
        file = open(filename,"r")
        game_pass = False
        for line in file:
            line = line.split("|")
            print("Hint : " + line[1])
            self.gameProcess(line[0])
            if self.game_end:
                game_pass = True
                file.close()
                print("Back to menu")
                break
        if not game_pass:
            print("Suceess your pass this category!!!")
            print("Check point !")
            if self.score > self.highScore_point:
                self.writeHighScore("w", self.score)
            elif self.score == self.highScore_point:
                self.writeHighScore("a", self.score)
            self.level_pass += user_input
            self.loadHighScore()
        self.gameStart()

    def loadHighScore(self):
        file = open("HighScore.txt", "r")
        for line in file:
            self.highScore_text += line
            self.highScore_point = int(line.split("||")[0])
        file.close()

    def gameProcess(self,word):
        wrong_guess = ""
        alphabet_remain = [0]*len(word)
        game_end  = False
        while not game_end:
            for index in range(len(alphabet_remain)):
                if alphabet_remain[index] == 0 and word[index].isalpha():
                    print("_",end =" ")
                elif not word[index].isalpha():
                    alphabet_remain[index] = 1
                    print(word[index], end=" ")
                else:
                    print(word[index],end=" ")
            print("> score :" + str(self.score)+" remaining wrong guess :"+str(self.guess_time),end=" ")

            if wrong_guess != "":
                print("wrong guess: "+ wrong_guess)
            else:
                print()
            user_guess = input("> ")
            if len(user_guess) > 1:
                print("please enter only 1 alphabet per time")
                continue
            elif len(user_guess) == 0:
                print("please enter at least 1 alphabet")
                continue
            if user_guess in wrong_guess :
                print("You already try this alphabet")
            elif (user_guess.upper() in word or user_guess.lower()in word )and user_guess not in wrong_guess :
                self.checkWord(user_guess,word,alphabet_remain)
                self.score += 15
            else:
                self.guess_time -= 1
                if user_guess not in wrong_guess:
                    wrong_guess += user_guess+" "

            if self.isPass(alphabet_remain):
                game_end = True
                print("Correct !!! The word is " + word+ " Next word \n")

            if self.guess_time == 0:
                game_end = True
                self.game_end = True
                print("Game Over, Your score is "+str(self.score))
                if self.score > self.highScore_point:
                    print("Congratulation,New High Score!!!")
                    self.writeHighScore("w",self.score)
                elif self.score == self.highScore_point:
                    self.writeHighScore("a",self.score)
                self.loadHighScore()

    def writeHighScore(self,t,s):
        name = input("Enter your name : ")
        file = open("HighScore.txt",t)
        file.writelines(str(s) + " || "+name+"\n")
        file.close()

    def checkWord(self,alphabet,word,alist):
        for index in range(len(word)):
            if word[index].lower() == alphabet or word[index].upper() == alphabet:
                if alist[index]:
                    print("You already try this alphabet.")
                else:
                    alist[index] = 1

    def isPass(self,alist):
        for element in alist:
            if element == 0:
                return False
        return True

def gameStart():
    main_game =  Hangman()
    main_game.gameStart()





if __name__ == '__main__':
    gameStart()