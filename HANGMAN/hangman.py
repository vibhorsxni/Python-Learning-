import hard
import easy
import medium

print(r'''
 __      __       .__                                .____           __ /\        __________.__                
/  \    /  \ ____ |  |   ____  ____   _____   ____   |    |    _____/  |)/ ______ \______   \  | _____  ___.__.
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  |    |  _/ __ \   __\/  ___/  |     ___/  | \__  \<   |  |
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/  |    |__\  ___/|  |  \___ \   |    |   |  |__/ __ \\___  |
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  > |_______ \___  >__| /____  >  |____|   |____(____  / ____|
       \/       \/          \/            \/     \/          \/   \/          \/                      \/\/     

  o         o           o           o          o        o__ __o          o          o           o           o          o  
 <|>       <|>         <|>         <|\        <|>      /v     v\        <|\        /|>         <|>         <|\        <|> 
 < >       < >         / \         / \\o      / \     />       <\       / \\o    o// \         / \         / \\o      / \ 
  |         |        o/   \o       \o/ v\     \o/   o/                  \o/ v\  /v \o/       o/   \o       \o/ v\     \o/ 
  o__/_ _\__o       <|__ __|>       |   <\     |   <|       _\__o__      |   <\/>   |       <|__ __|>       |   <\     |  
  |         |       /       \      / \    \o  / \   \\          |  |    / \        / \      /       \      / \    \o  / \ 
 <o>       <o>    o/         \o    \o/     v\ \o/     \         / \o/   \o/        \o/    o/         \o    \o/     v\ \o/ 
  |         |    /v           v\    |       <\ |       o       o   |     |          |    /v           v\    |       <\ |  
 / \       / \  />             <\  / \        < \      <\__ __/>  / \   / \        / \  />             <\  / \        < \ 
      ''')


user_choice = input("Enter your choice for game toughness (E/M/H) : ")

if (user_choice in ["E","e","M","m","H","h"]) :

     if(user_choice in ["e","E"]) :
          word = easy.choice_easy() 
          i = 0 
          while(i< len(word)):
               print(f"_", end = " ") 
               i+=1       
     elif(user_choice in ["M","m"]) :
          medium.choice_med()
     elif(user_choice in ["H","h"]):
          hard.choice_hard()
     else :
          print("Error 404 ")
else :
     print("Enter A Valid Input My Dear User ")
     