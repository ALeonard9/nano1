import media
import fresh_tomatoes

# ************Movies*******************
toy_story = media.Movie("Toy Story",
 "Toys that come to life",
 "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 "https://www.youtube.com/watch?v=KYz2wyBy3kc",
 "123")

avatar = media.Movie("Avatar",
"Aliens + Dances with Wolves",
"http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
"www.youtube.com/watch?v=cRdxXPV9GNQ",
"2020")

saw = media.Movie("Saw",
"Can you believe that ending?",
"http://upload.wikimedia.org/wikipedia/en/8/8f/Saw_film_logo.png",
"https://www.youtube.com/watch?v=OCZp5v8V-94",
"666")

interstellar = media.Movie("Interstellar",
"5th dimension",
"http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg",
"www.youtube.com/watch?v=0vxOhd4qlnA",
"890")

v_for_vendetta = media.Movie("V for Vendetta",
"The uprising",
"http://www.impawards.com/2006/posters/v_for_vendetta.jpg",
"www.youtube.com/watch?v=k_13fFIrhPk",
"321")

three_hundred = media.Movie("300",
"This is Sparta!",
"http://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_SX640_SY720_.jpg",
"www.youtube.com/watch?v=WorI5HPWbpg",
"300")

# ************TV*******************
breaking_bad = media.TV("Breaking Bad",
"420",
"Season 5",
"Episode 13",
"https://www.youtube.com/watch?v=HhesaQXLuRY")

# EXAMPLE 1 : Printing the story from a movie
# print(avatar.storyline)

#  EXAMPLE 2 : Printing all the information about a video
# breaking_bad.show_all()

# EXAMPLE 3 : Creating a movie page
movies = [toy_story, avatar, saw, interstellar, v_for_vendetta, three_hundred]
fresh_tomatoes.open_movies_page(movies)

# EXMAPLE 4 : Printing valid ratings for a movie. Demonstrates Class constant variables
# print(avatar.VALID_RATINGS)

# EXAMPLE 5 : Printing documentation, name of the class, and module. Built-in functions
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
