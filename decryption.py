def replace_letters(mapped_msg, orig_alphabet, keyed_alphabet):
	# the keyed alphabet appears to be a rearrangement of the original alphabet
	# so it makes sense to try substituting the letters of the keyed alphabet with those in the original alphabet
	letter_subst = {}
	for i in range(len(orig_alphabet)):
		letter_subst[keyed_alphabet[i]] = orig_alphabet[i]

	tokens = mapped_msg.split()
	# the decoded message turns out to have undergone 2 rounds of substitutions in this manner
	# (discovered through trial and error) 
	for j in range(2):
		decoded = ''
		for t in tokens:
			for c in t:
				decoded += letter_subst[c]
			decoded += ' '
			tokens = decoded.split()
	return decoded

def map_to_letters(tokens, keyed_alphabet):
	# if the message is broken up into pairs of 2 digits, each pair corresponds to a letter 
	# since the min and max pairs are within the range 0-25
	# hence, start by matching each digit pair to its corresponding letter in the keyed alphabet
	mapped = ''
	for t in tokens:
		for i in range(0, len(t), 2):
			pos = int(t[i:i+2])
			mapped += keyed_alphabet[pos]
		mapped += ' '
	return mapped

def decode():
	message = '012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119'
	keyed_alphabet = 'BHISOECRTMGWYVALUZDNFJKPQX'
	orig_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	tokens = message.split()
	mapped_msg = map_to_letters(tokens, keyed_alphabet)
	decoded_msg = replace_letters(mapped_msg, orig_alphabet, keyed_alphabet)
	print decoded_msg


if __name__ == '__main__':
	decode()

# def rotate_string(string):
# 	variants = []
# 	for i in range(len(string)):
# 		var = string[i:] + string[:i]
# 		variants.append(var)
# 	return variants

# def get_freqs(message):
# 	d = {}
# 	tokens = message.split()
# 	for t in tokens:
# 		for i in range(0, len(t), 2):
# 			key = t[i:i+2]
# 			if d.get(key):
# 				d[key] += 1
# 			else:
# 				d[key] = 1
# 	return d

# def freq_corr(freqs):
# 	corr = {}
# 	rankings = 'etaoinshrdlucmwfygpbvkxjqz'
# 	items = sorted([ (item[1], item[0]) for item in freqs.items() ], reverse=True)
# 	for idx, item in enumerate(items):
# 		corr[item[1]] = rankings[idx]
# 	return corr