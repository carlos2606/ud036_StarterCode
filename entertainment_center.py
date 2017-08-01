import media
import fresh_tomatoes

# Creating Toy Story instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy an his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Creating Avatar instance
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# Creating The Internship instance
the_internship = media.Movie("The Internship",
                             '''Two salesmen whose careers have been torpedoed
                                by the digital age find their way into a
                                coveted internship at Google''',
                             '''https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg''', # noqa
                             "https://www.youtube.com/watch?v=cdnoqCViqUo")

# Sending list of movies to be displayed on our website
fresh_tomatoes.open_movies_page([toy_story, avatar, the_internship])
