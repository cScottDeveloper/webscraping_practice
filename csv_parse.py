from bs4 import BeautifulSoup as bs
import requests
# an array of url's we are gonna check
targets = []
sitemaps = []
careers = []
urls = []

# go thru the member data line by line and get all the urls
with open( 'members.csv', 'r' ) as f:
    for line in f:
        # turns a line of the csv into an array
        # "a,b,c" becomes [a, b, c]
        member = line.split( ',' )
        # checks if Robots.txt is listed as existing for a url
        if 'True' in member[2]:
            # each target is ( member_name, member_site )
            targets.append( ( member[0], member[1] ) )


for target in targets:
    try:
        res = requests.get( target[1] + '/robots.txt' )
    except:
        continue
    soup = bs(res.text, 'lxml')
    text = soup.get_text()
    text = text.split('\n')
    for t in text:
        if 'sitemap' in t:
            t = t.strip("Sitemap: ")
            sitemaps.append(t)
            break

for sitemap in sitemaps:
    try:
        res = requests.get(sitemap)
        soup = bs(res.text, 'lxml')
        text = soup.get_text()
        text = text.split('\n')
        for t in text:
            if "http" in t:
                urls.append[t]
                for url in urls:
                    if 'career' or 'job' in url:
                        careers.append[url]
                        print(careers)
                try:
                    new_res = requests.get(t)
                    soup2 = bs(res.text, 'lxml')
                    text2 = soup.get_text()
                    text2 = text2.split('\n')
                except:
                    continue
    except:
        continue

