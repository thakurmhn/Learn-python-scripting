#!/usr/bin/env python3

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __getitem__(self, i):
        return self.players[i]

    def __repr__(self):
        return f'{self.players}'

    def __str__(self):
        return f'Club {self.name} with 2 players'

# create instance of class

my_club=Club('Achievers')

my_club.players.append('Vedak')
my_club.players.append('Binish')

print(my_club)

print(my_club[0])
