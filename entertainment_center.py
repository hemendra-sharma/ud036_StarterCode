"""This file generates a list of movies and passes that to 
fresh_tomatoes's 'open_movies_page' method."""

import media
import fresh_tomatoes

movies_list = [] # list of movies

# Now we will append the "movies_list" with several "Movie" instances...

# Justice League
movies_list += [media.Movie("Justice League",
		"Fueled by his restored faith in humanity and inspired by Superman's "
			"(Henry Cavill) selfless act, Bruce Wayne (Ben Affleck) enlists "
			"newfound ally Diana Prince to face an even greater threat.",
		"https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
		"https://www.youtube.com/watch?v=DblEwHkde8U")]

#Kingsman
movies_list += [media.Movie("Kingsman 2",
		"With their headquarters destroyed and the world held hostage, "
			"members of Kingsman find new allies when they discover a spy "
			"organization in the United States known as Statesman.",
		"https://upload.wikimedia.org/wikipedia/en/f/fb/Kingsman_The_Golden_Circle.png",
		"https://www.youtube.com/watch?v=0WmUbiMHeSE")]

# Avengers
movies_list += [media.Movie("Avengers",
		"S.H.I.E.L.D. leader Nick Fury is compelled to launch the "
			"'Avengers Initiative' when Loki poses a threat to planet Earth.",
		"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
		"https://www.youtube.com/watch?v=eOrNdBpGMv8")]

# Thor Ragnarok
movies_list += [media.Movie("Thor Ragnarok",
		"Imprisoned on the other side of the universe, the mighty Thor finds "
			"himself in a deadly gladiatorial contest that pits him against "
			"the Hulk, his former ally and fellow Avenger. ",
		"https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
		"https://www.youtube.com/watch?v=ue80QwXMRHg")]

# Spiderman Homecoming
movies_list += [media.Movie("Spiderman Homecoming",
		"Thrilled by his experience with the Avengers, young Peter Parker "
			"returns home to live with his Aunt May.",
		"https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
		"https://www.youtube.com/watch?v=DiTECkLZ8HM")]

# Annabelle
movies_list += [media.Movie("Annabelle",
		"Former toy maker Sam Mullins and his wife, Esther, are happy to welcome "
			+ "a nun and six orphaned girls into their California farmhouse.",
		"https://upload.wikimedia.org/wikipedia/en/9/9b/Annabelle-poster.jpg",
		"https://www.youtube.com/watch?v=paFgQNPGlsg")]

# call the method to generate and open the HTML file using movies_list
fresh_tomatoes.open_movies_page(movies_list)