import math
import re
import os
import requests as req
from os.path import join, dirname
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

#i = Input(2020, 7).getData()
inputCachePath = join(dirname(__file__), './')
cacheFile = open(join(inputCachePath, 'example.txt'), '+r')
i = cacheFile.read()
i = i.split("\n")
i = ",".join(i)


def PartOne(info):
	info = strToArr(info)
	#info = newlineParse(info)
	
	sa = []
	res = []
	
	for i in info:
		sa.append(i.split("contain"))

	pa = []
	tempPa = []
	for s in sa:
		if(len(s) < 2):
			tempPa.append(s[0])
		else:
			pa.append(tempPa)
			tempPa = []
			tempPa.append(s[0])
			tempPa.append(s[1])
			
	pa.append(tempPa)
			
	containsShiny = []
	tempActive = ""
	for a in pa:
		for o in a:
			if(tempActive == ""):
				tempActive = o
			else:
				r = re.findall(r"shiny gold", o)
				if(len(r) > 0):
					nTempActive = tempActive[::-1][2::][::-1]
					containsShiny.append(nTempActive)
		tempActive = ""
	
	tempActive2 = ""
	c = False
	for _ in range(0, 6):
		for a in pa:
			for o in a:
				if(tempActive2 == ""):
					tempActive2 = o
				else:
					
					for p in containsShiny:
						r = re.findall(rf"{p}", o)
						if(len(r) > 0):
							c = True
					
					if(c == True):	
						nTempActive2 = tempActive2[::-1][2::][::-1]
						containsShiny.append(nTempActive2)
					c = False
				[res.append(x) for x in containsShiny if x not in res] 
			tempActive2 = ""
			
	print(len(res))
	print(res)

			
	return len(res)


def PartTwo(info):
	info = strToArr(info)
	
	sa = []
	res = []
	
	for i in info:
		sa.append(i.split("contain"))

	pa = []
	tempPa = []
	for s in sa:
		if(len(s) < 2):
			tempPa.append(s[0])
		else:
			pa.append(tempPa)
			tempPa = []
			tempPa.append(s[0])
			tempPa.append(s[1])
			
	pa.append(tempPa)
			

				
	
	containsShiny = []
	res = []

	while len(containsShiny) > 0:
		for a in pa:
			for o in a:
				r = re.findall(r"shiny gold bags ", o)
				if(len(r) > 0):
					print(a)
				#if(len(r) > 0):
				#	print(r)
				#	r[1] = r[1][::-1][3::][::-1]
				#	containsShiny.append(r[1])
			#[res.append(x) for x in containsShiny if x not in res] 
			
		
		
			
	return containsShiny


#print(i)
#print(PartOne(i))
print(PartTwo(i))
