import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self, tip):
        self.tip_list = tip.split(",")   #separates commas in the hint entered by the user list like that:[1,2,"w"] or [1,2,1]
        for i in range(len(self.tip_list)): 
            if i != len(self.tip_list)-1:
                if self.tip_list[-1] in "wb":   #if the last element in the list is a letter
                    self.hand[int(self.tip_list[int(i)])-1][0] = self.tip_list[-1]  #the hand that the bot knows is updated
                elif self.tip_list[-1] in ["1","2","3","4"]:  #if the last element in the list is a number
                    self.hand[int(self.tip_list[int(i)])-1][1] = int(self.tip_list[-1])  #the hand that the bot knows is updated                       
        # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # output: none
        # The tip is processed and the information about the bot's hand is updated.

    def update_count_deck(self,card):
        self.i = 0    #Since there is more than one same card in the deck, I set up self.i to remove it for 1 time.
        for item in self.count_deck:  #if the card is in the deck 
            if item == card: 
                self.count_deck.pop(self.count_deck.index(item)) #remove the card from the deck in the boat
                self.i = self.i + 1
            if self.i == 1:
                break         
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.

    def update_hand(self,num):
        self.card = self.hand[num-1]              #The card in that index is
        self.hand.remove(self.card)               #removed from the boat's hand.
        if len(self.count_deck) > len(self.hand): #if there are enough cards in the deck
            self.hand.append(["!",-1])           #new card is added and bot understand that it has 2 or 3 card from deck.
        #My BONUS algorithm is:
        #In this algorithm, if there is 1 letter or number in the deck that the bot knows,
        # and the bot has the same number or letter known to the bot,
        #this is the bot card directly and the bot knows the card and updates its own hand.
        #for example bot's count deck has [w,1] and there is only one card only one number(1) or letter(w)
        #and bot has informations about its cards from tips for example bot's know that there is one card has
        #number of 1 or w and bot understand that it is its own card and update it.
        w_count = 0 #count of w in the deck.
        b_count = 0 #count of b in the deck.
        first_count = 0 #count of 1 in the deck.
        second_count = 0 #count of 2 in the deck.
        third_count = 0 #count of 3 in the deck.
        fourth_count = 0 #count of 4 in the deck.
        for i in deck:
            for j in i:
                if j == "w":
                    w_count += 1
                elif j == "b":
                    b_count += 1
                elif j == 1:
                    first_count += 1
                elif j == 2:
                    second_count += 1
                elif j == 3:
                    third_count += 1
                elif j == 4:
                    fourth_count += 1
        w_count2 = 0 #count of w in the hand.
        b_count2 = 0 #count of b in the hand.
        first_count2 = 0 #count of 1 in the hand.
        second_count2 = 0 #count of 2 in the hand.
        third_count2 = 0 #count of 3 in the hand.
        fourth_count2 = 0 #count of 4 in the hand.
        if w_count == 1:
            for i in self.hand:
                if "w" in i:
                    w_count2 += 1 #calculate count of w in the hand.
            if w_count2 == 1:
                for i in self.hand: 
                    if "w" in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if "w" in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
        if b_count == 1:
            for i in self.hand:
                if "b" in i:
                    b_count2 += 1 #calculate count of b in the hand.
            if b_count2 == 1:
                for i in self.hand:
                    if "b" in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if "b" in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
        if first_count == 1:
            for i in self.hand:
                if 1 in i:
                    first_count2 += 1 #calculate count of 1 in the hand.
            if first_count2 == 1:
                for i in self.hand:
                    if 1 in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if 1 in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
        if second_count == 1:          
            for i in self.hand:
                if 2 in i:
                    second_count2 += 1 #calculate count of 2 in the hand.
            if second_count2 == 1:
                for i in self.hand:
                    if 2 in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if 2 in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
        if third_count == 1:
            for i in self.hand:
                if 3 in i:
                    third_count2 += 1 #calculate count of 3 in the hand.
            if third_count2 == 1:
                for i in self.hand:
                    if 3 in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if 3 in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
        if fourth_count == 1:
            for i in self.hand:
                if 4 in i:
                    fourth_count2 += 1 #calculate count of 4 in the hand.
            if fourth_count2 == 1:
                for i in self.hand:
                    if 4 in i:
                        for j in self.count_deck: #change the hand with the card of deck.
                            if 4 in j:
                                self.hand[self.hand.index(i)] = self.count_deck[self.count_deck.index(j)]
                  
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.
    
    def give_tip(self):
        self.tip = ""  #the string the bot will give.
        self.count_w = 0 #how much w is on hand.
        self.count_b = 0 #how much b is on hand.
        self.count_1 = 0 #how much 1 is on hand.
        self.count_2 = 0 #how much 2 is on hand.   
        self.count_3 = 0 #how much 3 is on hand.   
        self.count_4 = 0 #how much 4 is on hand.   
        self.max_count = 0 #ı use that for find max count.
        self.count_w_indexlist = ["w"] #Keep locations with w in the list
        self.count_b_indexlist = ["b"] #Keep locations with b in the list
        self.count_1_indexlist = [1]   #Keep locations with 1 in the list
        self.count_2_indexlist = [2]   #Keep locations with 2 in the list
        self.count_3_indexlist = [3]   #Keep locations with 3 in the list
        self.count_4_indexlist = [4]   #Keep locations with 4 in the list 
        for i in range(len(self.play_hand)): #I looked every locations in player hand.
            for j in play_hand[i]:
                if j == "w":
                    self.count_w += 1                  #If location is "w" I increased 1 the count_w.
                    self.count_w_indexlist.append(i)   #I added "w"'s location into list.
                    if self.count_w > self.max_count : #find the largest number or letter
                        self.max_count = self.count_w
                elif j == "b":
                    self.count_b += 1                 #If location is "b" I increased 1 the count_w.
                    self.count_b_indexlist.append(i)  #I added "b"'s location into list.
                    if self.count_b > self.max_count: #find the largest number or letter
                        self.max_count = self.count_b  
                elif j == 1:
                    self.count_1 += 1                 #If location is "1" I increased 1 the count_w.
                    self.count_1_indexlist.append(i)  #I added "1"'s location into list.
                    if self.count_1 > self.max_count: #find the largest number or letter
                        self.max_count = self.count_1
                elif j == 2:
                    self.count_2 += 1                 #If location is "2" I increased 1 the count_w.
                    self.count_2_indexlist.append(i)  #I added "2"'s location into list.
                    if self.count_2 > self.max_count: #find the largest number or letter
                        self.max_count = self.count_2
                elif j == 3:
                    self.count_3 += 1                 #If location is "3" I increased 1 the count_w.
                    self.count_3_indexlist.append(i)  #I added "3"'s location into list.
                    if self.count_3 > self.max_count: #find the largest number or letter
                        self.max_count = self.count_3
                elif j == 4:
                    self.count_4 += 1                 #If location is "4" I increased 1 the count_w.
                    self.count_4_indexlist.append(i)  #I added "4"'s location into list.
                    if self.count_4 > self.max_count: #find the largest number or letter
                        self.max_count = self.count_4      
        self.totallist = [self.count_w_indexlist,self.count_b_indexlist,self.count_1_indexlist,
        self.count_2_indexlist,self.count_3_indexlist,self.count_4_indexlist] #all index lists have been added to 1 list.
        for i in self.totallist: 
            if len(i)-1 == self.max_count: #which list's length is equal to max count. It should be -1 because ı created my lists with their characteristic letter or number.
                for index in i[1:len(i)]: #first index has original letter or number so the index taken after that. 
                    self.tip += str(index+1) + "," #Create a tip.
                self.tip += str(i[0]) #gives the first index of tip.
                return self.tip
         # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.
    def pick_stack(self):
        if len(self.stack[0]) == 0: #if the first list of the stack is empty
            for i in self.hand: 
                if i[1] == 1:       #if the number on the card is one
                    if i[0] == "b": #should be b on the first list
                        return self.hand.index(i)+1 #card location
                    
        if len(self.stack[1]) == 0: #if the second list of the stack is empty
            for i in self.hand:
                if i[1] == 1:       #if the number on the card is one
                    if i[0] == "w": #should be w on the second list
                        return self.hand.index(i)+1 #card location
        self.i = 0
        while self.i != len(self.hand):
            if len(self.stack[0]) > 0:  #If there is a card in the first list in the stack
                if self.hand[self.i][0] == "b" and  self.stack[0][-1][1] + 1 == self.hand[self.i][1]: #the letter of this card is b and one more than the number of the card in the stack
                    return self.i + 1   #card location
            if len(self.stack[1]) > 0:  #If there is a card in the second list in the stack
                if self.hand[self.i][0] == "w" and  self.stack[1][-1][1] + 1 == self.hand[self.i][1]: #the letter of this card is w and one more than the number of the card in the stack
                    return self.i + 1   #card location
            self.i = self.i + 1
            if self.i == len(self.hand):
                return -1 #if there is no suitable card to put on the stack return -1                                     
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        

    def pick_discard(self):
        self.i = 0
        while self.i < len(self.hand):
            if self.hand[self.i] in self.stack[0] or self.hand[self.i] in self.stack[1]: #if there is that card in the stack
                return self.i+1 #that card should be thrown away
            self.i = self.i + 1
            if self.i == len(self.hand): #if the boat has no cards in the stack
                self.k = 0
                while True:
                    if self.hand[self.k][0] == "!" and self.hand[self.k][1] == -1: #if we don't know anything about one of the cards 
                        return self.k + 1 #card location
                    self.k = self.k + 1
                    if self.k == len(self.hand):  #if the bot has at least one information about all cards
                        for i in self.hand:
                            if i[0] in ["w","b"] and i[1] == -1: #Throws the card with unknown value into the trash
                                return self.hand.index(i) + 1   #card location
                            elif i[0] == "!" and i[1] in [1,2,3,4]: #Throws the card with unknown value into the trash
                                return self.hand.index(i) + 1   #card location           
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.
      

def shuffle(deck):
    number_list = []        #list of numbers for the indexes of the cards in the deck
    shuffled_deck_list = [] #shuffled deck
    for i in range(len(deck)): 
        number_list.append(i) #add indexes to the list of numbers
    shuffled_number_list = random.sample(number_list,len(number_list)) #Mixing the list of numbers with indexes attached
    for i in shuffled_number_list:
        shuffled_deck_list.append(deck[i]) #add to shuffled deck
    deck[0:] = shuffled_deck_list #build the new deck      
    # input: deck to be shuffled
    # output: none
    # shuffle the deck
    # you are free to choose the algorithm you want
    # explain your shuffle algorithm in a comment


def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

def update_hand(hand,deck,num):
    card = hand[num-1]      #card to be removed
    hand.pop(num-1)         #removed
    if len(deck) > 0:       #if there is a card in the deck
        hand = hand.append(deck[0]) #a new card is added to the hand
        deck = deck.pop(0)  #that card is removed from the deck
    return card    
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.


def try_stack(card,stack,trash,lives):
    if card[0] == "b":         #if the letter in the first index of the card is b, the first stack is checked
        if len(stack[0]) == 0: #If the first stack is empty,
            if card[1] == 1:   #it is checked that the element in the second index of the card is 1.
                stack[0].append(card) #and add and update it on the stack
            else:
                trash.append(card) #adds to the trash if the second value of the card is not 1
                trash.sort()       #sort the trash
                lives = lives - 1  #update lives 
                print("You lost 1 lives.") 
        else:                      #if there is a card in the stack
            if card[1] == stack[0][-1][1] + 1: #If the number on the card is 1 more than the number on the stack 
                stack[0].append(card) # it is added to the stack.
            else:                     #if the number on the card is not more than 1 than the card on the stack
                trash.append(card)    #adds to the trash 
                trash.sort()          #sort the trash
                lives = lives - 1     #update lives
                print("You lost 1 lives.")        
    elif card[0] == "w":    #if the letter in the first index of the card is w, the second stack is checked
        if len(stack[1]) == 0:        #If the second stack is empty,
            if card[1] == 1:          #it is checked that the element in the second index of the card is 1.
                stack[1].append(card) #and add and update it on the stack
            else:
                trash.append(card)    #adds to the trash if the second value of the card is not 1
                trash.sort()          #sort the trash
                lives = lives - 1     #update lives
                print("You lost 1 lives.")     
        else:
            if card[1] == stack[1][-1][1] + 1: #If the number on the card is 1 more than the number on the stack 
                stack[1].append(card)          #it is added to the stack.
            else:                     #if the number on the card is not more than 1 than the card on the stack
                trash.append(card)    #adds to the trash 
                trash.sort()          #sort the trash
                lives = lives - 1     #update lives
                print("You lost 1 lives.") 
    print(f"You have {lives} lives")                       
    return lives                        
    # input: the card to be stacked, current stack, current trash, number of lives
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.

def discard(card,trash,tips):
    trash.append(card) #add the card into trash.
    trash.sort()       #sort trash
    tips = tips + 1    #update number of tips
    print(f"The trash:{trash}")
    print(f"You have {tips} tips")
    return tips
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck) 
# First hands are dealt.
print("Randomly three cards are dealt to each player.")
comp_hand = deck[0:3] #  obtain cards (3 cards) from deck
play_hand = deck[3:6] #  obtain cards (3 cards) from deck
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand[0], comp_hand[1], comp_hand[2])
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                tips = tips - 1 #update tips
                tip = input("Enter the tip:(form of loc1,loc2*,loc3*,tip)") #users tip
                bot.get_tip(tip) #bot takes tip
                turn = 1 
                       # Switch turns.
                # Take a tip from the player, give it to the bot, update and print the number of tips.
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            if len(play_hand) > 0:
                turn = 1        # Switch turns.
                stack_num = int(input("Enter the location which do you want to stack:")) #the position of the card the user wants to stack
                removed_card = update_hand(play_hand,deck,stack_num) #removed card
                lives = try_stack(removed_card,stack,trash,lives)    #update lives,stack or trash.
                bot.update_count_deck(play_hand[-1]) #play hand will be update so bot will update its count deck.
            else:
                print("Not possible! you have not any card.")   
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
        elif inp == "d":
            if len(play_hand) > 0:
                turn = 1 # Switch turns.
                discard_num = int(input("Enter the location which do you want to discard:")) #the position of the card the user wants to discard
                removed_card = update_hand(play_hand,deck,discard_num) #removed card
                tips = discard(removed_card,trash,tips)                #update tips, trash.
                bot.update_count_deck(play_hand[-1]) #play hand will be update so bot will update its count deck.
            else:
                print("Not possible! you have not any card.")
                # Take the location of the card to be discarded from the player,
                # update hands and bot's count_deck and discard the selected card.
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        if tips > 1  and len(play_hand)>0:
            tips = tips - 1 #update tips
            print(f"Computer gives a tip:\n{bot.give_tip()}")
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.
        else:
            if len(deck) == 0:
                if len(comp_hand) == 0:
                   turn = 0
                   continue 
            location = bot.pick_stack() #The bot checks if you can stack it
            if location == -1: 
                location_discard = bot.pick_discard()  #the bot discards the card in one position
                removed_card = update_hand(comp_hand,deck,location_discard) #removed card
                bot.update_hand(location_discard)                           #computer updates its hand
                tips = discard(removed_card,trash,tips)                     #update tips
                bot.update_count_deck(removed_card)                         #update bot's count deck
            else:
                removed_card = update_hand(comp_hand,deck,location) #identify stacked card.
                bot.update_hand(location)                           #bot's hand update
                lives = try_stack(removed_card,stack,trash,lives)   #update lives
                bot.update_count_deck(removed_card)                 #update bot's count deck
            # Check if bot can pick a card to stack.
            # If yes, update bot's comp_hand, hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck               
            # and discard the selected card.
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives==0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break
