import pyttsx3
import os
import webbrowser
import psutil
print('\n')

print("SYSTEM STATUS")

print("\n")


pid = os.getpid()
py = psutil.Process(pid)
print(pid)
for pro in psutil.process_iter():
    try:
        processName = pro.name()
        processID = pro.pid
        print(processName , ' = ', processID)
    except (psutil.NoProcess, psutil.Protected, psutil.ZombieProcess):
        pass
print("\n")
print("the  options we have here are :")
print("\n")
print('*.youtube')
print("\n")
print('*.play diffrent songs')
print("\n")
print('*.corona cases live status in india')
print("\n")
print('*.google searching')
print("\n")
print('*.wikipedia searching')
print("\n")
print('*.run notepad')
print("\n")
print('*.book ticket')
print("\n")
print('*.latest news feeds')
print("\n")
print('*.run window media player')
print("\n")
print("*.play games")
print("\n")
print('*.to exit type bye or thank you')
print("\n")



while True:
	print("please write your choice (eg. play music) : "  , end='')
	p = input()

	if ("run" in p) or ("" in p)  and ("chrome" in p):
	  os.system("chrome")
	elif("latest" in p) and ('news' in p):
		webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

	elif (("run" in p) or  ("open" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	elif (("open" in p) or  ("play" in p )) and  (("youtube" in p) or ("vedio" in p) ) :
	  webbrowser.open("www.youtube.com")
	
	elif (("lets" in p) or  ("open" in p )) and  (("google" in p) or ("search" in p) ) :
	  webbrowser.open("www.google.com")

	elif (("open" in p) or  ("redirect to" in p )) and  (("wikipedia" in p) or ("wiki" in p) ) :
	  webbrowser.open("www.wikipedia.com")

	elif (("open" in p) or  ("play" in p )) and  (("game" in p) or ("games" in p) ) :
	  webbrowser.open("http://gametug.com")

	elif (("book" in p) or  ("redirect to" in p )) and  ((" ticket" in p) or ("tickets" in p) ) :
		print('\n')
		print("of which field you want to book your ticket please mention(eg.flight):")
		print('\n')
		print("*flight")
		print('\n')
		print("*train")
		print('\n')
		print("*bus")
		print('\n')
		print("*back")
		print('\n')
		print("please enter the field :",end='')
		y=input()
		if("flight" in y):
			webbrowser.open("www.goindigo.in")

		elif("bus" in y):
			webbrowser.open("www.irctc.com")
		
		elif("bus" in y):
			webbrowser.open("https://www.redbus.in/bus-tickets")
		elif("back" in y):
			break
    
	elif (("covid-19" in p) or  ("corona" in p )) and  (("stats" in p) or ("cases" in p) ) :
	  webbrowser.open("www.google.com/search?sxsrf=ALeKk010Tctl0jZIPBGXEtMS19PSo_18lw%3A1597785899533&source=hp&ei=K0c8X5HPHvOW4-EPuaqXqAY&q=total+corona+cases+india&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDuDWgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab")

	elif ("run" in p)  or ("open" in p) and ("media" in p or ("player" in p)):
	  os.system("wmplayer")
	elif ("play" in p)  or ("player" in p) and ("music" in p) or ("songs" in p):
		print("what will you like to listen :")
		print('\n')
		print("*.edm")
		print('\n')
		print("*.rock")
		print('\n')
		print("*.soothing")
		print('\n')
		print("*.motivational")
		print('\n')
		print("*.back if dont want to visit")
		print('\n')
		print("please enter your choice : "  , end='')
		print('\n')
		x = input()
		if("edm" in x):
			webbrowser.open("https://www.youtube.com/watch?v=gCYcHz2k5x0&list=PLw6eTMMKY24QLYfmrU2rB8x-lP5Fas2dY")
		elif("rock" in x):
			webbrowser.open("https://www.youtube.com/watch?v=ktvTqknDobU&list=PLzxEw1CbicllxqVJaN9hodbkMXNX0Cnds")
		elif("soothing" in x):
			webbrowser.open("https://www.youtube.com/watch?v=RgKAFK5djSk&list=PLMjMdpuyQeDNFTh3B_vl3RwYMRf70I4He")
		elif("motivational" in x):
			webbrowser.open("https://www.youtube.com/watch?v=zLVZxHWL0ro&list=PL4taEUw-UM8QZ7NiTUm2mEpzia2ulckpi")
		elif("back" in x):
		    break
		

	  

	elif  ("bye" in p)  or ("thank you" in p):
	  break

	else:
	  print("please use correct keywords")



#Created by -- MUDRIK KAUSHIK