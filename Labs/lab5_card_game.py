# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
# from queue import Queue
from queue import LifoQueue

# to use the shuffle for shuffling the cards
from random import shuffle

class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add card from shuffled deck
        new_card = self.the_cards.get()

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file='cards/' + new_card + '.gif')
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        self.closed_deck = Button(cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        self.closed_deck.config(image=closed_card)
        self.closed_deck.grid(row=0, column=1, padx=2, pady=2)
        self.closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.done_playing)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        # add card to score
        self.update_score(new_card)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        cards = LifoQueue(maxsize=52) #change this if you want to use a different data structure
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        card_list = []

        # add cards to card_list
        for suit in suits:
            for num in range(1,11):
                card_list.append(str(num) + "_" + suit)
            for p in people:
                card_list.append(p + "_" + suit)

        shuffle(card_list)

        # add to LIFO queue
        for card in card_list:
            cards.put(card)

        print(card_list)

        return cards

    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        new_card = self.the_cards.get()

        the_card = PhotoImage(file='cards/' + new_card + '.gif')
        self.open_card.config(image=the_card)
        self.open_card.photo = the_card
        self.open_card.update_idletasks()

        self.update_score(new_card)

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):
        print("it works!")
        if self.player_score == 21:
            self.score_label.config(text="Your score: " + str(self.player_score) + " You hit the jackpot!")
            self.score_label.update_idletasks()
        elif self.player_score > 21:
            self.score_label.config(text="Your score: " + str(self.player_score) + " Game over!")
            self.score_label.update_idletasks()

        if self.player_score >= 21:
            self.closed_deck.config(state=DISABLED)
        else:
            self.closed_deck.config(state=NORMAL)

    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        # check card score
        # if card is a jack, queen, or king, add 10
        if card[0] == 'j' or card[0] == 'q' or card[0] == 'k':
            score = 10
        else:
            score = int(card[0])

        self.player_score = self.player_score + score

        # update score if not on the first card
        if self.the_cards.qsize() < 51:
            self.score_label.config(text="Your score: " + str(self.player_score))
            self.score_label.update_idletasks()

        self.check_scores()

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        self.closed_deck.config(state=DISABLED)
        self.score_label.config(text="Your score: " + str(self.player_score) + " Well done! Keep playing?")
        self.score_label.update_idletasks()

    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.pick_card()

        # change score
        self.score_label.config(text="Your score: " + str(self.player_score))
        self.score_label.update_idletasks()

# object creation here:
app = CardGame()
