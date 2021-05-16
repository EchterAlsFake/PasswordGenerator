from colorama import *
import string
import secrets
from tqdm import tqdm
from pyfiglet import Figlet
from time import sleep
from random import uniform
for i in tqdm(range(144)):
    sleep(uniform(0.05, 0.001))
f = Figlet(font='big')
sleep(2)
print(Fore.LIGHTGREEN_EX + f.renderText(text="Password   Generator"))
sleep(2)
print(Fore.LIGHTGREEN_EX + "[+]" + Fore.BLUE + "Author==EchterAlsFake")
print("Generating Password..")
for x in tqdm(range(144)):
    sleep(uniform(0.05, 0.001))
chars = string.digits + string.ascii_letters + string.punctuation
print(len(chars))
print(''.join(secrets.choice(chars)for _ in range(40)))
Password = input("Enter the generated Password")
Document = input("Dateipfad und name (Datei muss nicht existiren In dem Fall wird sie erstellt)")
f = open(Document, 'a')
f.write(Password)
