#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Step 1: Open the web browser
#Step 2: Go to the Linkedin
#Step 3: Change the URl to an user
#Step 4: Import the csv text
#Step 5: Write the text

#!pip install openpyxl
#!pip install numpy
import pandas as pd #!pip install pandas
import pyautogui #!pip install pyautogui
import pyperclip
import datetime
import time

pyautogui.PAUSE = 0.9

#Step 1:
import os
os.system("xdg-open \"\"https://www.google.com.br/")

#OR
#import webbrowser  
#webbrowser.open("https://www.google.com.br/", new=0, autoraise=True)

#Step 2:
time.sleep(2)
pyautogui.write("linkedin")
pyautogui.press("enter")
time.sleep(2)
print(pyautogui.position())
pyautogui.click(x=350, y=385) #Link do Linkedin #1920p = 350x, 960p = 175x
time.sleep(8)

#Step 3:
pyautogui.hotkey("alt", "d")
pyautogui.press("backspace")
pyautogui.write("linkedin.com")
pyautogui.press("slash")
pyautogui.press("right")
pyautogui.write("in")
pyautogui.press("slash")
pyautogui.press("right")
pyautogui.write("davibrinhosa")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=500, y=660)#Botao de Mensagem #1920p = 500x, 960p = 250x
pyautogui.click(x=1400, y=880) #Botao do chat #1920p = 1400x, 960p = 700x
time.sleep(2)

#Step 4:
tabela = pd.read_csv(r"/home/whitepaladin-linux/Documents/GitHub/IntesivoPython/Project_01/csv_for_python.csv") #, sep=";" -> separation example
text01 = tabela.iloc[0, 0]
text02 = tabela.iloc[0, 1]
joke_text = tabela["Part_03"].sum()
text_date = str(datetime.datetime.now().strftime('%d-%b-%Y'))
complement_text = f"""
So, we finish the Project 01 in the date {text_date}.
"""
complete_text = str(text01) + str(text02) + str(joke_text) + str(complement_text)
time.sleep(2)

#Step 5:
pyperclip.copy(complete_text)
pyautogui.hotkey("ctrl","v")
#pyautogui.hotkey("ctrl", "enter")


# In[9]:


#Test Area

