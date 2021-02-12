import os
from config import *

def landing_page():
    os.system('clear')
    print(Fore.RED+Style.BRIGHT+"\n"+" "*45+'''
:::    ::: :::       :::     :::     ::::::::: :::   :::           :::::::::      :::     :::        :::        
:+:   :+:  :+:       :+:   :+: :+:        :+:  :+:   :+:           :+:    :+:   :+: :+:   :+:        :+:        
+:+  +:+   +:+       +:+  +:+   +:+      +:+    +:+ +:+            +:+    +:+  +:+   +:+  +:+        +:+        
+#++:++    +#+  +:+  +#+ +#++:++#++:    +#+      +#++:             +#++:++#+  +#++:++#++: +#+        +#+        
+#+  +#+   +#+ +#+#+ +#+ +#+     +#+   +#+        +#+              +#+    +#+ +#+     +#+ +#+        +#+        
#+#   #+#   #+#+# #+#+#  #+#     #+#  #+#         #+#              #+#    #+# #+#     #+# #+#        #+#        
###    ###   ###   ###   ###     ### #########    ###              #########  ###     ### ########## ########## '''+" "*40)
    print("\n"+Fore.YELLOW+" "*51 + "By Archit Jain")
    print("\n"+Fore.WHITE+" "*22 + "--------------------------------------------------------------------\n")
    print(Fore.CYAN+"\n"+" "*50 + "Press 1 to start\n")
    print(Fore.CYAN+" "*45 + "Press any other key to exit\n")
    print("\n"+Fore.WHITE+" "*22 + "--------------------------------------------------------------------\n")
    
    print("\n\n")
    x = input(Fore.WHITE+" "*52+"Enter  : ")
    archit = 0
    try:
      val = int(x)
      if(val == 1 ):
            archit = 1
    except ValueError:
      if(x == "1" ):
            archit = 1
    return int(archit)

def quitmsg():
    os.system('clear')
    print("\n\n\n")
    print(Fore.BLUE + " "*20+ '''
            Y88b   d88P                      .d88888b.           d8b 888    
             Y88b d88P                      d88P" "Y88b          Y8P 888    
              Y88o88P                       888     888              888    
               Y888P  .d88b.  888  888      888     888 888  888 888 888888 
                888  d88""88b 888  888      888     888 888  888 888 888    
                888  888  888 888  888      888 Y8b 888 888  888 888 888    
                888  Y88..88P Y88b 888      Y88b.Y8b88P Y88b 888 888 Y88b.  
                888   "Y88P"   "Y88888       "Y888888"   "Y88888 888  "Y888 
                                                   Y8b ''' + "\n\n") 

def gameover(SCORE,TIME):
    os.system('clear')
    print("\n\n\n")
    print(Fore.BLUE + " "*20+ '''
             .d8888b.                                        .d88888b.                            
            d88P  Y88b                                      d88P" "Y88b                           
            888    888                                      888     888                           
            888         8888b.  88888b.d88b.   .d88b.       888     888 888  888  .d88b.  888d888 
            888  88888     "88b 888 "888 "88b d8P  Y8b      888     888 888  888 d8P  Y8b 888P"   
            888    888 .d888888 888  888  888 88888888      888     888 Y88  88P 88888888 888     
            Y88b  d88P 888  888 888  888  888 Y8b.          Y88b. .d88P  Y8bd8P  Y8b.     888     
             "Y8888P88 "Y888888 888  888  888  "Y8888        "Y88888P"    Y88P    "Y8888  888 ''' + "\n\n\n\n") 
    print(Fore.GREEN + " "*45+ "Final Score : "+ str(SCORE) +"\n")
    print(Fore.GREEN + " "*42+ "Time taken : "+ str(TIME) +" second(s) \n\n")
    print("\n"+Fore.WHITE+" "*20 + "----------------------------------------------------------------------\n")

def pausedmsg(SCORE,TIME):
    os.system('clear')
    print("\n\n\n")
    print(Fore.BLUE + " "*20 + '''
                            8888888b.                                          888      
                            888   Y88b                                         888      
                            888    888                                         888      
                            888   d88P 8888b.  888  888 .d8888b   .d88b.   .d88888      
                            8888888P"     "88b 888  888 88K      d8P  Y8b d88" 888      
                            888       .d888888 888  888 "Y8888b. 88888888 888  888      
                            888       888  888 Y88b 888      X88 Y8b.     Y88b 888      
                            888       "Y888888  "Y88888  88888P'  "Y8888   "Y88888 ''' + "\n\n") 
    print(Fore.GREEN + " "*45+ "Current Score : "+ str(SCORE) +"\n")
    print(Fore.GREEN + " "*42+ "Time taken : "+ str(TIME) +" second(s) \n\n")
    print("\n"+Fore.WHITE+" "*20 + "----------------------------------------------------------------------\n")
    print("\n"+Fore.WHITE+" "*20 + "                    < Press [R] or [r] to resume >                    \n")
    print("\n"+Fore.WHITE+" "*20 + "                     < Press [Q] or [q] to quit >                     \n")
