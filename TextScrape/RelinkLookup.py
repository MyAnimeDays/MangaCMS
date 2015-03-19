


import runStatus
runStatus.preloadDicts = False

# import Levenshtein as lv

import urllib.parse
import os
import os.path
from importlib.machinery import SourceFileLoader


########################################################################################################################
#
#	#### ##     ## ########   #######  ########  ########    ##        #######   #######  ##    ## ##     ## ########
#	 ##  ###   ### ##     ## ##     ## ##     ##    ##       ##       ##     ## ##     ## ##   ##  ##     ## ##     ##
#	 ##  #### #### ##     ## ##     ## ##     ##    ##       ##       ##     ## ##     ## ##  ##   ##     ## ##     ##
#	 ##  ## ### ## ########  ##     ## ########     ##       ##       ##     ## ##     ## #####    ##     ## ########
#	 ##  ##     ## ##        ##     ## ##   ##      ##       ##       ##     ## ##     ## ##  ##   ##     ## ##
#	 ##  ##     ## ##        ##     ## ##    ##     ##       ##       ##     ## ##     ## ##   ##  ##     ## ##
#	#### ##     ## ##         #######  ##     ##    ##       ########  #######   #######  ##    ##  #######  ##
#
########################################################################################################################


def getPythonScriptModules():
	moduleDir = os.path.split(os.path.realpath(__file__))[0]


	ret = []
	moduleRoot = 'TextScrape'
	for fName in os.listdir(moduleDir):
		itemPath = os.path.join(moduleDir, fName)
		if os.path.isdir(itemPath):
			modulePath = "%s.%s" % (moduleRoot, fName)
			for fName in os.listdir(itemPath):

				# Skip files without a '.py' extension
				if not fName == "Scrape.py":
					continue

				fPath = os.path.join(itemPath, fName)
				fName = fName.split(".")[0]
				fqModuleName = "%s.%s" % (modulePath, fName)
				# Skip the __init__.py file.
				if fName == "__init__":
					continue

				ret.append((fPath, fqModuleName))

	return ret

def findPluginClass(module, prefix):

	interfaces = []
	for item in dir(module):
		if not item.startswith(prefix):
			continue

		plugClass = getattr(module, item)
		if not "plugin_type" in dir(plugClass) and plugClass.plugin_type == "TextScraper":
			continue
		if not 'tableKey' in dir(plugClass):
			continue

		interfaces.append((plugClass.tableKey, plugClass))

	return interfaces

def loadPlugins():
	modules = getPythonScriptModules()
	ret = {}

	for fPath, modName in modules:
		loader = SourceFileLoader(modName, fPath)
		mod = loader.load_module()
		plugClasses = findPluginClass(mod, 'Scrape')
		for key, pClass in plugClasses:
			if key in ret:
				raise ValueError("Two plugins providing an interface with the same name? Name: '%s'" % key)
			ret[key] = pClass
	return ret


def fetchRelinkableDomains():
	domains = set()
	pluginDict = loadPlugins()
	for plugin in pluginDict:
		plg = pluginDict[plugin]

		if isinstance(plg.baseUrl, (set, list)):
			for url in plg.baseUrl:
				url = urllib.parse.urlsplit(url.lower()).netloc
				domains.add(url)

				if url.startswith("www."):
					domains.add(url[4:])

		else:
			url = urllib.parse.urlsplit(plg.baseUrl.lower()).netloc

		domains.add(url)
		if url.startswith("www."):
			domains.add(url[4:])
		if hasattr(plg, 'scannedDomains'):
			for domain in plg.scannedDomains:
				url = urllib.parse.urlsplit(domain.lower()).netloc

				domains.add(url)
				if url.startswith("www."):
					domains.add(url[4:])

	return domains


RELINKABLE = fetchRelinkableDomains()
