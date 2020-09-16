import requests as req
res = req.get( "https://www.google.com" )
print( res.text )