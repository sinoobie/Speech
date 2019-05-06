from gtts import gTTS
import subprocess as sp
import os,time,sys,datetime,wikipedia,webbrowser,gtts


#color
col='\033[9'
lg=col+'2m'
lc=col+'6m'
lw=col+'7m'

wikipedia.set_lang("en")
filesave='audio/bicara.mp3'
class main:
	def __init__(self,cari,query):
		self.cari=cari
		self.query=query
	def salam(self):
		waktu=int(datetime.datetime.now().hour)
		if waktu >= 0 and waktu < 12:
			bicara = ("good morning dude!")
			tts = gTTS(text=bicara, lang='en')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		if waktu >= 12 and waktu < 18:
			bicara = ("good afternoon dude!")
			tts = gTTS(text=bicara, lang='en')
			tts.save(filesave)
			print(f'{lc}computer:{lw} '+bicara)
			say()
		if waktu >= 18 and waktu != 0:
			bicara = ("good night dude!")
			tts = gTTS(text=bicara, lang='en')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		bicara="hello, i karin the speech text program. can i help you?"
		tts=gTTS(text=bicara,lang='en')
		tts.save(filesave)
		print(f'{lc}computer: {lw}'+bicara)
		say()
	
	def wiki(self):
		bicara=wikipedia.summary(self.cari,sentences=2)
		tts=gTTS(text=bicara,lang='en')
		tts.save(filesave)
		print(f'{lc}computer: {lw}'+bicara)
		say()
	
	def basa_basi(self):
		if 'hallo karin' in self.query:
			bicara='hallo dude!'
			tts=gTTS(text=bicara,lang='en')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		elif '/exit' in self.query:
			bicara='thanks for using me. goodbye!'
			tts=gTTS(text=bicara,lang='en')
			tts.save(filesave)
			print(f'{lc}computer:{lw} '+bicara)
			say()
			exit()
		elif '/google' in self.query:
			tts=gTTS(text='open google, please wait!',lang='en')
			tts.save(filesave)
			print(f'{lc}computer:{lw} open google, please wait!')
			say()
			webbrowser.open('https://google.com')
		elif '/youtube' in self.query:
			bicara='open youtube, please wait'
			tts=gTTS(text=bicara,lang='en')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
			webbrowser.open('https://youtube.com')
		elif '/facebook' in self.query:
                        bicara='open facebook, please wait'
                        tts=gTTS(text=bicara,lang='en')
                        tts.save(filesave)
                        print(f'{lc}computer: {lw}'+bicara)
                        say()
                        webbrowser.open('https://facebook.com')
		elif '/say' in self.query:
			bicara=self.query.replace('/say ','')
			tts=gTTS(text=bicara,lang='en')
			tts.save(filesave)
			print(f'{lc}computer:{lw} '+bicara)
			say()
		elif '/help' in self.query:
			bicara=("""i just understand this command:
\t/wiki\t\t for search on wikipedia
\t/google\t\t for open the google
\t/youtube\t for open the youtube
\t/facebook\t for open the facebook

\t/say\t\t for say something query
\t/exit\t\t for exit the program
\t/help\t\t for display this help""")
			tts=gTTS(text=bicara,lang='en')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		else: warm()
		
def say():
	sp.call('mpv '+filesave, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

def warm():
	bicara="sorry I don't understand what you command, please type /help"
	tts=gTTS(text=bicara,lang='en')
	tts.save(filesave)
	print(f'{lc}computer:{lw} '+bicara)
	say()

if __name__=='__main__':
	try:
		run=main(None,None)
		run.salam()
		while True:
			try:
				cmd=input(f'{lg}command:{lw} ')
				if '/wiki' in cmd:
					com=cmd.replace('/wiki ','')
					run=main(com,None)
					run.wiki()
				else:
					run=main(None,cmd)
					run.basa_basi()
			except SystemExit: exit()
			except: warm()
	except KeyboardInterrupt: exit("\nkey intterupt")
	except gtts.tts.gTTSError: exit("Error. try:\ncheck your internet connection or contact the author")
