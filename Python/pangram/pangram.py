alphabet = "abcdefghijklmnopqrstuvqxyz"

def is_pangram(sentence):
	
	sentence = sentence.lower()
	
	for letter in alphabet:
		if letter not in sentence:
			return False
	return True
  