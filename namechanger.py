import os

def rename(clo,num):

	clo.append("_")
	clos = ''.join(clo)

	oldnames = os.listdir(os.getcwd())
	newlist=[]
	tags=[]

	for i in range(1,num+1):
		if i < 10:
			tags.extend((clos + "0" + str(i) + "_6-4" + ext,clos + "0" + str(i) + "_3-1" + ext))
		else:
			tags.extend((clos + str(i) + "_6-4" + ext,clos + str(i) + "_3-1" + ext))
			
	for files in oldnames:
		if files.endswith(ext):
			newlist.append(files)

	for i in range(len(tags)):
		os.rename(newlist[i], tags[i])
	
id = [input("Enter the CLO #: ")]
cards = int(input("Enter the number of cards: "))
ext = str(input("Enter the exact file extension (case-sensitive), e.g. '.JPG': "))

rename(id,cards)