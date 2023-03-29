import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
	data = json.load(read_file)
stops = {}
tramlines = {}

for line in data['linia']:
	tramlines[line['name']] = []
	if 'przystanek' in line:
		for stop in line['przystanek']:
			tramlines[line['name']].append(stop['name'][:-3])
			stops[stop['name'][:-3]] = True
		
with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(tramlines, file, ensure_ascii = False)



sorted_lines = sorted(tramlines, key = lambda k: len(tramlines[k]), reverse=True)
print ("Liczba przystankow w poszczegolnych liniach: ")
for line in sorted_lines:
    print("Linia " + line + ": " + str(len(tramlines[line])) + " przystankow")

print("\n\nObslugiwane przystanki:")
for i in stops:
	print(i)
