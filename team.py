#include "Team.h"
from  globals import *
class Team:
    """The team."""
    def __init__(self, name, preRating, oStats, dStats, SOS):
        self.name = name
        self.statRating = 0
        self.seasonRating = 0
        self.preseasonRating = preRating
        self.SOS = SOS
        self.GP = 0
        self.wins = 0
        self.losses = 0
        self.rating = 0
        self.games = []
        self.adjustedGameRatings = []
        self.oStats = oStats
        self.dStats = dStats

    def calculateRating(self):
        """Calculate the team's rating."""
        rar = self.statRating * STAT_WEIGHT + self.seasonRating * GAME_WEIGHT  + self.preseasonRating * PRESEASON_WEIGHT + self.SOS * SOS_WEIGHT
        return rar

    def addGame(self, g):
        """Add a game to the team's record."""
        self.GP += 1
        if g.isWon:
            self.wins += 1
        else:
            self.losses += 1
        self.games.append(g)
        #change seasonRating to new weighted average of all game ratings
        ratings = [x.rating for x in self.games]
        total = 0
        self.adjustedGameRatings = []
        for c,i in enumerate(ratings):
            coef = 10*(c+1) / (self.GP**2)
            self.adjustedGameRatings.append(i*1)
            total += i*1
        self.seasonRating = total / self.GP
        self.rating = self.calculateRating()

    def printGames(self):
        """Print games. In progress."""
        with open('output.txt', 'a') as file:
            sum = 0
            file.write("TEAM NAME:" + self.name + "-----------------\n\n")
            for c,g in enumerate(self.games):
                file.write(g.oppName + '\n')
                file.write("Rating:" + str(g.oppRating))
                file.write('\n')
                file.write("MOV: " + str(g.MOV) + '\n')
                file.write("isWon: " + str(g.isWon) + '\n')
                file.write("home: " + str(g.home) + '\n')
                file.write("day: " + str(g.day) + '\n')
                file.write("Game Rating:" + str(g.rating))
                file.write('\n\n\n')
                file.write("~~~~~~~~~~~~~ADJUSTED GAME RATING!~~~~~~~~~~~~:"+ str(self.adjustedGameRatings[c]) +  '\n\n\n\n')
                sum += self.adjustedGameRatings[c]
            file.write("SUM" + str(sum))