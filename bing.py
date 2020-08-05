import os,re,requests
from colorama import Fore,init
from multiprocessing.dummy import Pool

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


def clean():
	lines_seen = set()
	outfile = open('sites.txt', "a")
	infile = open('sitelist.txt', "r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	infile.close()
	if os.name == "nt":
		os.system("del sitelist.txt")
	else:
		os.system("rm -rf sitelist.txt")
	print("[{}+{}] Duplicate sites removed successfully!".format(settings.r,settings.y))
	print("\n[{}+{}] Sites saved as {}sites.txt{}!".format(settings.r,settings.y,settings.b,settings.y))


binglist = {"http://www.bing.com/search?q=&count=50&first=1",
"http://www.bing.com/search?q=&count=50&first=51",
"http://www.bing.com/search?q=&count=50&first=101",
"http://www.bing.com/search?q=&count=50&first=151",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com/search?q=&count=50&first=251",
"http://www.bing.com/search?q=&count=50&first=301",
"http://www.bing.com/search?q=&count=50&first=351",
"http://www.bing.com/search?q=&count=50&first=401",
"http://www.bing.com/search?q=&count=50&first=451",
"http://www.bing.com/search?q=&count=50&first=501",
"http://www.bing.com/search?q=&count=50&first=551",
"http://www.bing.com/search?q=&count=50&first=601",
"http://www.bing.com/search?q=&count=50&first=651",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.vn/search?q=&count=50&first=101"}


def dorkscan(dork):
	for bing in binglist:
		bingg = bing.replace("&count",dork + "&count")
		try:
			r = requests.get(bingg)
			checktext = r.text
			checktext = checktext.replace("<strong>","")
			checktext = checktext.replace("</strong>","")
			checktext = checktext.replace('<span dir="ltr">','')
			checksites = re.findall('<cite>(.*?)</cite>',checktext)
			for sites in checksites:
				sites = sites.replace("http://","protocol1")
				sites = sites.replace("https://","protocol2")
				sites = sites + "/"
				site = sites[:sites.find("/")+0]
				site = site.replace("protocol1","http://")
				site = site.replace("protocol2","https://")
				if "http" in site:
					print(site + "/")
				else:
					print("http://" + site + "/")
				try:
					with open("sitelist.txt","a") as f:
						if "http" in site:
							f.write(site + "/" + "\n")
						else:
							f.write("http://" + site + "/" + "\n")
				except:
					pass
		except:
			pass


print("""{}
8888    888                                 888                MrAdu3l 8888888b.  
88888   888                                 888                  888   888  "Y88b 
S_ID99  888                                 888                  888   888    888  
MrAdu3l 888 888  888  .Yups.  MrRa3s.   .S_ID99  .d88b.  MrRa3ss 888   888    888 
888 8888888 888  888 d8P  Y8b 888 "88b d88" 888 d8P  Y8b 888P"   888   888    888 
888  MrRa3s 888  888 S_ID9999 888  888 888  888 88888888 888     888   888    888 
888   Y8888 Y88b 888 Y8b.     888  888 Y88b 888 Y8b.     888     888   888  .d88P 
888    Y888  "MrRa3s  "Y8888  888  888  "S_ID99  "Yupss  888   MrAdu3l 8888888P"  
                 888                                                              
            Y8b d88P                                                              
             "Yups"   For Reverse IP From Bing EXAMPLE: [{}+{}]ip:"8.8.8.8"[{}+{}] 
                     
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

dorklist = raw_input("[{}*{}] Dorklist : ".format(settings.r,settings.y))

try:
	dorks = open(dorklist, 'r').read().splitlines()
	print("[{}+{}] Scan started! Please wait... :)".format(settings.r,settings.y))
	pp = Pool(10)
	pr = pp.map(dorkscan,dorks)
except:
	print("[{}-{}] Dorklist not found!".format(settings.r,settings.y))
