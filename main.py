import random


class HangmanDiagram:
    diagram = {1:
               f"""
                ______________
               | ____________ |
               ||           | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 2:
                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 3:
                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
               |            | |
               |            | |
               |            | |
               |            | |
               |            | |
                            | |
                            | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 4:

                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
               |            | |
             \ |            | |
              \|            | |
               |            | |
               |            | |
                            | |
                            | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 5:
                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
               |            | |
             \ | /          | |
              \|/           | |
               |            | |
               |            | |
                            | |
                            | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 6:
                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
               |            | |
             \ | /          | |
              \|/           | |
               |            | |
               |            | |
              /             | |
             /              | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """, 7:
                   """
                ______________
               | ____________ |
               ||           | |
            ██████          | |
           ██    ██         | |
           ██    ██         | |
           ██    ██         | |
            ██████          | |
               |            | |
             \ | /          | |
              \|/           | |
               |            | |
               |            | |
              / \           | |
             /   \          | |
                            | |
                            | |
        ------------------------------
        /\/\/\/\/\/\/\//\/\/\/\/\/\/\\
        ------------------------------
        """
               }

    def __repr__(self) -> str:
        return self.__class__.__name__


class RandomWordGenerator:
    """
    An object that chooses a word at random from a pre-defined list

    Example:
    setup = RandomWordGenerator()
    word = setup.get()
    """

    def __init__(self) -> None:
        self.word = random.choice(["Apple", "Orange"])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.word})"

    def __str__(self) -> str:
        return f"{self.word}"

    def get(self) -> str:
        """Method that returns the chosen word in a str format"""

        return self.word


class ConvertWord:
    """This converts a given word into a dict {index: letter}"""

    def __init__(self) -> None:
        self.word_dict = {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.word_dict})"

    def __str__(self) -> str:
        return f"{self.word_dict}"

    def convert_to_dict(self, unformatted_word) -> dict:
        """
        Iterate through the word and place them into a dict {index: letter}

        example:
        word = "Apple"

        returns {0: "A", 1: "p", 2: "p", 3: "l", 4: "e"}
        """
        for index, letter in enumerate(unformatted_word):
            self.word_dict[index] = letter.lower()
        return self.word_dict


class HangmanUnderscoreDiagram:

    def __init__(self, word: str) -> None:
        self.word = word

    def __repr__(self) -> str:
        return __class__.__name__

    def __str__(self) -> str:
        return " _ " * len(self.word)

    def create_hidden_word(self) -> list:
        return " _ ".split() * len(self.word)


class Game:

    failed_guesses = 0

    has_won = False
    formatted_word = None
    underscore_word = None

    def __init__(self) -> None:
        self.setup()

    def setup(self):
        """This method allows the class to refresh the variables so
        if the user wants to carry on with the game they can with a new word"""
        setup = RandomWordGenerator().get()
        self.formatted_word = ConvertWord().convert_to_dict(setup)
        self.underscore_word = HangmanUnderscoreDiagram(
            setup).create_hidden_word()
        self.failed_guesses = 0
        print("Hello")
        self.has_won = False
        self.start_game(True)
   

    def start_game(self, continue_playing: bool):
        while continue_playing:
            if self.failed_guesses == 7:
                player_choice_play = input(
                    "Do you want to continue playing? (Y/N) ")
                if player_choice_play == "Y":
                    continue_playing = True
                    self.setup()
                else:
                    continue_playing = False
                    break
          
            if self.has_won:
                player_choice_play = input(
                    "Do you want to continue playing? (Y/N) ")
                if player_choice_play == "Y":
                    continue_playing = True
                    self.setup()
                else:
                    continue_playing = False
                    break
                    
            user_guess = input("Please choose a letter: ")
            print("Please enter a valid letter")
            self.guess(user_guess.lower())

    def guess(self, letter):

        if letter in self.formatted_word.values():
            for index, dict_letter in self.formatted_word.items():
                if letter == dict_letter:
                    self.__reveal_letter(letter, index, self.underscore_word)
                    self.__check_win_status(self.underscore_word)
        else:
    
            self.failed_guesses += 1
            hangman = HangmanDiagram()
            print(hangman.diagram[self.failed_guesses])
            print(f"{letter} not in {''.join(self.underscore_word)}\n")
            

    @staticmethod
    def __reveal_letter(letter, index, underscore_word):
        underscore_word.pop(index)
        underscore_word.insert(index, letter)
        print(f"{letter} in {''.join(underscore_word)}")

    def __check_win_status(self, underscore_word):
        if "_" not in underscore_word:
            self.failed_guesses = 0
            self.has_won = True
            print("You win!")


# TODO: Add error message if longer than len(letter) > 1 or is int
# TODO: Add error message if user tries to type something other than Y or N
game = Game()
