import os,platform,re
import tkinter.messagebox as tkmb
from logger import Logger

logprint = Logger().logger

# App Info
appName = "Minecraft UWP Toolkit - Crack Module"
appShortName = "MCUWPTK-CRACK"
appNameLog =' [' + appShortName + '] '
version = "v1.0"
license = "MIT License"
author = "XiaozhiSans"
copyright = "Copyright (c) 2024 XiaozhiSans. All rights reservered."

class crackMCUWP():
	def __init__(self):
		if tkmb.askyesno(">.<", "are you sure want to crack Minecraft Trial (UWP)?\n u.u tip: pls make sure the toolkit is running as admin."):
			sysVer = self.checkSys()
			if sysVer==-1:
				tkmb.showerror("x.x", "unsupported system or system version!!")
				logprint.error(appNameLog + "x.x unsupported system or system version!!")
				return -1
			logprint.info(appNameLog + "u.u system is " + sysVer)
			# according to system version select patch file
			fileName = sysVer + ".7z"
			result = os.system("crack\\nsudo -u=s -p=e 7z e -y -o%windir% " + fileName)
			if result == 0:
				tkmb.showinfo(title = "+.+", message = "Minecraft Trial (UWP) has been cracked.\n ~(￣▽￣)~ enjoy!")
				logprint.info(appNameLog + "+.+ Minecraft Trial (UWP) has been cracked.")
				return 0
			else:
				retry = tkmb.askretrycancel("x.x", "Minecraft Trial (UWP) has not cracked.\ndo you want retry?\n -.-; tip: try to run the toolkit as admin?")
				logprint.warning(appNameLog + "x.x Minecraft Trial (UWP) crack filed. -.-; maybe the permissions aren't enough?")
				if retry == True: crackMCUWP()
				else: return 1
		else: logprint.info(appNameLog + "-.-; user cancelled crack.")

	def checkSys(self):
		logprint.info(appNameLog + "checking system version...")
		sysVer=platform.version()
		pattern = r'\d+\.\d+'
		match = re.search(pattern, sysVer)
		if match:
			sysVer = match.group()
			sysVer = float(sysVer)
		if (sysVer >= 12.0)and(sysVer < 12.9): return "win11"
		if (sysVer >= 10.0)and(sysVer < 10.9): return "win10"
		else: return -1
