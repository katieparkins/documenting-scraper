###import library urllib2 and Beautiful Soup from bs4
import urllib2, csv
from bs4 import BeautifulSoup

###creating file outfile from jail data
outfile = open('jaildata.csv', 'w')

###creating writer that knows how to interact with outfile
writer = csv.writer(outfile)

###defining which url we're pulling data from 
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
###having library we imported read the url we defined for data
html = urllib2.urlopen(url).read()

###make "soup" dig through html??
soup = BeautifulSoup(html, "html.parser")

###identifying the body of text we want to pull data from
tbody = soup.find('tbody', {'class': 'stripe'})

###identifying which rows we want to pull data from
rows = tbody.find_all('tr')

###creating loop to pull data
for row in rows:

    cells = row.find_all('td') ###identifying which cells in rows we want to pull data from

###create empty list to put data we're scraping into
    data = []
    for cell in cells:
        data.append(cell.text.encode('utf-8'))

    writer.writerow(data)