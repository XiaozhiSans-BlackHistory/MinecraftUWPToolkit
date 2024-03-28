import ttkbootstrap as ttk
import tkinter.messagebox as tkmb
from tkinter import font
import time,datetime,os,platform
from logger import Logger
from crack import crackMCUWP
import webbrowser as url

logprint = Logger().logger
logprint.debug("Initializing app...")

# App Info
appName = "Minecraft UWP Toolkit"
appShortName = "MCUWPTK"
appNameLog =' [' + appShortName + '] '
version = "v0.1-alpha"
license = "MIT License"
author = "XiaozhiSans"
copyright = "Copyright (c) 2024 XiaozhiSans. All rights reservered."
logprint.debug("got App Info: " + appName + "by" + author)
logprint.debug("checking System Info...")

# Sys Info
userName = os.getlogin()

machineValue = platform.machine()
sysX = "unknown (" + machineValue + ')'
if machineValue == "i386":
	sysX = "X86 (i386)"
if machineValue == "x86":
	sysX = "X86"
if machineValue == "AMD64":
	sysX = "X64 (AMD64)"
if machineValue == "x86_64":
	sysX = "X64 (x86_64)"
logprint.debug("got system architecture: " + sysX)

isWindows = False
isLinux = False
isJava = False
isOther = False
sysType = platform.system()
if sysType == "Windows":
	isWindows = True
else:
	if sysType == "Linux":
		isLinux = True
	else:
		if sysType == "Java":
			isJava = True
		else:
			isOther = True

sysInfo =sysType + ' ' + platform.version() + ' '
if isWindows:
	sysInfo += (platform.win32_edition() + ' ')
sysInfo += sysX
logprint.debug("got System Info: " + sysInfo)

logprint.debug("starting mainApp...")
class mainApp(ttk.Window):
	def __init__(self):
		super().__init__()
		logprint.info(appNameLog + "+.+ Toolkit started. Version: " + version)
		self.title(appName)
		#self.geometry("400x400")
		self.resizable(False, False)
		theme = ttk.Style("darkly")

		# Load Main Labels
		self.MCUWPTK_label = ttk.Label(
			self,
			text="Minecraft UWP Toolkit " + version,
			bootstyle="inverse-info"
			)
		self.MCUWPTK_label.grid(row=0, column=0)

		self.time_label = ttk.Label(
			self,
			text="",
			bootstyle="inverse-primary"
			)
		self.time_label.grid(row=0, column=4)

		self.date_label = ttk.Label(
			self,
			text="",
			bootstyle="inverse-secondary"
			)
		self.date_label.grid(row=1, column=4)

		self.welcome_label = ttk.Label(
			self,
			text=": ) Welcome, " + userName,
			bootstyle="info"
			)
		self.welcome_label.grid(row=0, column=1)

		self.sysInfo_label = ttk.Label(
			self,
			text="System Info: " + sysInfo
			)
		self.sysInfo_label.grid(row=1, column=0, columnspan=2)

		self.warning_label = ttk.Label(
			self,
			text="",
			bootstyle="warning"
			)
		self.warning_label.grid(row=3, column=0)

		if (machineValue!="AMD64")and(machineValue!="x86_64"):
			self.warning_label.config(text="; ( Due to the unsupported architecture of your system,\nsome features may not work properly.")
			logprint.warning(appNameLog + "x.x Warning: unsupported system architecture.")

		# Load Main Btns
		self.crackBtn = ttk.Button(
			self,
			text="Crack Minecraft",
			command=crackMCUWP,
			bootstyle="primary"
			)
		self.crackBtn.grid(row=4, column=0, padx=10, pady=10, ipadx=20)

		self.cloneBtn = ttk.Button(
			self,
			text="Clone Minecraft",
			command=self.cloneMC,
			bootstyle="outline-primary"
			)
		self.cloneBtn.grid(row=5, column=0, padx=10, pady=2, ipadx=20)

		self.startBtn = ttk.Button(
			self,
			text="Start Minecraft",
			command=self.startMC,
			bootstyle="success"
			)
		self.startBtn.grid(row=4, column=1, padx=10, pady=2, ipadx=20)

		self.aboutBtn = ttk.Button(
			self,
			text="About",
			command=self.about,
			bootstyle="info"
			)
		self.aboutBtn.grid(row=8, column=4, padx=(20, 0), pady=(70, 0), ipadx=20)

		self.quitBtn = ttk.Button(
			self,
			text="Quit",
			command=self.destroy,
			bootstyle="danger"
			)
		self.quitBtn.grid(row=8, column=0, padx=(0, 105), pady=(70, 0), ipadx=20)

		self.after_id_time = None
		self.after_id_date = None

		self.update_time()
		self.update_date()

	# Load Main Fcts
	def about(self):
		tkmb.showinfo(title="About", message="App name: " + appName + "\nVersion: " + version + "\nLicense: " + license + "\nAuthor: " + author + '\n' + copyright)

	def startMC(self):
		os.system("explorer minecraft://")
		logprint.info(appNameLog + "+.+ Minecraft started.")

	def cloneMC(self):
		if tkmb.askyesno("-.-?", "this feature is still indev, but you can use Minecraft UWP Cloner.\nget more info about MCUWPC?"):
			url.open("https://github.com/XiaozhiSans/MinecraftUWPCloner")

	def update_time(self):
		current_time = time.strftime('%H:%M:%S')
		self.time_label.config(text=current_time)
		self.after_id_time = self.time_label.after(1000, self.update_time)

	def update_date(self):
		current_date = datetime.date.today().strftime('%Y/%m/%d')
		self.date_label.config(text=current_date)
		self.after_id_date = self.date_label.after(1000, self.update_date)

	def destroy(self):
		logprint.info(appNameLog + "-.- trying to exit program...")
		if tkmb.askyesno("-.-?", "are you sure want to quit?"):
			logprint.info(appNameLog + "-.- Program exits by " + userName)
			if self.after_id_time:
				self.time_label.after_cancel(self.after_id_time)
			if self.after_id_date:
				self.date_label.after_cancel(self.after_id_date)
			super().destroy()
		else:
			logprint.info(appNameLog + "-.-" + userName + " cancelled exit program")

if __name__ == "__main__":
	mainApp().mainloop()
