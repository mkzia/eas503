import json

data = [
	{
		'student_name': 'John Doe',
		'major': 'Math'
	},
	{
		'student_name': 'Jane Doe',
		'major': 'Chemistry'
	},

]

filename = 'test.json'

## Save data
with open(filename, 'w') as file:
    json.dump(data, file, sort_keys=True, indent=2, separators=(',', ': '), ensure_ascii=False)


## read the json file
with open(filename, 'r') as file:
        data_reloaded = json.load(file)

print(data)

print(data_reloaded)