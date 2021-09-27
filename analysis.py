from numpy.lib.function_base import _piecewise_dispatcher
import pandas as pd
import matplotlib.pyplot as plt

#get the data from the csv file
data = pd.read_csv("nba_test.csv")
#print(data)
#print(data.Team)

#define a class Team, which takes team name and performes the analysis
class Team():

    def __init__(self, team_name):
        self.team_name = team_name
        self.team_row=data.loc[data['Team']== self.team_name]
        print(self.team_row)
        self.dictionary ={1: 'Overall', 2:'Home'}
        self.user_input = None
        self.user_option =None
    
    def menu(self):
        print('What metrix do you want to see? \n 1. Win/loss ratio \n 2. Division comparison \n 3. Montly graph \n 4.Game result predictor')
        self.user_option = input("What option are you choosing? ")

        if self.user_option == '2':
            print('What metrix do you want to see? \n 1. Overall win ratio \n 2.Monthly win ratio')
            self.user_input=input('Input a number between 1 and 10: ')
            try:
                self.user_input = int(self.user_input)
                if self.user_input < 1 or self.user_input >10:
                    print('This is not a valid option!')
                else:
                    return self.win_loss_ratio(self.user_input)
    
            except TypeError:
                print('Not a valid option. Choose again')

        elif self.user_option == '2':
            pass


    def win_loss_ratio(self,category):
        
        #get only the row of the chosen team
        category_value = self.team_row.iat[0,category]
        wins = int(category_value.split('-')[0])
        loses = int(category_value.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        print(f'The {self.dictionary[category]} win/loss ratio of {self.team_name} is {win_loss_ratio}%!')

        # return wins and losses 
        return wins,loses,win_loss_ratio

    def monthly_win_loss(self):
        oct = self.win_loss_ratio(16)
        nov = self.win_loss_ratio(17)
        


class Show_data():

    def __init__(self, user_input):
        self.user_input = user_input

    #Define a function to create a piechart based on wins and losses in any category

    def piechart_win_loss_ratio(self, wins ,loses):
        labels = 'Wins', 'Losses'
        sizes = [wins,loses]
        explode = (0.1 ,0)
        colors = ['#e38d8d', '#95b7ed']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title('')
        plt.savefig('plots.png')
        plt.show() 
        plt.close(1)
    
    def barchart(self):
        pass



#This is to test and should be in main 
team_name = input("Team name: ")

my_team=Team(team_name)
a = my_team.menu()
my_team.user_input

my_team.monthly_win_loss()
visual_data=Show_data(my_team.user_input)

visual_data.piechart_win_loss_ratio(a[0], a[1])


