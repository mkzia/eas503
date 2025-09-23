with open(filename) as file:
	line_count = 0
	word_count = 0
	char_count = 0
	for line in file:
		line = line.strip()
		line_count += 1
		word_count += len(line.split())
		for word in line.split():
			char_count += len(word)



