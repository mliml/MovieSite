import time
import web
import urllib
from PIL import Image 

def get_poster(id,url):
	file_name_old = 'static/poster/%d.jpg' %id
	file_name = 'static/poster2/%d.jpg' %id
	pic = Image.open(file_name_old)
	new_pic = pic.resize((300, 430), Image.BILINEAR)
	new_pic.save(file_name)


db = web.database(dbn='sqlite',db='MovieSite.db')
movies = db.select('movie')
count = 0
for movie in movies:
	get_poster(movie.id,movie.image)
	count += 1
	print count, movie.id
	time.sleep(1)