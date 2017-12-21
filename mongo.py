#!/usr/local/bin/python3
import cgi
import cgitb
cgitb.enable()
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import pymongo

client = pymongo.MongoClient('mongodb://mp4060:********@class-mongodb.cims.nyu.edu/mp4060')

form = cgi.FieldStorage()

state = form["state"].value
sort = form["sort"].value 
quantity = form["quantity"].value 

print("Content-type: text/html;charset=utf-8")
print("\n\n") 

print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>PyMongo Program</title>
        <link rel="stylesheet" type="text/css" href="mongo.css" />
    </head>
    <body>
        <div class="container">
        	<h3>State Zip Codes</h3>
''')

for zip in client.mp4060.zips.find({"state":state}).sort(sort, pymongo.ASCENDING).limit(int(quantity)):

    id = zip.get('_id', 'Unknown Zip')
    city = zip.get('city', 'Unknown City')
    location = zip.get('loc', 'Unknown Location')
    population = zip.get('pop', 'Unknown Population')
    state = zip.get('state', 'Unknown State')

    #if population != 0:
    print('''

               	<p>{city}, {state}, {id}
               	<br />
              	 {location}
              	 <br />
              	 Population: {population}
             	  </p>
             	  <hr />

   	 '''.format(id=id, city=city, location=location, population=population, state=state))


#output the bottom of the HTML document
print('''
    
            <!-- clearfix -->
            <div class="clear"></div>
        </div>
    </body>
</html>
''')
