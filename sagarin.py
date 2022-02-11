import re

class Sagarin:
    def __init__(self):
        self.nameDict = {
            "Connecticut": "UConn",
            "Xavier-Ohio": "Xavier",
            "Southern California": "USC",
            "North Carolina": "UNC",
            "Saint Mary's-Cal.": "Saint Mary\'s",
            "Loyola-Chicago": "Loyola (IL)",
            "UAB": "Alabama-Birmingham",
            "St. John\'s": "St. John\'s (NY)",
            "VCU(Va. Commonwealth)": "VCU",
            "Miami-Florida": "Miami (FL)",
            "Mississippi": "Ole Miss",
            "Central Florida(UCF)": "UCF",
            "Iona College": "Iona",
            "UC Irvine": "UC-Irvine",
            "Pittsburgh": "Pitt",
            "Monmouth-NJ": "Monmouth",
            "UC Santa Barbara": "UCSB",
            "UC Riverside": "UC-Riverside",
            "Oakland-Mich.": "Oakland",
            "Saint Joseph\'s-Pa.": "St. Joseph\'s",
            "East Tennessee State(ETS": "ETSU",
            "Pennsylvania": "Penn",
            "Massachusetts": "UMass",
            "NC Greensboro": "UNC Greensboro",
            "CS Fullerton": "Cal State Fullerton",
            "Saint Peter\'s": "St. Peter\'s",
            "Hawai\'i": "Hawaii",
            "NC Wilmington": "UNC Wilmington",
            "Boston U.": "Boston University",
            "UC Davis": "UC-Davis",
            "Detroit Mercy": "Detroit",
            "Bowling Green": "Bowling Green State",
            "UT Arlington": "Texas-Arlington",
            "Stony Brook-NY": "Stony Brook",
            "Southern U.": "Southern",
            "Miami-Ohio": "Miami (OH)",
            "NC Asheville": "UNC Asheville",
            "Kansas City(UMKC)": "Kansas City",
            "Fla. International": "Florida International",
            "CS Bakersfield": "Cal State Bakersfield",
            "Fort Wayne(PFW)": "Purdue-Fort Wayne",
            "UMass Lowell": "UMass-Lowell",
            "Loyola-Maryland": "Loyola (MD)",
            "Long Island U.(LIU)": "LIU",
            "Albany-NY": "Albany (NY)",
            "ULM": "Louisiana-Monroe",
            "North Florida(UNF)": "North Florida",
            "Army West Point": "Army",
            "Texas A&M-CorpusChristi": "Texas A&M-Corpus Christi",
            "UC San Diego": "UC-San Diego",
            "Illinois-Chicago": "UIC",
            "NC A&T": "North Carolina A&T",
            "Presbyterian College": "Presbyterian",
            "SE Missouri State(SEMO)": "Southeast Missouri State",
            "UTRGV": "Texas-Rio Grande Valley",
            "NC Central": "North Carolina Central",
            "Prairie View A&M": "Prairie View",
            "NJIT(New Jersey Tech)": "NJIT",
            "Binghamton-NY": "Binghamton",
            "SE Louisiana": "Southeastern Louisiana",
            "Cal Poly-SLO": "Cal Poly",
            "CS Northridge": "Cal State Northridge",
            "Grambling State": "Grambling",
            "Saint Francis-Pa.": "Saint Francis (PA)",
            "St. Francis-NY": "St. Francis (NY)",
            "Tennessee-Martin": "UT-Martin",
            "American U.": "American",
            "St. Thomas-Mn.": "St. Thomas (MN)",
            "SC State": "South Carolina State",
            "Md.-Eastern Shore(UMES)": "Maryland-Eastern Shore",
            "Omaha(Neb.-Omaha)": "Omaha",
            "Central Connecticut St.": "Central Connecticut",
            "Ark.-Pine Bluff": "Arkansas-Pine Bluff",
            "MVSU(Miss. Valley St.)": "Mississippi Valley State"
        }


    def sagarin_out(self, sagarin_in, sagarin_out):
            with open(sagarin_in, 'r') as f:
                raw = f.read().splitlines()
                f.close()

            rows = []

            it = iter(range(len(raw)))
            for t in it:
                if raw[t][0] == "C":
                    next(it)
                    next(it)
                    continue
                else:
                    rows.append(raw[t])
            
            teams = []
            for count,row in enumerate(rows):
                teams.append(self.find_team(row))
            
            with open(sagarin_out, 'w') as f:
                for t in teams:
                    if t in self.nameDict.keys():
                        f.write(self.nameDict[t])
                    else:
                        f.write(t)
                    f.write('\n')
                f.close()

    def find_team(self, row):
        ind = row.find('=')
        team = row[:ind]
        team = team.lstrip().rstrip()
        start = team.find(next(filter(str.isalpha, team)))
        return team[start:]