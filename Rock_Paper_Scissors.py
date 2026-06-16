import random
l1=["Rock","Paper","Scissors"]
attempt=0
user_score=0
computer_score=0

while True:
    attempt=attempt+1
    print("\n================================")
    print("Round", attempt)
    print("================================")
    
    user=input("Enter(Rock/Paper/Scissors):")
    computer=random.choice(l1)
    print("User's Choice=",user)
    print("Computer's choice=",computer)
    
    if user=="Rock" and computer=="Rock":
        print("No points Its a Draw")
        print("User Score=",user_score," Computer Score=",computer_score)
        
        
    elif user=="Rock" and computer=="Scissors":
        user_score=user_score+1
        print("User won this round")
        print("User Score=",user_score," Computer Score=",computer_score)
        
    elif user=="Rock" and computer=="Paper":
        computer_score=computer_score+1
        print("Computer won this round")
        print("User Score=",user_score," Computer Score=",computer_score)
        
    elif user=="Paper" and computer=="Scissors":
         computer_score=computer_score+1
         print("Computer won this round")
         print("User Score=",user_score," Computer Score=",computer_score)
          
    elif user=="Paper" and computer=="Paper":
         print("No points.Its a Draw")
         print("User Score=",user_score," Computer Score=",computer_score)
         
    elif user=="Paper" and computer=="Rock":
         user_score=user_score+1
         print("User won this round")
         print("User Score=",user_score," Computer Score=",computer_score)
         
    elif user=="Scissors" and computer=="Rock":
         computer_score=computer_score+1
         print("Computer won this round")
         print("User Score=",user_score," Computer Score=",computer_score)
          
    elif user=="Scissors" and computer=="Scissors":
         print("No points.Its a Draw")
         print("User Score=",user_score," Computer Score=",computer_score)
         
    elif user=="Scissors" and computer=="Paper":
         user_score=user_score+1
         print("User won this round")
         print("User Score=",user_score," Computer Score=",computer_score)
    else:
        print("Enter a valid string")
        
    if user_score==3:
       print("\n================================")
       print("GAME OVER")
       print("================================")
       print("Winner : User")
       print("Final Score")
       print("User     :", user_score)
       print("Computer :", computer_score)
       print("Rounds Played :", attempt)
       break
        
    elif computer_score==3:
        print("\n================================")
        print("GAME OVER")
        print("================================")
        print("Winner : User")
        print("Final Score")
        print("User     :", user_score)
        print("Computer :", computer_score)
        print("Rounds Played :", attempt)
        break

    
