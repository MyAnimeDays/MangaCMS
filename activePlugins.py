

if __name__ == "__main__":

	import logSetup
	logSetup.initLogging()

import ScrapePlugins.BuMonitor.Run
import ScrapePlugins.DjMoeLoader.Run
import ScrapePlugins.DjMoeLoader.Retag
import ScrapePlugins.BtBaseManager.Run
import ScrapePlugins.PururinLoader.Run
import ScrapePlugins.JzLoader.Run

import ScrapePlugins.FakkuLoader.Run
import ScrapePlugins.McLoader.Run
import ScrapePlugins.CxLoader.Run
import ScrapePlugins.MjLoader.Run
import ScrapePlugins.WebtoonLoader.Run            # Yeah. There is webtoon.com. and WebtoonsReader.com. Confusing much?
import ScrapePlugins.WebtoonsReader.Run
import ScrapePlugins.KissLoader.Run
import ScrapePlugins.SadPandaLoader.Run
import ScrapePlugins.NHentaiLoader.Run
import ScrapePlugins.DynastyLoader.Run
import ScrapePlugins.HBrowseLoader.Run
import ScrapePlugins.Crunchyroll.Run
import ScrapePlugins.IrcGrabber.IrcEnqueueRun
import ScrapePlugins.IrcGrabber.BotRunner
import ScrapePlugins.Kawaii.Run
import ScrapePlugins.ZenonLoader.Run
import ScrapePlugins.MangaBox.Run
import ScrapePlugins.MangaHere.Run
import ScrapePlugins.YoMangaLoader.Run

import ScrapePlugins.FoolSlide.VortexLoader.Run
import ScrapePlugins.FoolSlide.RoseliaLoader.Run
import ScrapePlugins.FoolSlide.SenseLoader.Run
import ScrapePlugins.FoolSlide.ShoujoSenseLoader.Run
import ScrapePlugins.FoolSlide.TwistedHel.Run
import ScrapePlugins.FoolSlide.S2Loader.Run
import ScrapePlugins.FoolSlide.MangatopiaLoader.Run
import ScrapePlugins.SurasPlace.Run
import ScrapePlugins.GameOfScanlationLoader.Run


import ScrapePlugins.MangaMadokami.Run
import ScrapePlugins.BooksMadokami.Run

# Convenience functions to make intervals clearer.
def days(num):
	return 60*60*24*num
def hours(num):
	return 60*60*num
def minutes(num):
	return 60*num

# Plugins in this dictionary are the active plugins. Comment out a plugin to disable it.
# plugin keys specify when plugins will start, and cannot be duplicates.
# All they do is specify the order in which plugins
# are run, initially, starting after 1-minue*{key} intervals
scrapePlugins = {
	0  : (ScrapePlugins.BtBaseManager.Run,                   hours( 1)),
	2  : (ScrapePlugins.BuMonitor.Run,                       hours( 1)),

	3  : (ScrapePlugins.JzLoader.Run,                        hours( 8)),   # Every 8 hours, since I have to scrape a lot of pages, and it's not a high-volume source anyways
	4  : (ScrapePlugins.DjMoeLoader.Run,                     hours( 1)),
	5  : (ScrapePlugins.DjMoeLoader.Retag,                   hours( 1)),
	6  : (ScrapePlugins.McLoader.Run,                        hours(12)),  # every 12 hours, it's just a single scanlator site.
	8  : (ScrapePlugins.IrcGrabber.IrcEnqueueRun,            hours(12)),  # Queue up new items from IRC bots.
	9  : (ScrapePlugins.PururinLoader.Run,                   hours( 1)),
	10 : (ScrapePlugins.FakkuLoader.Run,                     hours( 1)),
	11 : (ScrapePlugins.CxLoader.Run,                        hours(12)),  # every 12 hours, it's just a single scanlator site.
	12 : (ScrapePlugins.MjLoader.Run,                        hours( 1)),
	13 : (ScrapePlugins.IrcGrabber.BotRunner,                hours( 1)),  # Irc bot never returns. It runs while the app is live. Rerun interval doesn't matter, as a result.
	15 : (ScrapePlugins.MangaHere.Run,                       hours(12)),
	16 : (ScrapePlugins.WebtoonLoader.Run,                   hours( 8)),
	17 : (ScrapePlugins.DynastyLoader.Run,                   hours( 8)),
	18 : (ScrapePlugins.HBrowseLoader.Run,                   hours( 1)),
	19 : (ScrapePlugins.KissLoader.Run,                      hours( 1)),
	20 : (ScrapePlugins.NHentaiLoader.Run,                   hours( 1)),
	21 : (ScrapePlugins.Crunchyroll.Run,                     hours( 6)),
	22 : (ScrapePlugins.SadPandaLoader.Run,                  hours( 2)),
	# 23 : (ScrapePlugins.WebtoonsReader.Run,                  hours( 6)),  # They claim they're planning on coming back. We'll see.
	25 : (ScrapePlugins.Kawaii.Run,                          hours(12)),
	26 : (ScrapePlugins.ZenonLoader.Run,                     hours(24)),
	27 : (ScrapePlugins.MangaBox.Run,                        hours(12)),
	28 : (ScrapePlugins.YoMangaLoader.Run,                   hours(12)),
	29 : (ScrapePlugins.GameOfScanlationLoader.Run,          hours(12)),

	# FoolSlide modules
	30 : (ScrapePlugins.FoolSlide.VortexLoader.Run,          hours(12)),
	31 : (ScrapePlugins.FoolSlide.RoseliaLoader.Run,         hours(12)),
	32 : (ScrapePlugins.FoolSlide.SenseLoader.Run,           hours(12)),
	33 : (ScrapePlugins.FoolSlide.ShoujoSenseLoader.Run,     hours(12)),
	34 : (ScrapePlugins.FoolSlide.TwistedHel.Run,            hours(12)),
	36 : (ScrapePlugins.FoolSlide.MangatopiaLoader.Run,      hours(12)),
	37 : (ScrapePlugins.SurasPlace.Run,                      hours(24)),
	38 : (ScrapePlugins.FoolSlide.S2Loader.Run,              hours(12)),

	40 : (ScrapePlugins.MangaMadokami.Run,                   hours(4)),
	41 : (ScrapePlugins.BooksMadokami.Run,                   hours(4)),

}


if __name__ == "__main__":

	# scrapePlugins = {
		# 0 : (TextScrape.BakaTsuki.Run,                       60*60*24*7),  # Every 7 days, because books is slow to update
		# 1 : (TextScrape.JapTem.Run,                          60*60*24*5),
		# 3 : (TextScrape.Guhehe.Run,                          60*60*24*5),
		# 2 : (TextScrape.ReTranslations.Run,                  60*60*24*1)   # There's not much to actually scrape here, and it's google, so I don't mind hitting their servers a bit.
	# }

	print("Test run!")
	import nameTools as nt

	def callGoOnClass(passedModule):
		print("Passed module = ", passedModule)
		print("Calling class = ", passedModule.Runner)
		instance = passedModule.Runner()
		instance.go()
		print("Instance:", instance)


	import signal
	import runStatus

	def signal_handler(dummy_signal, dummy_frame):
		if runStatus.run:
			runStatus.run = False
			print("Telling threads to stop (activePlugins)")
		else:
			print("Multiple keyboard interrupts. Raising")
			raise KeyboardInterrupt


	signal.signal(signal.SIGINT, signal_handler)
	import sys
	import traceback
	print("Starting")
	try:
		if len(sys.argv) > 1 and int(sys.argv[1]) in scrapePlugins:
			plugin, interval = scrapePlugins[int(sys.argv[1])]
			print(plugin, interval)
			callGoOnClass(plugin)
		else:
			print("Loopin!", scrapePlugins)
			for plugin, interval in scrapePlugins.values():
				print(plugin, interval)
				callGoOnClass(plugin)
	except:
		traceback.print_exc()


	print("Complete")

	nt.dirNameProxy.stop()
	sys.exit()
