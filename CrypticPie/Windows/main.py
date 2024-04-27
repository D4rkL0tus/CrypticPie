"""
    CRYPPY IS A FRAMEWORK FOR AUTOMATION OF CRYPTO TRADING
    SUPPLIED WITH DIFFERENT ALGORITHSN THAT WILL ASSIST YOU 
    IN AUTOMATED TRADING OF CRYPTO
    WITH SUPPORT FOR THE MAJOR CRYPTO EXCHANGES
    THIS SOFTWARE WILL DO YOU WELL WITHIN TRADING

    Author: Trent W. Schake
    Version: NOT_REALEASED
    Python_Version: 3.11

    This is signed under the MIT opensource licensening
    for more informaiton on the MIT license please follow the
    following URL:
    [https://en.wikipedia.org/wiki/MIT_License]
"""
import threading
import os
import time


# Where the program starts
def main():
    MenuUserInput = input() # defines a variable for user input
    UserMenu = """  
                  |  SweetiePie |
            Created By Trent W. Schake
    
        [1] Start Trading   [2] Configuration
        [3] Exit           
    """
    match MenuUserInput:
        case "1":
            try:
                StartTrading()
            except "2":
                exit()
        case "2":
            try:
                ConfigurationMenu()
            except:
                exit()
        case "3":
            exit()
# Function that is used for starting the Trading Service            
def Stattrading():
    print("TEST")

def ConfigurationMenu():
    ConfigurationMenu = """"
                    | Configuration |
        
        [1] Select Crypto Services [2] Set Trading Parameters
        [3]
    """

if __name__ == '__main__':
    main()

