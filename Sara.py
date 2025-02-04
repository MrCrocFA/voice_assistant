# SARA or KESHA 2.0

import pyttsx3
import os
import random
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *

# global variables section

text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
adress = ''
j = 0
task_number = 0

ndel = ['сара', 'zara', 'саров', 'ладно', 'не могла бы ты','пожалусйта']

commands = ['привет', 'открой файл', 'выключи комп', 'выруби компьютер', 'пока', 'покажи файл','покажи список команд',
'открой браузер', 'открой интернет', 'открой youtube', 'включи музон','вруби музыку', 'очисти файл',
'открой стату', 'покажи cтатистику', 'открой музыку', 'переведи', 'планы', 'на будущее', 'что планируется']


def pri_com(): # displays request history
	z = {}
	mas = []
	mas2 = []
	mas3 = []
	mas4 = []
	file = open('commands.txt', 'r', encoding = 'UTF-8')
	k = file.readlines()
	for i in range(len(k)):
		line = str(k[i].replace('\n','').strip())
		mas.append(line)
	file.close()
	for i in range(len(mas)):
		x = mas[i]
		if x in z:
			z[x] += 1
		if not(x in z):
			b = {x : 1}
			z.update(b)
		if not(x in mas2):
			mas2.append(x)
	for i in mas2:
		mas3.append(z[i])
	for i in range(1, len(mas3)+1):
		mas4.append(str(i)+') ')	
	list = pd.DataFrame({
		'command' : mas2,
		'count' : mas3
	}, index = mas4)
	list.index.name = '№'
	print(list)

def plans():
	global engine
	# PLAAANS :))
	plans = ''' 
	Моя задача будет заключаться в помощи в управлении системой умного дома.
	На данный момент ведется работа над виртуальной частью программного обеспечения.
	Так же ведется работа по оптимизации всех существующих в коде функций.
	В дальнейшем планируется работа над технической частью проекта.
	Она будет состоять из создания эллементов умного дома с помощью микроконтроллеров Arduino.
	В конечном итоге виртуальная и техническая части проекта будут обьеденены.
	Моя конечная цель будет достигнута.
	 '''
	engine.say(plans)

def clear_analis(): # clearing the request history file
	global engine
	file = open('commands.txt', 'w', encoding = 'UTF-8')
	file.close()
	engine.say('Файл аналитики очищен!')

def add_file(x):
	file = open('commands.txt', 'a',encoding = 'UTF-8')
	if x != '':
		file.write(x+'\n')
	file.close()	

def comparison(x): # searches for the most suitable function for the request
	global commands,j,add_file
	ans = ''
	for i in range(len(commands)):
		k = fuzz.ratio(x,commands[i])
		if (k > 50)&(k > j):
			ans = commands[i]
			j = k
	if (ans != 'пока')& (ans != 'привет'):
		add_file(ans)
	return(str(ans))

def web_search(): # searches the Internet for the query (address)
	global adress
	webbrowser.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(adress))

def check_searching(): # checks, you need to search on the Internet
	global text,wifi_name,add_file
	global adress
	global web_search
	if 'найди' in text:
		add_file('найди')
		adress = text.replace('найди','').strip()
		text = text.replace(adress,'').strip()
		web_search()
		text = ''
	elif 'найти' in text:
		add_file('найди')
		adress = text.replace('найти','').strip()
		text = text.replace(adress,'').strip()
		web_search()
		text = ''
	adress = ''

def clear_task(): # removes keywords
	global text,ndel
	for z in ndel:
		text = text.replace(z,'').strip()
		text = text.replace('  ',' ').strip()
		
def hello(): # greeting function
	global engine
	z = ["Рада снова вас слышать!", 'Что вам угодно?', 'Привет. Чем-нибудь помочь?']
	x = random.choice(z)
	engine.say(x)

def quit():
	global engine
	x = ['надеюсь мы скоро увидемся!', 'рада была помочь', 'всегда к вашим услугам']
	engine.say(random.choice(x))
	engine.runAndWait()
	engine.stop()
	os.system('cls')
	exit(0)

def show_cmds(): # displays a list of available commands
	my_com = ['привет', 'открой файл', 'выключи компьютер', 'пока', 'покажи список команд',
	'открой vk', 'открой интернет', 'открой youtube', 'включи музыку', 'очисти файл', 'покажи cтатистику']
	for i in my_com:
		print(i)
	time.sleep(2)	

def brows(): # open browser
	webbrowser.open('https://google.ru')

def youtube(): # open YT
	webbrowser.open('https://www.youtube.com')

def shut(): # shut down
	global quit
	os.system('shutdown /s /f /t 10')
	quit()	

def musik(): # music
	webbrowser.open('https://z1.fm/')

def check_translate():
	global text, tr
	tr = 0
	variants = ['переведи', 'перевести', 'переводить', 'перевод']
	for i in variants:	
		if (i in text)&(tr == 0):
			word = text
			word = word.replace('переведи','').strip()
			word = word.replace('перевести','').strip()
			word = word.replace('переводить','').strip()
			word = word.replace('перевод','').strip()
			word = word.replace('слово','').strip()
			word = word.replace('слова','').strip()
			webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text={}'.format(word))
			tr = 1
			text = ''

cmds = {
	'привет' : hello,							'выруби компьютер' : shut,					'выключи комп' : shut,
	'пока' : quit,								'покажи  cтатистику' : pri_com,				'покажи список команд' : show_cmds,													
	'открой браузер' : brows,					'открой интернет' : brows,
	'открой youtube' : youtube,					'вруби музыку' : musik,
	'открой  стату' : pri_com,					'включи музон' : musik,						'очисти файл' : clear_analis,
	'покажи файл' : pri_com, 					'открой файл' : pri_com,					'открой музыку' : musik,
	'планы' : plans,							'на будущее' : plans, 						'что планируется' : plans,
	'переведи' : check_translate
}

# recognize

def talk(): 
	global text, clear_task
	text = ''
	with sr.Microphone() as sourse:
		print('Я вас слушаю: ')
		r.adjust_for_ambient_noise(sourse)
		audio = r.listen(sourse, phrase_time_limit=3)
		try:
			text = (r.recognize_google(audio, language="ru-RU")).lower()	
		except(sr.UnknownValueError):
			pass
		except(TypeError):
			pass
		os.system('cls')
		lb['text'] = text
		clear_task()

# run command

def cmd_exe():
	global cmds, engine, comparison, check_searching, task_number, text, lb
	check_translate()
	text = comparison(text)
	print(text)
	check_searching()
	if (text in cmds):
		if (text != 'привет') & (text != 'пока') & (text != 'покажи список команд'):
			k = ['Секундочку', 'Сейчас сделаю', 'уже выполняю']
			engine.say(random.choice(k))
		cmds[text]()
	elif text == '':
		pass
	else:
		print('Команда не найдена!')
	task_number += 1
	if (task_number % 10 == 0):
		engine.say('У вас будут еще задания?')
	engine.runAndWait()
	engine.stop()


print(Fore.YELLOW + '', end = '')
os.system('cls')

# inf loop

def main():
	global text, talk, cmd_exe, j
	try:
		talk()
		if text != '':
			cmd_exe()
			j = 0
	except(UnboundLocalError):
		pass
	except(TypeError):
		pass

# GUI

root = Tk()
root.geometry('250x350')
root.configure(bg = 'gray22')
root.title('Sara')
root.resizable(False, False)

lb = Label(root, text = text)
lb.configure(bg = 'gray')
lb.place(x = 25, y = 25, height = 25, width = 200)

but1 = Button(root, text = 'Слушать', command = main)
but1.configure(bd = 1, font = ('Castellar', 25), bg = 'gray')
but1.place(x = 50, y = 160, height = 50, width = 150)

but2 = Button(root, text = 'Выход', command = quit)
but2.configure(bd = 1, font = ('Castellar',25), bg = 'gray')
but2.place(x = 50, y = 220, height = 50, width = 150)

root.mainloop()

while True:
	main()