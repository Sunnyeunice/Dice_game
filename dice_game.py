

import random


def dice_roll():
    '''
    (None) -> int
    A function that simulates the roll of two six-sided dice
    returns integer between 2 and 12(included)
    
    >>> random.seed(2)
    >>> dice_roll()
    2
    >>> dice_roll()
    8
    >>> random.seed(9)
    >>> dice_roll()
    9
    >>> random.seed(20)
    >>> dice_roll()
    12
    '''
    # generating two random numbers between 1 and 6(both included)
    rand_1 = random.randint(1, 6)
    rand_2 = random.randint(1, 6)
    #summing the two random numbers
    sum_rand = rand_1 + rand_2
    return sum_rand


def second_stage(point):
    """
    (int) -> int
    simulates second stage of Pass Line Bet
    
    >>> random.seed(5)
    >>> r = second_stage(6)
    8 9 12 11 5 8 3 4 6 
    >>> r
    6
    >>> random.seed(709)
    >>> r = second_stage(10)
    11 4 3 3 8 2 10
    >>> r
    10
    >>> random.seed(3)
    >>> r = second_stage(9)
    7 
    >>> r
    7
    >>> random.seed(59)
    >>> r = second_stage(4)
    3 10 3 9 7 
    >>> r
    7
    
    """
    
    i = 0 
    # iterates through the loop until 7 or the point is reached
    # depending on which comes first and stops the loop
    while i != 7 and i != point:
        #calling a helper function
        i = dice_roll()
        print(i, end = " ") #prints on the same line
    print()
    return i
        
            


def can_play(money, bet):
    """
    (float, float) -> bool
    returns a booblean True if the bet is more than $0.0
    but not more than they own
    They can only play if the boolean is True
    
    >>> can_play(20.5, 7.5)
    True
    >>> can_play(20.9, 7.5)
    True
    >>> can_play(3.5, 7.5)
    False
    >>> can_play(0, 10.5)
    False
    """
    
    # returns True is the condition is satisfied
    # compares the bet with the money owned which must be greater than 0
    return (bet <= money and bet > 0)
    #otherwise returns False


def pass_line_bet(money, bet):
    """
    (float, float) -> float
    
    simulates what happens when a Pass Line Bet is placed
    returns a float corresponding to the amount of money the player has left
    
    >>> random.seed(5)
    >>> m = pass_line_bet(12.5, 3.5)
    A 8 has been rolled. Roll again!
    9 12 11 5 8 
    You win!
    >>> m
    16.0
    >>> random.seed(679)
    >>> m = pass_line_bet(11.05, 13.5)
    A 11 has been rolled. You win!
    >>> m
    24.55
    >>> random.seed(9)
    >>> m = pass_line_bet(4.5, 2.5)
    A 9 has been rolled. Roll again!
    6 4 7 
    You lose
    >>> m
    2.0
    >>> random.seed(72)
    >>> m = pass_line_bet(0.55, 0.5)
    A 6 has been rolled. Roll again!
    8 9 10 6 
    You win!
   """
    
    # calls a helper function and assign it to a variable
    point = dice_roll()
    if point == 7 or point == 11:
        # checks if a 7 or 11 has been played
        print("A", point, "has been rolled. You win!")
        #returns the money the player now has after winning
        return money + bet
    if point == 2 or point == 3 or point == 12:
        #checks if either a 2, 3 or 12 has been played 
        print("A", point, "has been rolled. You lose!")
        return money - bet
    # if the above statements don't execute, the following is checked 
    print("A", point, "has been rolled. Roll again!")
    # calls a helper function
    result = second_stage(point)
    if result == 7:
        print("You lose")
        return money - bet
    else:
        print("You win!")
        return money + bet
            


def play():
    """
    (None) -> None
    
    retrieves two inputs from the user and determines whether they
    cannot play not and if they can, the bet is placed
    
    >>> play()
    Please enter your money here: 12.5
    How much would you like to bet? 15.0
    Insufficient funds. You cannot play.
    >>> random.seed(279)
    >>> play()
    Please enter your money here: 13.0
    How much would you like to bet? 4.5
    A 7 has been rolled. You win!
    You now have $17.5
    >>> random.seed(789)
    >>> play()
    Please enter your money here: 12.5
    How much would you like to bet? 3.5
    A 10 has been rolled. Roll again!
    7 
    You lose
    You now have $9.0
    >>> random.seed(9)
    >>> play()
    Please enter your money here: 15.0
    How much would you like to bet? 9.5
    A 9 has been rolled. Roll again!
    6 4 7 
    You lose
    You now have $5.5
    """
    
    # asks for inputs from the user
    #converts the from string to float
    money = float(input("Please enter your money here: "))
    bet = float(input("How much would you like to bet? "))
    # first checks if the player has enough money
    # calls a helper function
    if not can_play(money, bet):
        print("Insufficient funds. You cannot play.")
        return # terminates the function
    else:
        # the helper function is True thus player can play
        money_left = pass_line_bet(money, bet)
        print("You now have $", end = '' )
        # displays the two print statements on the same line
        print(round(money_left, 2))
