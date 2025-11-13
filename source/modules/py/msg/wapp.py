#import pywhatkit as kit
from auto_whatsapp import auto_whatsapp
from datetime import datetime
import os
import sys

phone = "+5584991089575"
users = ["Susan"]
msg = "Teste Python"

auto_whatsapp.sendChat(users, msg)





'''
data_atual = datetime.now()

print(data_atual.day)
print(data_atual.hour)
print(data_atual.minute)


print(os.environ)
print("---------------------------")
print(sys.path)
'''