#movie class defines the properties of a movie.
#Instance of movie class is created for each movie and is fed to fresh_tomatoes.open_movies_page().
class movie:
	#This is a constructor. It is called automatically whenever an instance of the class is created.
	#Parameters for each property is passed while instantiating.
	def __init__(self,title, box_image, trailer_url,movie_id_par):
		self.title= title
		self.poster_image_url=box_image
		self.trailer_youtube_url=trailer_url
		self.movie_id=movie_id_par
