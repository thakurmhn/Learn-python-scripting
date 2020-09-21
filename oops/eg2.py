#!/usr/bin/env python3



class Movie:
    def __init__(self, name, director):
        self.name=name
        self.director=director


    def print_info(self):
        print(f"{self.name} by {self.director}")

my_movie = Movie('The Matrix', 'Wachowski')

my_movie.print_info()

#print(my_movie.name)
#print(my_movie.director)
