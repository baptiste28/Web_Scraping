from numpy.lib.function_base import _piecewise_dispatcher
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#define a class Team, which takes team name and performes the analysis
class Team():

    def __init__(self):

        while True:
            self.team_name = input("Team name: ").title()
            self.data = pd.read_csv("nba_test.csv")
            self.data = self.data.fillna('1-100')
            self.team_row=self.data.loc[self.data['Team']== self.team_name]

            print(self.team_row)

            if len(self.team_row) == 0:
                print('This is not a valid team name!')
                continue
            else:
                break

        self.dictionary ={1: 'Overall', 2:'Home', 3:'Road', 4:'E', 5:'W',6:'A', 7:'C',8:'SE', 9:'NW', 10:'P',11:'SW', 12:'Pre' , 13:'Post', 14:'≤3', 15:'≥10', 16:'Oct', 17:'Nov', 18:'Dec', 19:'Jan', 20:'Feb', 21:'Mar', 22:'Jul', 23:'Aug'}
        self.user_input = None
        self.user_option = None
        self.data_visual = Show_data()
    
    def menu(self):
        while True:
            print('What metrix do you want to see? \n 1. Win/loss ratio \n 2. Division comparison \n 3. Monthly graph \n 4. Coference statistics \n 5. Game result predictor \n\n OR type Q to quit \n')
            self.user_option = input("What option are you choosing? ")

            if self.user_option == '1':
                print('What metrix do you want to see? \n 1. Overall win ratio \n 2. Home win ratio \n 3. Road win ratio \n\n OR press any button to go back to the main menu!\n')
                self.user_input=input('Input a number between 1 and 3: ')
                try:
                    self.user_input = int(self.user_input)
                    if self.user_input < 1 or self.user_input > 3:
                        print('This is not a valid option!')
                    else:
                        a = self.win_loss_ratio(self.user_input)
                        self.data_visual.piechart_win_loss_ratio(a[0], a[1], a[3])
            
                except (TypeError, ValueError) as e:
                    print('Not a valid option. Choose again')
                    continue

            elif self.user_option == '2':
                continue
            elif self.user_option == '3':
                a = self.monthly_win_loss()
                self.data_visual.linechart(a)
                continue
            elif self.user_option == '4':
                self.conference()
            elif self.user_option == '5':
                continue
            elif self.user_option =='q':
                quit()
            else:
                print("\nThis is not a valid option! Please try again!")
                continue


    def win_loss_ratio(self,category):
        
        #get only the row of the chosen team
        category_value = self.team_row.iat[0,category]
        wins = int(category_value.split('-')[0])
        loses = int(category_value.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        #print(f'The {self.dictionary[category]} win/loss ratio of {self.team_name} is {win_loss_ratio}%!')
        title = f'  Win/loss ratio in {self.dictionary[category]} category of {self.team_name}'

        # return wins and losses 
        return wins,loses,win_loss_ratio,title

    def monthly_win_loss(self):
        months = []
        for i in range(16,24):
            month = self.win_loss_ratio(i)[2]
            months.append(month)
        return months



class Show_data():

    def __init__(self):
        pass
    
    #Define a function to create a piechart based on wins and losses in any category

    def piechart_win_loss_ratio(self, wins ,loses,title):
        labels = 'Wins', 'Losses'
        sizes = [wins,loses]
        explode = (0.1 ,0)
        colors = ['#e38d8d', '#95b7ed']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title(title)
        plt.savefig('plots.png')

    
    def linechart(self,y):
        x = np.linspace(1,100,8)
        x_text = ['Oct', 'Nov','Dec','Jan','Feb','Mar','Jul','Aug']
        plt.figure()
        plt.title('Monthly performance graph')
        plt.ylabel('%')
        plt.xticks(x,x_text)
        plt.plot(x,y)
        plt.savefig('plots.png')
        
        


my_team=Team()
a = my_team.menu()




