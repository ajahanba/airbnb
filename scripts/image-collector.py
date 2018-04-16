import csv
import urllib
import shutil
import os.path
import requests


with open('NY_listings.csv', 'rb') as f:
        reader = csv.reader(f)
    next(reader)
    for row in reader:
             id=row[0]
     url = row[14]
     c = row[30]
     print c
     if (c is '1') :
               if os.path.exists("NY_images/"+id): continue
      if not url: continue
      print id
      response = requests.get(url, stream=True)
      with open("Chicago_2015_images/"+id, 'wb') as out_file:
                 shutil.copyfileobj(response.raw, out_file)
      del response
