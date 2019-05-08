from pandas import pandas
from pandas import ExcelFile, ExcelWriter
import random
from app.meal import Meal

from flask import Flask
from flask import request

items_sheet = pandas.read_excel('Meals.xlsx', sheet_name='Items')
items_list = []

class FoodProcessor():
    def addInfo(self):
        for i in range(len(items_sheet['Items'])):
            breakfast = lambda : True if items_sheet['Breakfast'][i] == "Yes" else False
            lunch = lambda : True if items_sheet['Lunch'][i] == "Yes" else False
            dinner = lambda : True if items_sheet['Dinner'][i] == "Yes" else False
            shaak = lambda : True if items_sheet['Shaaks?'][i] == "Yes" else False
            daal = lambda : True if items_sheet['Daals?'][i] == "Yes" else False

            meal = Meal(items_sheet['Items'][i], breakfast(), lunch(), dinner(), shaak(), daal(), items_sheet['Nutrition'][i])

            if items_sheet['Nutrition'][i] == "High":
                items_list.append(meal)
            elif items_sheet['Nutrition'][i] == "Medium":
                items_list.append(meal)
            elif items_sheet['Nutrition'][i] == "Low":
                items_list.append(meal)

    def printStatement(self, mealTime):
        number = random.randint(1, 101)
        mealTime_list = []
        meal = None

        while meal == None:
            for item in items_list:
                if mealTime == "Breakfast" and number < 25:
                    if item.breakfast == True and item.nutrition == "Low":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Breakfast" and number < 55:
                    if item.breakfast == True and item.nutrition == "Medium":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Breakfast":
                    if item.breakfast == True and item.nutrition == "High":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Lunch" and number < 25:
                    if item.lunch == True and item.nutrition == "Low":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Lunch" and number < 55:
                    if item.lunch == True and item.nutrition == "Medium":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Lunch":
                    if item.lunch == True and item.nutrition == "High":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Dinner" and number < 25:
                    if item.dinner == True and item.nutrition == "Low":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Dinner" and number < 55:
                    if item.dinner == True and item.nutrition == "Medium":
                        mealTime_list.append(item)
                    else:
                        continue
                elif mealTime == "Dinner":
                    if item.dinner == True and item.nutrition == "High":
                        mealTime_list.append(item)
                    else:
                        continue
                else:
                    return ("")

            meal = random.choice(mealTime_list)

        shaak_list = items_sheet['Shaaks'][:21]
        daal_list = items_sheet['Daals'][:6]

        shaak_selection = random.choice(shaak_list)
        daal_selection = random.choice(daal_list)

        if meal.shaak == False and meal.daal == False:
            return_str = ("{}".format(meal.name))
        elif meal.shaak == True and meal.daal == False:
            return_str = ("{}, with {} nu shaak".format(meal.name, shaak_selection))
        elif meal.shaak == False and meal.daal == True:
            return_str = ("{}, with {} ni daal".format(meal.name, daal_selection))
        elif meal.shaak == True and meal.daal == True:
            return_str = ("{}, with {} nu shaak and {} ni daal".format(meal.name, shaak_selection, daal_selection))
        else:
            print("Yeah, what the heck?")

        return_str_final = ("{}".format(return_str))
        return return_str_final

    def main(self):
        addInfo()

        whichMeal = input("Breakfast, lunch, or dinner?\n")
        #print(printStatement(selectMeal(whichMeal)))


if __name__ == "__main__": FoodProcessor.main()