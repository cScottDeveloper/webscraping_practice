import requests as req
import lxml.html
import urllib.robotparser

class Member:
    def __init__( self, url ):
        self.url = url
        self.name = ''
        self.robots = 'False'
url = 'https://aiamnow.com/memberships/'
res = req.get( url )
member_sites = []
tree = lxml.html.fromstring( res.text )
for div in tree.cssselect('div.fl-photo-content'):
    try:
        site = div[0].attrib['href']
        if site[-1] == '/':
            site = site[:-1]
        member = Member( site )
        # parse the member name from the url
        name = ''
        if 'http://' in site:
            name = site[ len('http://') : ]
        else:
            name = site[ len('https://') : ] 
        if 'www.' in name:
            name = name[ len('www.') : ]
        name = name[ : name.find('.') ]
        member.name = name
        member_sites.append( member )
    except:
        continue
for m in member_sites:
    url = m.url + '/robots.txt'
    try:
        res = req.get( url )
    except:
        m.robots = 'False'
        continue
    if res.status_code == 200:
        m.robots = 'True'
with open( 'members.csv', 'w' ) as f:
    f.write( '{}, {}, {}\n'.format( 'member', 'url', 'robots.txt' ) )
    for m in member_sites:
        f.write( '{}, {}, {}\n'.format( m.name, m.url, m.robots ) )