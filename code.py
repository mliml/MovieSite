import web
from web import form

urls = (
	'/','index',
	'/movie/(\d+)','movie',
	'/card','card',
)

  
render = web.template.render('templates/',base='layout')
db = web.database(dbn='sqlite',db='MovieSite.db')



class index:
	def GET(self):
		movies = db.select('movie')
		return render.index(movies)
	def POST(self):
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie',where=condition)
		return render.index(movies)

class movie:
	def GET(self,movie_id):
		movie_id = int(movie_id)
		movie = db.select('movie',where='id=$movie_id',vars=locals())[0]
		return render.movie(movie)

class card:
	def GET(self):
		movies = db.select('movie')
		return render.card(movies)
	def POST(self):
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie',where=condition)
		return render.card(movies)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()