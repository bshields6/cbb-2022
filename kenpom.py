class Kenpom:
    def __init__(self):
        self.nameDict = {
            'Loyola Chicago': 'Loyola (IL)',
            'Connecticut': 'UConn',
            'North Carolina': 'UNC',
            'UAB': 'Alabama-Birmingham',
            'St. John\'s': 'St. John\'s (NY)',
            'Mississippi': 'Ole Miss',
            'Miami FL': 'Miami (FL)',
            'UC Irvine': 'UC-Irvine',
            'UC Santa Barbara': 'UCSB',
            'Massachusetts': 'UMass',
            'UC Riverside': 'UC-Riverside',
            'Miami OH': 'Miami (OH)',
            'N.C. State': 'NC State',
            'East Tennessee State': 'ETSU',
            'Bowling Green': 'Bowling Green State',
            'UC Davis': 'UC-Davis',
            'Saint Joseph\'s': 'St. Joseph\'s',
            'Pittsburgh': 'Pitt',
            'Cal St. Fullerton': 'Cal State Fullerton',
            'Charleston': 'College of Charleston',
            'Detroit Mercy': 'Detroit',
            'Louisiana Monroe': 'Louisiana-Monroe',
            'Gardner Webb': 'Gardner-Webb',
            'Saint Peter\'s': 'St. Peter\'s',
            'Cal Baptist': 'California Baptist',
            'UMKC': 'Kansas City',
            'Cal St. Bakersfield': 'Cal State Bakersfield',
            'UMass Lowell': 'UMass-Lowell',
            'St. Francis PA': 'Saint Francis (PA)',
            'FIU': 'Florida International',
            'UC San Diego': 'UC-San Diego',
            'Prairie View A&M': 'Prairie View',
            'UT Arlington': 'Texas-Arlington',
            'Illinois Chicago': 'UIC',
            'Purdue Fort Wayne': 'Purdue-Fort Wayne',
            'Loyola MD': 'Loyola (MD)',
            'UT Rio Grande Valley': 'Texas-Rio Grande Valley',
            'SIU Edwardsville': 'SIU-Edwardsville',
            'Cal St. Northridge': 'Cal State Northridge',
            'St. Thomas': 'St. Thomas (MN)',
            'Texas A&M Corpus Chris': 'Texas A&M-Corpus Christi',
            'Albany': 'Albany (NY)',
            'St. Francis NY': 'St. Francis (NY)',
            'Grambling State': 'Grambling',
            'Tennessee Martin': 'UT-Martin',
            'Nebraska Omaha': 'Omaha',
            'Maryland Eastern Shore': 'Maryland-Eastern Shore',
            'Bethune Cookman': 'Bethune-Cookman',
            'Arkansas Pine Bluff': 'Arkansas-Pine Bluff'
        }

    def kenpom_out(self, kenpom_in, kenpom_out):
        with open(kenpom_in, 'r') as f:
            teams = f.read().splitlines()
            f.close()

        for count,team in enumerate(teams):
            if team.endswith('St.'):
                team = team[:-3 ]+ 'State'
                teams[count] = team
        
        with open(kenpom_out, 'w') as f:
            for t in teams:
                if t == 'NCSOS' or t == 'Team':
                    continue
                if t in self.nameDict.keys():
                    f.write(self.nameDict[t])
                else:
                    f.write(t)
                f.write('\n')
            f.close()
