from numpy.lib.function_base import _piecewise_dispatcher
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#define a class Team, which takes team name and performes the analysis
class Team():

    def __init__(self, team_name):
        self.team_name = team_name
        self.team_row=data.loc[data['Team']== self.team_name]
        print(self.team_row)
        self.dictionary ={1: 'Overall', 2:'Home', 3:'Road', 4:'E', 5:'W',6:'A', 7:'C',8:'SE', 9:'NW', 10:'P',11:'SW', 12:'Pre' , 13:'Post', 14:'≤3', 15:'≥10', 16:'Oct', 17:'Nov', 18:'Dec', 19:'Jan', 20:'Feb', 21:'Mar', 22:'Jul', 23:'Aug'}
        self.user_input = None
        self.user_option = None
        self.data_visual = Show_data()

    def menu(self):
        while True:
            print('What metrix do you want to see? \n 1. Win/loss ratio \n 2. Division comparison \n 3. Monthly graph \n 4. Conference statistics \n 5. Game result predictor \n 6. All-Star analysis \n 7. Game Margin \n\n OR type Q to quit \n')
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
                        self.data_visual.piechart_win_loss_ratio(a[0], a[1])

                except (TypeError, ValueError) as e:
                    print('Not a valid option. Choose again')
                    continue

            elif self.user_option == '2':
                self.divison_comparison()
                continue
            elif self.user_option == '3':
                a = self.monthly_win_loss()
                self.data_visual.linechart(a)
                continue
            elif self.user_option == '4':
                self.conference_comparison()
                continue
            elif self.user_option == '5':
                pass
            elif self.user_option == '6':
                self.all_star()
                continue
            elif self.user_option == '7':
                self.game_margin()
                continue
            elif self.user_option =='q':
                quit()
            else:
                print("\nThis is not a valid option! Please try again!")
                continue




    def win_loss_ratio(self,category,printing):

        #get only the row of the chosen team
        category_value = self.team_row.iat[0,category]
        wins = int(category_value.split('-')[0])
        loses = int(category_value.split('-')[1])
        win_loss_ratio = round((wins / (wins+loses) *100),2)
        # simple IF function to print or not that phrase when callin the win_loss_ratio function
        if printing == True:
            print(f'The {self.dictionary[category]} win/loss ratio of {self.team_name} is {win_loss_ratio} % !')

        # return wins and losses
        return wins,loses,win_loss_ratio

    def monthly_win_loss(self):
        oct = self.win_loss_ratio(16)[2]
        nov = self.win_loss_ratio(17)[2]
        dec = self.win_loss_ratio(18)[2]
        jan = self.win_loss_ratio(19)[2]
        feb = self.win_loss_ratio(20)[2]
        mar = self.win_loss_ratio(21)[2]
        jul = self.win_loss_ratio(22)[2]
        aug = self.win_loss_ratio(23)[2]

        return oct,nov,dec,jan,feb,mar,jul,aug

    def divison_comparison(self):
        # creating a list of win/loss ratios for each division
        division_list = []
        for i in range(6,12):
            division_win_loss = self.win_loss_ratio(i,False)[2]
            division_list.append(division_win_loss)

        # manually creating a list of the official division names
        division_list_names = ["Atlantic","Central","South-East","North-West","Pacific","South-West"]

        position_max = division_list.index(max(division_list))
        position_min = division_list.index(min(division_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = division_list_names[position_max]
        name_position_min = division_list_names[position_min]

        # creating a list of the total number of games per division, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(6,12):
            number_games = self.win_loss_ratio(i,False)[0] + self.win_loss_ratio(i,False)[1]
            list_number_games.append(number_games)

        print("")
        print("The highest win/loss ratio was",max(division_list),"%", f"and it was in the {name_position_max} division")
        print("")
        print("The lowest win/loss ratio was",min(division_list),"%", f"and it was in the {name_position_min} division")
        print("")

        # looping for the 6 different divisions
        print(f"The {team_name} played a total of :")
        print("")
        for i in range(6):
            print('\t' * 1 + f"{list_number_games[i]} games in the {division_list_names[i]} division")
            print("")

    def conference_comparison(self):
        # creating a list of win/loss ratios for each division
        conference_list = []
        for i in range(4,6):
            conference_win_loss = self.win_loss_ratio(i,False)[2]
            conference_list.append(conference_win_loss)

        # manually creating a list of the official division names
        conference_list_names = ["East","West"]

        position_max = conference_list.index(max(conference_list))
        position_min = conference_list.index(min(conference_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = conference_list_names[position_max]
        name_position_min = conference_list_names[position_min]

        # creating a list of the total number of games per conference, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(4,6):
            number_games = self.win_loss_ratio(i,False)[0] + self.win_loss_ratio(i,False)[1]
            list_number_games.append(number_games)

        print("")
        print("The highest win/loss ratio was",max(conference_list),"%", f"and it was in the {name_position_max} conference")
        print("")
        print("The lowest win/loss ratio was",min(conference_list),"%", f"and it was in the {name_position_min} conference")
        print("")

        # looping for the 2 different conferences
        print(f"The {team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games in the {conference_list_names[i]} conference")
            print("")

    def all_star(self):
        # creating a list of win/loss ratios for pre and post All-Star game
        all_star_list = []
        for i in range(12,14):
            all_star_win_loss = self.win_loss_ratio(i,False)[2]
            all_star_list.append(all_star_win_loss)

        # manually creating a list of the official division names
        all_star_list_names = ["Pre All-Star Game","Post All-Star Game"]

        position_max = all_star_list.index(max(all_star_list))
        position_min = all_star_list.index(min(all_star_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = all_star_list_names[position_max]
        name_position_min = all_star_list_names[position_min]

        # creating a list of the total number of games per conference, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(12,14):
            number_games = self.win_loss_ratio(i,False)[0] + self.win_loss_ratio(i,False)[1]
            list_number_games.append(number_games)

        print("")
        print("The highest win/loss ratio was",max(all_star_list),"%", f"and it was {name_position_max}")
        print("")
        print("The lowest win/loss ratio was",min(all_star_list),"%", f"and it was {name_position_min}")
        print("")

        # looping for the 2 different conferences
        print(f"The {team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games {all_star_list_names[i]}")
            print("")

    def game_margin(self):
        # creating a list of win/loss ratios for pre and post All-Star game
        game_margin_list = []
        for i in range(14,16):
            game_margin_win_loss = self.win_loss_ratio(i,False)[2]
            game_margin_list.append(game_margin_win_loss)

        # manually creating a list of the official division names
        game_margin_list_names = ["≤3 points game margin","≥ 10 points game margin"]

        position_max = game_margin_list.index(max(game_margin_list))
        position_min = game_margin_list.index(min(game_margin_list))
        # fetching the corresponding Division name of the min/max win/loss ratio
        name_position_max = game_margin_list_names[position_max]
        name_position_min = game_margin_list_names[position_min]

        # creating a list of the total number of games per conference, for one team (ex:[10,8,7,15,12,9])
        list_number_games = []
        number_games = []
        for i in range(14,16):
            number_games = self.win_loss_ratio(i,False)[0] + self.win_loss_ratio(i,False)[1]
            list_number_games.append(number_games)

        print("")
        print("The highest win/loss ratio was",max(game_margin_list),"%", f"and it was in the {name_position_max} category")
        print("")
        print("The lowest win/loss ratio was",min(game_margin_list),"%", f"and it was in the {name_position_min} category")
        print("")

        # looping for the 2 different conferences
        print(f"The {team_name} played a total of :")
        print("")
        for i in range(2):
            print('\t' * 1 + f"{list_number_games[i]} games with {game_margin_list_names[i]}")
            print("")



class Show_data():

    def __init__(self):
        pass


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

    def linechart(self,y):
        x = [10,20,30,40,50,60,70,80]
        x_text = ['Oct', 'Nov','Dec','Jan','Feb','Mar','Jul','Aug']
        plt.figure()
        plt.xticks(x,x_text)
        plt.plot(x,y)
        plt.show()
        plt.close()


#get the data from the csv file
data = pd.read_csv("nba_test.csv")

#Reaplce the NAN values with 0. For example team 'Charlotte Hornets' does not have values in the Jul and Aug category.
data = data.fillna('1-100')
#This is to test and should be in main
#print(data)
#print(data.Team)


team_name = input("Team name: ")

my_team=Team(team_name)
a = my_team.menu()
