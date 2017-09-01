import csv
import collections
from datetime import datetime
path = "C:\Users\The PC\Dropbox\musicalproject\music\kermitnirmit.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
data = []
for row in reader:
    date = datetime.strptime(row[3], '%d %b %Y %H:%M')
    title = (row[2])
    artist = (row[0])
    album = (row[1])
data.append([artist, album, title, date])
file = open(returns_path, 'w')
writer = csv.writer(file)
write
