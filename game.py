from globals import *
from math import sqrt
class Game:
    """One game."""
    def __init__(self, MOV, isWon, oppName, oppRating, home, day):
        """Initialize the game."""
        self.MOV = MOV
        self.day = day
        self.isWon = isWon
        self.home = home
        self.oppName = oppName
        self.oppRating = oppRating
        self.rating, rawRating = self.calculateGameRating()
        

    def calculateGameRating(self):
        """Calculate rating for protagonist team."""
        oppR = self.oppRating
        ratingCoef = oppR
        #if oppR >= 0:
            #ratingCoef = sqrt(oppR)
        if oppR > GOOD_TEAM_CUTOFF:
            ratingCoef += GOOD_TEAM_BOOST

        #else:
            #ratingCoef = -sqrt(abs(oppR))
        
        if self.isWon:
            rating = (ratingCoef * OPP_RATING_WEIGHT) + WIN_BOOST + sqrt(self.MOV)
        else:
            rating = (ratingCoef * OPP_RATING_WEIGHT) - WIN_BOOST - sqrt(abs(self.MOV))

        if self.day > ROAD_GAME_START and self.day < ROAD_GAME_END:
            if self.home:
                rating -= ROAD_BOOST
            else:
                rating += ROAD_BOOST

        rawRating = rating
        recencyCoef = 1
        rating *= recencyCoef
        return rating, rawRating