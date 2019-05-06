from gtts import gTTS
import subprocess as sp
import os,time,sys,datetime,wikipedia,webbrowser,gtts

#color
col='\033[9'
lg=col+'2m'
lc=col+'6m'
lw=col+'7m'

wikipedia.set_lang("id")
filesave='audio/bicara.mp3'
class main:
	def __init__(self,cari,query):
		self.cari=cari
		self.query=query
	def salam(self):
		waktu=int(datetime.datetime.now().hour)
		if waktu >= 0 and waktu < 12:
			bicara = ("selamat pagi gan!")
			tts = gTTS(text=bicara, lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		if waktu >= 12 and waktu < 18:
			bicara = ("selamat siang gan!")
			tts = gTTS(text=bicara, lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		if waktu >= 18 and waktu != 0:
			bicara = ("selamat malam gan!")
			tts = gTTS(text=bicara, lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		bicara="hallo, saya adalah karin speech text program. ada yang bisa saya bantu?"
		tts=gTTS(text=bicara,lang='id')
		tts.save(filesave)
		print(f'{lc}computer: {lw}'+bicara)
		say()
	
	def wiki(self):
		bicara=wikipedia.summary(self.cari,sentences=2)
		tts=gTTS(text=bicara,lang='id')
		tts.save(filesave)
		print(f'{lc}computer: {lw}'+bicara)
		say()
	
	def basa_basi(self):
		if 'hallo karin' in self.query:
			bicara='hallo gan!'
			tts=gTTS(text=bicara,lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		elif '/exit' in self.query:
			bicara='terima kasih sudah memakai program ini. sampai jumpa!'
			tts=gTTS(text=bicara,lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
			exit()
		elif '/google' in self.query:
			tts=gTTS(text='membuka google, mohon tunggu!',lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}membuka google, mohon tunggu!')
			say()
			webbrowser.open('https://google.com')
		elif '/youtube' in self.query:
			bicara='membuka youtube, mohon tunggu!'
			tts=gTTS(text=bicara,lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
			webbrowser.open('https://youtube.com')
		elif '/facebook' in self.query:
                        bicara='membuka facebook, mohon tunggu!'
                        tts=gTTS(text=bicara,lang='id')
                        tts.save(filesave)
                        print(f'{lc}computer: {lw}'+bicara)
                        say()
                        webbrowser.open('https://facebook.com')
		elif '/say' in self.query:
			bicara=self.query.replace('/say ','')
			tts=gTTS(text=bicara,lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		elif '/help' in self.query:
			bicara=("""saya hanya mengerti command ini:
\t/wiki\t\t untuk mencari di wikipedia
\t/google\t\t untuk membuka google
\t/youtube\t untuk membuka youtube
\t/facebook\t untuk membuka facebook

\t/say\t\t untuk mengucapkan suatu query
\t/exit\t\t untuk keluar dari program
\t/help\t\t untuk menampilkan help ini""")
			tts=gTTS(text=bicara,lang='id')
			tts.save(filesave)
			print(f'{lc}computer: {lw}'+bicara)
			say()
		else: warm()
		
def say():
	sp.call('mpv '+filesave, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

def warm():
	bicara="maaf, saya tidak mengerti command anda, silahkan ketik /help"
	tts=gTTS(text=bicara,lang='id')
	tts.save(filesave)
	print(f'{lc}computer: {lw}'+bicara)
	say()

if __name__=='__main__':
	try:
		run=main(None,None)
		run.salam()
		while True:
			try:
				cmd=input(f'{lg}command: {lw}')
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
