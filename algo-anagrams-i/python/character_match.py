# Don't forget to run your tests!

def is_character_match(string1, string2):
	# Your code here
	string1_list = list(string1.replace(" ", "").upper())
	string2_list = list(string2.replace(" ", "").upper())
	for x in string1_list:
		for i, y in enumerate(string2_list):
			if x == y:
				string2_list.pop(i)
				break
	return not string2_list
