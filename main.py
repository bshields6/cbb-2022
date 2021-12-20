from kenpom import Kenpom
from league import League


league = League()

league.readScores()

league.printTeams()

kenpom = Kenpom()

kenpom.kenpom_out('kenpom_in.txt', 'kenpom_out.txt')