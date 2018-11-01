import os



def num1():
	responce = os.system("clear")
	searchQuery = raw_input('Please input a search query: ')
	searchQueryConf = raw_input("Are you sure you want to search for " + '"'+ searchQuery + '"' + ' [y/n]'.lower())
	if searchQueryConf == 'y':
		responce = os.system("clear")
		responce = os.system("grep -i " + searchQuery + " *")
def num2():
	responce = os.system("clear")