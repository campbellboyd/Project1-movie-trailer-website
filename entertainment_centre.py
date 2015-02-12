'''
Created on 7 Feb 2015

@author: campbell
'''
import media
import fresh_tomatoes 

# data - creating instances of class Movie from media.py
toy_story3 = media.Movie("Toy Story 3",
                         "2010",
                         "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
                         "Lee Unkrich",
                         "John Lasseter (story), Andrew Stanton (story)",
                         "Tom Hanks, Tim Allen, Joan Cusack",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Toy_Story_3_poster.jpg/220px-Toy_Story_3_poster.jpg",
                         "https://www.youtube.com/watch?v=JcpWXaA2qeg")
platoon = media.Movie("Platoon",
                      "1986",
                      "A young recruit in Vietnam faces a moral crisis when confronted with the horrors of war and the duality of man.",
                      "Oliver Stone",
                      "Oliver Stone",
                      "Charlie Sheen, Tom Berenger, Willem Dafoe",
                      "https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg",
                      "https://www.youtube.com/watch?v=AykiF9YYF2U")
the_deer_hunter = media.Movie("The Deer Hunter",
                              "1978",
                              "An in-depth examination of the ways in which the U.S. Vietnam war impacts and disrupts the lives of people in a small industrial town in Pennsylvania.",
                              "Michael Cimino",
                              "Michael Cimino (story), Deric Washburn (story)",
                              "Robert De Niro, Christopher Walken, John Cazale",
                              "https://upload.wikimedia.org/wikipedia/en/5/57/The_Deer_Hunter_poster.jpg",
                              "https://www.youtube.com/watch?v=3Gqit3zVmyc")
apocalypse_now = media.Movie("Apocalypse Now",
                              "1979",
                              "During the Vietnam War, Captain Willard is sent on a dangerous mission into Cambodia to assassinate a renegade colonel who has set himself up as a god among a local tribe.",
                              "Francis Ford Coppola (as Francis Coppola)",
                              "John Milius, Francis Ford Coppola",
                              "Martin Sheen, Marlon Brando, Robert Duvall",
                          "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
                                 "https://www.youtube.com/watch?v=snDR7XsSkB4")
full_metal_jacket = media.Movie("Full Metal Jacket",
                                "1987",
                                "A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                                "Stanley Kubrick",
                                "Gustav Hasford (novel), Stanley Kubrick (screenplay)",
                                "Matthew Modine, R. Lee Ermey, Vincent D'Onofrio",
                                "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
                                "https://www.youtube.com/watch?v=UuWmCVdwhKg")
a2001_a_space_odyssey = media.Movie("2001: A Space Odyssey",
                                   "1968",
                                   "Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
                                   "Stanley Kubrick",
                                   "Stanley Kubrick (screenplay), Arthur C. Clarke (screenplay)",
                                   "Keir Dullea, Gary Lockwood, William Sylvester",
                                   "https://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                                   "https://www.youtube.com/watch?v=N6ywMnbef6Y")
forrest_gump = media.Movie("Forrest Gump",
                           "1994",
                           "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "Robert Zemeckis",
                           "Winston Groom (novel), Eric Roth (screenplay)",
                           "Tom Hanks, Robin Wright, Gary Sinise",
                            "http://content7.flixster.com/movie/11/17/36/11173677_det.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")
avatar = media.Movie("Avatar",
                     "2009",
                     "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home..",
                     "James Cameron",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=_Tkc5pQp_JE")
goodfellas = media.Movie("Goodfellas",
                         "1990",
                         "Henry Hill and his friends work their way up through the mob hierarchy.",
                         "Martin Scorsese",
                         "Nicholas Pileggi (book), Nicholas Pileggi (screenplay)",
                         "Robert De Niro, Ray Liotta, Joe Pesci",
                          "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                          "https://www.youtube.com/watch?v=YH-7he92XfI")

# load data in list for idplaying in module fresh_tomatoes
movies = [toy_story3, forrest_gump, avatar, goodfellas, a2001_a_space_odyssey, full_metal_jacket, apocalypse_now, the_deer_hunter, platoon]
fresh_tomatoes.open_movies_page(movies)
