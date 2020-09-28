import json

favorit_tracks = [
	{'name': 'Вечная любовь', 'artist': 'Агата кристи'},
	{'name': 'Angel', 'artist': 'Massive Attack'},
	{'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding = 'utf-8') as f:
	json.dump(favorit_tracks, f)

print('Выполнено')

