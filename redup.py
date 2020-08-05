import os
from colorama import Fore,init

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


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
             "Yups"          [{}+{}] Duplicate Remover [{}+{}]
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

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
