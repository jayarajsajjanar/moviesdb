import media
import fresh_tomatoes

The_Shawshank_Redemption    = media.movie("Shawshank Redemption",
											"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
											"https://www.youtube.com/watch?v=6hB3S9bIaco")
											
The_Godfather				= media.movie("The Godfather",
											"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
											"https://www.youtube.com/watch?v=sY1S34973zA")

The_Godfather_Part_II       = media.movie("The Godfather Part ii",
											"https://upload.wikimedia.org/wikipedia/en/0/03/Godfather_part_ii.jpg",
											"https://www.youtube.com/watch?v=qJr92K_hKl0")

The_Dark_Knight  			= media.movie("The Dark Knight",
											"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
											"https://www.youtube.com/watch?v=EXeTwQWrcwY")

Pulp_Fiction 				= media.movie("Pulp Fiction",
											"https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
											"https://www.youtube.com/watch?v=s7EdQ4FqbhY")

Angry_Men					= media.movie("12 Angry Men",
											"http://t0.gstatic.com/images?q=tbn:ANd9GcTDnld_1CpP-iESMfN_iAF0yEOYAhv0gX7F3RKIf47oQIua_vAS",
											"https://www.youtube.com/watch?v=fSG38tk6TpI")
											
movies_list=[The_Shawshank_Redemption,The_Godfather, The_Godfather_Part_II, The_Dark_Knight,Pulp_Fiction,Angry_Men  ]


fresh_tomatoes.open_movies_page(movies_list)