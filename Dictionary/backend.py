import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
	w = w.lower()
	close = get_close_matches(w, data.keys())

	if w in data:
		return data[w]

	elif w.title() in data:
		return data[w.title()]

	elif w.upper() in data:
		return data[w.upper()]

	elif len(close) > 0:
	# 	yn = input("Did you mean %s instead? (y/n)" %(close[0]))
		return "Did you mean '%s' instead?" %(close[0])

		# if yn == 'y' or yn == 'Y':
		# 	return data[close[0]]
			
	# 	elif yn == 'n' or yn == 'N':
	# 		return "The word doesn't exist. Please double-check it!"
		
	# 	else:
	# 		return "Couldn't get your entry :("

	else:
		return "The word doesn't exist.\nPlease double-check it!"