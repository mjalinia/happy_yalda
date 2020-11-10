import os

import time

WIDTH = 79

"""                              instagram:  @mohammad_._javad
                                 
                                 telegram : @mj_alinia 
                                 
                                 email : aliniajavad@yahoo.com
"""
    
message = "YALDA MOBARAK H".upper()

printedMessage = [ "","","","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "Y" : [ "**   **",
                       "**   **",
                       "**   **",
                       "   **  ",
                       "   **  ",
                       "   **  ",
                       "   **  " ],
               
               "A" : [ "******",
                       "**  **",
                       "**  **",
                       "******",
                       "**  **",
                       "**  **",
                       "**  **" ], 

               "L" : [ "**    ",
                       "**    ",
                       "**    ",
                       "**    ",
                       "**    ",
                       "**    ",
                       "******" ],

               "D" : [ "******   ",
                       "**    ** ",
                       "**     **",
                       "**     **",
                       "**     **",
                       "**    ** ",
                       "******   " ],

               "M" : [ "***          ***",
                       "** **      ** **",
                       "**  **    **  **",
                       "**   **  **   **",
                       "**     **     **",
                       "**     **     **",
                       "**     **     **" ],
                "B" : ["******  ",
                       "**   ** ",
                       "**   ** ",
                       "******  ",
                       "**   ** ",
                       "**   ** ",
                       "******  " ],
               
               
                "R" : ["*****   ",
                       "**   ** ",
                       "*    ** ",
                       "*****   ",
                       "** **   ",
                       "**  **  ",
                       "**   ** " ],
                "K" : ["**      **",
                       "**    **  ",
                       "**  **    ",
                       "**        ",
                       "**  **    ",
                       "**    **  ",
                       "**     ** " ],
                "O" : ["  ***  ",
                       "**   **",
                       "**   **",
                       "**   **",
                       "**   **",
                       "**   **",
                       "  ***  " ],
                ":" : ["  ***  ",
                       " ***** ",
                       "  ***  ",
                       "       ",
                       "  ***  ",
                       " ***** ",
                       "  ***  " ],
                "H" : ["**---------------------------------**",
                       " **   @             @       @     ** ",
                       "  **       @                     **  ",
                       "   **             @      @      **   ",
                       "     ***                      ***    ",
                       "       ******             ******     ",
                       "            **************           " ],
}







for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")


offset = WIDTH
while True:
    try:

        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

        for row in range(7):
            print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    
        offset -=1
   
        if offset <= ((len(message)+2)*6) * -1:
            offset = WIDTH
    
        time.sleep(0.05)
    except:
        print("\n\033[92mUser using CTRL + C...")
        exit(0)
