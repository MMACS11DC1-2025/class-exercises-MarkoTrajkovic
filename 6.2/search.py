file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []
dance_scores = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])
		dance_scores.append([danceability])




for i in range(len(dance_scores)):
	biggest_score = dance_scores[i]
	biggest_index = i
	for j in range(i+1, len(dance_scores)):
		if dance_scores[j] > biggest_score:
			biggest_score = dance_scores[j]
			biggest_index = j
	dance_scores[biggest_index], dance_scores[i] = dance_scores[i], dance_scores[biggest_index]



print("Dance score \tSong")
for item in dance_scores[:5]:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])
