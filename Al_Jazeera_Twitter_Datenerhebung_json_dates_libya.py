import json

f = open('ajenglish_Arabien.json')
data = json.load(f)
l = []
for d in data:
	if 'libya' in d['text'].lower():
		l.append(d)

dates = []
for d in l:
	dates.append(d['created_at'])

with open('dates.txt', 'w') as f:
	for d in dates:
		f.write('%s\n' %d)
