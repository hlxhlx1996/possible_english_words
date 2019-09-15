# Word Anagram

# Requirements

# Input: a set of input characters, ranging from a-z, case-insensitive.
# Output: all the possible English words from the dictionary that could be composed of these characters, 
# case-insensitive. Note that each of these characters can only be used once. 
# The possible English words could be fetched from, for example,  
# https://raw.githubusercontent.com/lad/words/master/words which is a copy of /usr/share/dict/words.
# Ensure the main program can be run in https://coderpad.io/

# Deliverable

# Submit your code to github.com and email us the link of your code repo, where the repo contains the following.
# One source code file for the main program.
# One runme.sh bash script to (compile and) run the program on Linux or Mac terminal.
# [Optional] one README file with additional instructions, if needed.
# [Bonus] one additional file with test cases.

# How to test

# git clone git clone https://github.com/username/xyz.git
# cd xyz && ./runme.sh

def run():
	print('Enter some characters, and press "Enter".')
	req = str(input())
	print('\nYou entered:', req)

	dic = getDictionary()
	wordlist = getWordList(dic, req)

	print('\nHere are all the possible English words with those letters:\n')
	for word in wordlist:
		print(word, end = '')

def getDictionary():
	dic_file = open('/usr/share/dict/words', 'r')
	dic = dic_file.readlines()
	dic_file.close()
	return dic

def getWordList(dic, chars):
	char_list = list(chars)
	wordlist = []
	for word in dic:
		if len(word) > len(char_list): # every character can be used only once
			continue
		temp_list = char_list.copy()
		for c in word.lower():
			if c in temp_list:
				temp_list.remove(c)
			else:
				break

		if len(char_list) - len(temp_list) == len(word) - 1:
			wordlist.append(word)

	return wordlist


run()
