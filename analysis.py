import pandas as pd

#get the data from the csv file
data = pd.read_csv("nba_test.csv")
#print(data)
#print(data.Team)

#define a class Team, which takes team name and performes the analysis
class Team():
    def __init__(self, team_name):
        self.team_name = team_name

    def win_loss_ratio(self):
        
        team=data.loc[data['Team']== self.team_name]
        overall = team.iat[0,1]
        wins = int(overall.split('-')[0])
        loses = int(overall.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        print(f'The overall win/loss ratio of {self.team_name} is {win_loss_ratio}%!')
        return win_loss_ratio

#This is to test and should be in main 
team_name = input("Team name: ")
my_team=Team(team_name)
my_team.win_loss_ratio()
