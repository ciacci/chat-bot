import telepot
import time
import os, random
from pprint import pprint

def handle(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    #print content_type, chat_type, chat_id
    if content_type == "text":
        msg=message['text']
        if msg== "/sabino":
            bot.sendPhoto(chat_id,open("/home/francesco/Telegram/img/sabino.jpg","rb"))
        elif msg== "/chat":
            img_path="/home/francesco/Telegram/img/chat/"
            img_name=random.choice(os.listdir(img_path))
            img=open(img_path+img_name,"rb")
            bot.sendPhoto(chat_id,img)
            bot.sendMessage(chat_id,"Awend ne")
        elif msg =="/spaghitt":
            bot.sendPhoto(chat_id,open("/home/francesco/Telegram/img/spaghitt.jpg","rb"))
            bot.sendAudio(chat_id,open("/home/francesco/Telegram/audio/spaghitt.ogg","rb"))
            bot.sendMessage(chat_id,"300 gremm d spaghitt, ma vou seit pezz!")
        else:
            if any(x in msg for x in ["nicola","Nicola","ncol","Ncol","nco","Nco","Violo","violo","Violante","violante"]):
                bot.sendMessage(chat_id,"Ncoooooo");
            elif any(x in msg for x in ["Cassa","cassa"]):
                bot.sendMessage(chat_id,"CASSAAAAAAAA");
        #bot.sendMessage(chat_id,message['text'])
            
bot=telepot.Bot("405730557:AAHauZjh1qYStRZGRYMz6EuZFtnU30TeABM")
bot.message_loop(handle, run_forever=True)
#print "In attesa di nuovi messaggi..."


#while 1:
#    time.sleep(10)
