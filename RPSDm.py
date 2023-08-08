types_list = ["rock", "paper", "scissors"]

def user_input():
    
    print("Welcome to RPSDm(rock, paper, scissors Deathmatch)  - Made by Dav ")
    
    while True:
        user_input = input("Enter rock, paper or scissors: ").lower()
        if user_input in types_list:
            break
        else:
            continue
        
