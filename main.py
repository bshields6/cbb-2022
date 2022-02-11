from kenpom import Kenpom
from sagarin import Sagarin
from league import League


league = League()

league.readScores()

league.printTeams()

kenpom = Kenpom()

kenpom.kenpom_out('kenpom_in.txt', 'kenpom_out.txt')

sagarin = Sagarin()

sagarin.sagarin_out('sagarin_in.txt', 'sagarin_out.txt')