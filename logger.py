import logging as log
import time,os

# App Info
appName = "Minecraft UWP Toolkit - Logger Module"
appShortName = "MCUWPTK-LOG"
appNameLog =' [' + appShortName + '] '
version = "v1.0"
license = "MIT License"
author = "XiaozhiSans"
copyright = "Copyright (c) 2024 XiaozhiSans. All rights reservered."

class Logger():
	def __init__(self):
		self.logger = log.getLogger("logger")
		self.logger.setLevel(log.INFO)

		sh = log.StreamHandler()

		log_file = os.path.join("mcuwptk.log")
		fh = log.FileHandler(log_file, encoding="utf-8")

		formator = log.Formatter(
			fmt = "%(asctime)s(%(filename)s)-%(levelname)s: %(message)s",
			datefmt="[%Y/%m/%d %X]"
			)
		sh.setFormatter(formator)
		fh.setFormatter(formator)

		self.logger.addHandler(sh)
		self.logger.addHandler(fh)

		logprint = self.logger
		logprint.debug("Logger has been initialized.")
