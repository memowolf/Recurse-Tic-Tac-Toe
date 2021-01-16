# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:17:07 2021

@author: Memo
"""


def display_board(locale):
    print("\n")
    print(locale[0], "|", locale[1], "|", locale[2])
    print(locale[3], "|", locale[4], "|", locale[5])        
    print(locale[6], "|", locale[7], "|", locale[8]) 
    

def check_input():
    location = input("Which number location do you want to place your mark? ")
    while location not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        location = input("Please select a # between 1 and 9: ")
  
    return location

    
def open_slot(locale):
    valid = False
    while valid == False:
        location = check_input()
 
        if locale[int(location) - 1] == location:
            valid = True
        else:
            print("\nPlease pick an empty location: ")
        
        # end while valid == False:
            
    return location
    
    
def x_or_o(locale, location, player):
    if location == "1":
        locale[0] = player
    elif location == "2":
        locale[1] = player
    elif location == "3":
        locale[2] = player
    elif location == "4":
        locale[3] = player
    elif location == "5":
        locale[4] = player
    elif location == "6":
        locale[5] = player
    elif location == "7":
        locale[6] = player
    elif location == "8":
        locale[7] = player
    elif location == "9":
        locale[8] = player
    return locale
    
def score_test(locale, player):
    if locale[0] == locale[1] == locale[2] == player or \
        locale[3] == locale[4] == locale[5] == player or \
        locale[6] == locale[7] == locale[8] == player or \
        locale[0] == locale[3] == locale[6] == player or \
        locale[1] == locale[4] == locale[7] == player or \
        locale[2] == locale[5] == locale[8] == player or \
        locale[0] == locale[4] == locale[8] == player or \
        locale[2] == locale[4] == locale[6] == player:
            return True

def all_full(locale):
    taken = True
    for i in locale:
        if i != "X" and i != "O":
            taken = False        
    return taken


#main program
game_on = True

while game_on == True:  
    board = ["1","2","3","4","5","6","7","8","9"]
    no_score = True
    
    while no_score == True:
        display_board(board)
        print("\nPlayer X's turn")
        
        x_turn = open_slot(board)
        
        x_or_o(board, x_turn, "X")

        if score_test(board, "X") == True:        
            no_score = False
            print("\nPlayer X is the winner")
        
        if all_full(board) == True:
             no_score = False
             print("\n\nThere is no winner")
            
      
        if no_score == True:
            display_board(board)
            print("\nPlayer O's turn")
            
            o_turn = open_slot(board)
                            
            x_or_o(board, o_turn, "O")
    
            if score_test(board, "O") == True:        
                no_score = False
                print("Player O is the winner")                
                
        # end while no_score == True:
        
        
    game_on = False
    display_board(board)
    print("\nGame over")
    # end while game_on == True:
     