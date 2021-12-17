from team import Team
from game import Game
from statistics import mean, stdev
import csv
from globals import *

class League:
	"""The league."""
	def __init__(self):
		self.teamNames = []
		self.teams = []
		self.day = 0
		self.createTeams()
		self.normalizeWeightStats()
		self.normalizeStatRatings()
		self.normalizeSOS()

	def readScores(self):
		f = open("Scores.txt", 'r')
		lines = f.read().splitlines()
		f.close()
		count = 0
		for line in range(0, len(lines), 2):
			self.day += 1
			#get two lines at once because two teams in game
			str1 = lines[count]
			str2 = lines[count + 1]
			count += 2
			#remove final and whitespace from scores
			str1 = self.cropLine(str1)
			str2 = self.cropLine(str2)

			score1Digits = self.findNumDigits(str1)
			score2Digits = self.findNumDigits(str2)
			name1 = str1[:-(score1Digits + 1)]
			name2 = str2[:-(score2Digits + 1)]
			name1 = self.removeSeed(name1)
			name2 = self.removeSeed(name2)
			score1 = int(str1[-score1Digits:])
			score2 = int(str2[-score2Digits:])

			MOV = abs(score1 - score2)
			team1win = score1 > score2
			
			t1d1 = True
			t2d1 = True
			#find team 1 and their rating
			try:
				ind1 = self.teamNames.index(name1)
				rating1 = self.teams[ind1].rating
			#if team isn't d1, ValueError gets thrown from index()
			except ValueError:
				rating1 = NOT_D1_RATING
				t1d1 = False
			try:
				ind2 = self.teamNames.index(name2)
				rating2 = self.teams[ind2].rating
			except ValueError:
				rating2 = NOT_D1_RATING
				t2d1 = False

			if t1d1:
				g = Game(MOV, team1win, name2, rating2, False, self.day)
				team = self.teams[ind1]
				team.addGame(g)
			
			if t2d1:
				g = Game(MOV, not team1win, name1, rating1, True, self.day)
				team = self.teams[ind2]
				team.addGame(g)
				
		self.normalizeSeasonRatings()
 
	def createTeams(self):
		"""Create all teams and initialize ratings."""
		t = open("Teams.txt", 'r')
		o = open("oStats.csv", 'r')
		d = open("dStats.csv", 'r')
		p = open("PreseasonRatings.csv", 'r')
		oStatsTotals = []
		dStatsTotals = []
		teams = t.read().splitlines()
		preReader = csv.reader(p)
		preRatings = [x[1] for x in preReader]
		oList = list(csv.reader(o))
		dList = list(csv.reader(d))

		for count,ele in enumerate(teams):
			if count == NUM_TEAMS:
				break
			if ele in NOT_PLAYING:
				continue

			sos = float(oList[count][1])
			oLine = oList[count][2:]
			dLine = dList[count][2:]

			self.teamNames.append(ele)
			oStats = []
			dStats = []
			for i in oLine:
				oStats.append(float(i))
			
			for i in dLine:
				dStats.append(float(i))
			team = Team(ele, float(preRatings[count]), oStats, dStats, sos)
			self.teams.append(team)

		t.close()
		o.close()
		d.close()
		p.close()

	def printTeams(self):
		"""Print teams in order of rating."""
		sortedTeams = sorted(self.teams, key=lambda x: x.rating, reverse=True)

		#print('Team\t\t\t\t\tRating\t\t\t\tWins\tLosses\t\t\tStat\t\t\tSeason\t\t\t\t\tSOS')
		for t in sortedTeams:
			string = t.name
        	#for alignment
			le = len(t.name)
			for i in range(2):
				string += "\t"

			string += "\t" + str(t.rating) + "\t\t" + str(t.wins) + "\t\t" + str(t.losses) + "\t\t" + \
								str(t.statRating) + "\t\t" + str(t.seasonRating) + "\t\t" + str(t.SOS)

			print(string)


	def findNumDigits(self, line):
		"""Find number of digits at end of line."""
		i = len(line) - 1
		count = 0
		while True:
			c = line[i]
			if c.isdigit():
				i -= 1
				count += 1
			else:
				break

		return count


	def removeSeed(self, line):
		"""Take seed out of line if it's there."""
		for count,char in enumerate(line):
			if (char == '('):
				c = line[count + 1]
				#check for number, some teams have () in their name such as St. Johns (NY)
				if c.isdigit():
					#-1 is for the space always right before seed
					line = line[:(count - 1)]
					break
		return line


	def cropLine(self, line):
		"""Take Final, OT, and trailing whitespace out of line."""
		if len(line) > 4 and line[-5:] == "Final":
			line = line[:-5]

		elif line[-2:] == "OT":
			line = line[:-2]

		#take 2 spaces off if number isn't at 2nd to last position
		c = line[-2]
		if not c.isdigit():
			line = line[:-2]
		#take 1 off otherwise
		else:
			line = line[:-1]
		
		return line


	def normalizeStatRatings(self):
		"""Normalize stat ratings to standard distribution."""
		ratings = []

		for t in self.teams:
			ratings.append(t.statRating)

		avg = mean(ratings)
		dev = stdev(ratings)

		newRatings = []

		for r in ratings:
			new = (r - avg) / dev
			newRatings.append(new)
		for c,t in enumerate(self.teams):
			t.statRating = newRatings[c]
			t.rating = t.calculateRating()

	def normalizeSeasonRatings(self):
		"""Normalize season ratings to standard distribution."""
		ratings = []

		for t in self.teams:
			ratings.append(t.seasonRating)

		avg = mean(ratings)
		dev = stdev(ratings)

		newRatings = []
		for r in ratings:
			new = (r - avg) / dev
			newRatings.append(new)

		for c,t in enumerate(self.teams):
			t.seasonRating = newRatings[c]
			t.rating = t.calculateRating()

	def normalizeSOS(self):
		sos = []
		for t in self.teams:
			sos.append(t.SOS)
		
		avg = mean(sos)
		dev = stdev(sos)

		newSos = []
		for s in sos:
			new = (s - avg) / dev
			newSos.append(new)
		for c,t  in enumerate(self.teams):
			t.SOS = newSos[c]
			t.rating = t.calculateRating()

	def normalizeWeightStats(self):
		"""Normalize oStats and dStats to standard distribution, then weigh them."""
		#normalize oStats and dStats 1 category at a time
		for c in range(NUM_CATEGORIES):
			oStats = []
			dStats = []
			for t in self.teams:
				oStats.append(t.oStats[c])
				dStats.append(t.dStats[c])
			o_avg = mean(oStats)
			o_dev = stdev(oStats)
			d_avg = mean(dStats)
			d_dev = stdev(dStats)
			newO = []
			newD = []
			for s in oStats:
				new = (s - o_avg) / o_dev
				newO.append(new)
			for s in dStats:
				new = (s - d_avg) / d_dev
				newD.append(new)		
			for count,t in enumerate(self.teams):
				t.oStats[c] = newO[count] * O_STAT_WEIGHTS[c]
				t.dStats[c] = newD[count] * D_STAT_WEIGHTS[c]
		
		for t in self.teams:
			t.statRating = sum(t.oStats) + sum(t.dStats)