from config import *

arr =[
     [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    
     [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
    
     [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
      [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
      [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    ]

def setup(level):
    arrp = []
    arp = []
    striii=""
    I=int(len(arr[level]))
    for i in range(0,I):
        J=int(len(arr[level][i]))
        striii+="    | "
        arp = [" "]*4 + ["|"," "]
        for j in range(0,J):
            if(arr[level][i][j]==0):
                striii+="      "
                arp = arp + [" "]*5
            elif(arr[level][i][j]==1):
                striii+= Back.CYAN+Fore.BLACK+"[   ]"+RESET+" "
                temp1 = bcolors['Cyan'] + colors['Black'] + "[" + RESET
                temp2 = bcolors['Cyan'] + colors['Black'] + " " + RESET
                temp3 = bcolors['Cyan'] + colors['Black'] + "]" + RESET
                arp = arp + [temp1,temp2,temp2,temp2,temp3," "]
            elif(arr[level][i][j]==2):
                striii+= Back.BLUE+Fore.BLACK+"[   ]"+RESET+" "
                temp1 = bcolors['Blue'] + colors['Black'] + "[" + RESET
                temp2 = bcolors['Blue'] + colors['Black'] + " " + RESET
                temp3 = bcolors['Blue'] + colors['Black'] + "]" + RESET
                arp = arp + [temp1,temp2,temp2,temp2,temp3," "]
            elif(arr[level][i][j]==3):
                striii+= Back.RED+Fore.BLACK+"[   ]"+RESET+" "
                temp1 = bcolors['Red'] + colors['Black'] + "[" + RESET
                temp2 = bcolors['Red'] + colors['Black'] + " " + RESET
                temp3 = bcolors['Red'] + colors['Black'] + "]" + RESET
                arp = arp + [temp1,temp2,temp2,temp2,temp3," "]
            elif(arr[level][i][j]==4):
                striii+= Back.GREEN+Fore.BLACK+"[   ]"+RESET+" "
                temp1 = bcolors['Green'] + colors['Black'] + "[" + RESET
                temp2 = bcolors['Green'] + colors['Black'] + " " + RESET
                temp3 = bcolors['Green'] + colors['Black'] + "]" + RESET
                arp = arp + [temp1,temp2,temp2,temp2,temp3," "]
            elif(arr[level][i][j]==-1):
                striii+= Back.YELLOW+Fore.BLACK+"[   ]"+RESET+" "
                temp1 = bcolors['Yellow'] + colors['Black'] + "[" + RESET
                temp2 = bcolors['Yellow'] + colors['Black'] + " " + RESET
                temp3 = bcolors['Yellow'] + colors['Black'] + "]" + RESET
                arp = arp + [temp1,temp2,temp2,temp2,temp3," "]
        striii+="|"
        arp = arp + ["|"]
        arrp.append(arp)
        if(i!=I-1):
            striii+="\n"
    return arrp

