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

# Creating Forrest Gump instance
forrest_gump = media.Movie("Forrest Gump",
                            """While not intelligent, Forrest Gump
                            has accidentally been present at many
                            historic moments, but his true love,
                            Jenny Curran, eludes him.""",
                            "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", # noqa
                            "https://www.youtube.com/watch?v=bLvqoHBptjg")

# Creating Harry Potter instance
harry_potter = media.Movie('Harry Potter',
                            """Rescued from the outrageous neglect of his
                             aunt and uncle, a young boy with a great destiny
                             proves his worth while attending Hogwarts School
                             of Witchcraft and Wizardry.""",
                             "https://s-media-cache-ak0.pinimg.com/736x/7d/b4/b3/7db4b32cfa0da3a0a6b4e0f9630b4c02--harry-potter-movies-harry-potter-images.jpg", # noqa
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo")

# Creating 3 idiots instance
three_idiots = media.Movie('3 Idiots',
                            """Two friends are searching for their long lost
                             companion. They revisit their college days and
                             recall the memories of their friend who inspired
                             them to think differently, even as the rest of
                             the world called them 'idiots'""",
                             "http://www.gstatic.com/tv/thumb/movieposters/7951929/p7951929_p_v8_aa.jpg", # noqa
                             'https://www.youtube.com/watch?v=xvszmNXdM4w')
# Sending list of movies to be displayed on our website
movies = [toy_story, avatar, the_internship, forrest_gump, harry_potter,
          three_idiots]
fresh_tomatoes.open_movies_page(movies)
