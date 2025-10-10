import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Commented out stuff:

        # daytuh = [["M", "Brown", "Brown", "5'8\"", 160],
        #         ["F", "Blonde", "Blue", "5'5\"", 110],
        #         ["F", "Brown", "Blue", "4'0\"", 60],
        #         ["M", "Blonde", "Brown", "4'8\"", 100],
        #         ["M", "Blonde", "Brown", None, None],
        #         ["F", "Blonde", "Blue", None, None]]

        # x = pd.DataFrame(daytuh, columns = ["Gender", "Hair Color", "Eye Color", "Height", "Weight (lbs)"], index = ["Parker Nelson", "Ava Nelson", "Margot Nelson", "Beckham Nelson", "Vincent Nelson", "Rory Nelson"])

        # x.loc["Michael Nelson"] = ["M", "Brown", "Blue", "6'0\"", 225]
        # x.loc["Amelia Nelson"] = ["F", "Blonde", "Blue", "5'6\"", 150]

        # x.loc["Canyon Hunter"] = ["M", "Brown", "Brown", "5'7\"", 200]
        # x.loc["Marisa Hunter"] = ["F", "Brown", "Brown", "5'2\"", 125]
        # x.loc["Crew Hunter"] = ["M", "Brown", "Brown", None, None]
        # x.loc["Sunday Hunter"] = ["F", "Brown", "Brown", None, None]
        # x.loc["Cohen Hunter"] = ["M", "Brown", "Brown", None, None]

        # x.loc["Morgan Nelson"] = ["M", "Brown", "Brown", "5'7\"", 200]
        # x.loc["Gina Nelson"] = ["F", "Brown", "Brown", "5'2\"", 170]
        # x.loc["Reagan Nelson"] = ["M", "Brown", "Brown", "5'0\"", 160]

        # x.loc["Rhett Neuenschwander"] = ["M", "Brown", "Blue", "6'0\"", 185,]
        # x.loc["Brooke Neuenschwander"] = ["F", "Red", "Blue", "5'5\"", 135]
        # x.loc["Anders Neuenschwander"] = ["M", "Brown", "Blue", "6'1\"", 190]
        # x.loc["Sadie Neuenschwander"] = ["F", "Brown", "Blue", "5'6\"", 120]
        # x.loc["Liam Neuenschwander"] = ["M", "Blonde", "Blue", "5'10\"", 140]

        # x["Age"] = [36, 36, 6, 8, 4, 2, 39, 34, 37, 37, 17, 15, 13, 71, 71, 33, 63, 62, 34, 31, 29]
        # x["Birth Year"] = 2037 - x["Age"]

        # x["Gender01"] = [1 if i == "M" else 0 if i == "F" else np.nan for i in x["Gender"]]

        # print(x)

        # # sns.scatterplot(data = x, x = 'Gender01', y = 'Weight (lbs)')
        # # plt.show()

        # x.to_csv("family_data.csv", index=True)
        # y = pd.read_csv("sw.csv", index_col=0)
        # y.to_excel("sw.xlsx", index=True)
        # # print(y)

        # z = pd.read_csv("tvShows.csv", index_col = 0)
        # z["year"] = z["year"].astype(str)   
        # z.to_excel("tvShows.xlsx", index = True)


tvShowData = pd.read_csv("tvShows.csv")

fiveStar = tvShowData.loc[tvShowData["rating"] == 5]
fourStar = tvShowData.loc[tvShowData["rating"] == 4]
threeStar = tvShowData.loc[tvShowData["rating"] == 3]
twoStar = tvShowData.loc[tvShowData["rating"] == 2]
oneStar = tvShowData.loc[tvShowData["rating"] == 1]

fiveStar.to_csv("five_star_shows.csv", index=False)
fourStar.to_csv("four_star_shows.csv", index=False)
threeStar.to_csv("three_star_shows.csv", index=False)
twoStar.to_csv("two_star_shows.csv", index=False)
oneStar.to_csv("one_star_shows.csv", index=False)

movieData = pd.read_csv("movies.csv")

movieFiveStar = movieData.loc[movieData["rating"] == 5]
movieFourStar = movieData.loc[(movieData["rating"] == 4) | (movieData["rating"] == 4.5)]
movieThreeStar = movieData.loc[(movieData["rating"] == 3) | (movieData["rating"] == 3.5)]
movieTwoStar = movieData.loc[(movieData["rating"] == 2) | (movieData["rating"] == 2.5)]
movieOneStar = movieData.loc[(movieData["rating"] == 1) | (movieData["rating"] == 1.5)]

movieFiveStar.to_csv("five_star_shows.csv", index=False)
movieFourStar.to_csv("four_star_shows.csv", index=False)
movieThreeStar.to_csv("three_star_shows.csv", index=False)
movieTwoStar.to_csv("two_star_shows.csv", index=False)
movieOneStar.to_csv("one_star_shows.csv", index=False)

def format_counter(num):
    if num < 10:
        return f"{num}.    "
    elif num < 100:
        return f"{num}.   "
    elif num < 1000:
        return f"{num}.  "
    elif num < 10000:
        return f"{num}. "
    else:
        return f"{num}."
while True:
    clear_screen()
    response = input("Welcome to Parker's Movie and TV-Show reviews:\nWould you like to see movies or tv-shows? (M/T) ")
    if response.strip() == "":
        print("\nExiting program. Goodbye!")
        break
    elif response.strip().upper() in ["M", "MOVIES"]:
        while True:
            clear_screen()
            print("\nYou are now viewing movie ratings! (Press Enter on an empty line to return to the main menu.)\n")
            responseOne = input("Input the number corresponding to the star rating you would like to see: ")
            if responseOne.strip() == "":
                clear_screen()
                print("\nReturning to main menu...\n")
                break
            clear_screen()
            if int(responseOne) == 5:
                print(f"5-Star Ratings ({len(movieFiveStar)}):\n")
                movieFiveStarCounter = 0
                for _, row in movieFiveStar.iterrows():
                    movieFiveStarCounter += 1
                    print(f"{format_counter(movieFiveStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 4:
                print(f"\n\n\n4-Star Ratings ({len(movieFourStar)}):\n")
                movieFourStarCounter = 0
                for _, row in movieFourStar.iterrows():
                    movieFourStarCounter += 1
                    print(f"{format_counter(movieFourStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 3:
                print(f"\n\n\n3-Star Ratings ({len(movieThreeStar)}):\n")
                movieThreeStarCounter = 0
                for _, row in movieThreeStar.iterrows():
                    movieThreeStarCounter += 1
                    print(f"{format_counter(movieThreeStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 2:
                print(f"\n\n\n2-Star Ratings ({len(movieTwoStar)}):\n")
                movieTwoStarCounter = 0
                for _, row in movieTwoStar.iterrows():
                    movieTwoStarCounter += 1
                    print(f"{format_counter(movieTwoStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 1:
                print(f"\n\n\n1-Star Ratings ({len(movieOneStar)}):\n")
                movieOneStarCounter = 0
                for _, row in movieOneStar.iterrows():
                    movieOneStarCounter += 1
                    print(f"{format_counter(movieOneStarCounter)}({row['rating']})  ||  {row['name']}")
            else:
                clear_screen()
                print("\nInvalid star rating. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue...")
            clear_screen()
    elif response.strip().upper() in ["T", "TV SHOWS"]:
        while True:
            clear_screen()
            print("\nYou are now viewing TV show ratings! (Press Enter on an empty line to return to the main menu.)\n")
            responseOne = input("Input the number corresponding to the star rating you would like to see: ")
            if responseOne.strip() == "":
                clear_screen()
                print("\nReturning to main menu...\n")
                break
            clear_screen()
            if int(responseOne) == 5:
                print(f"5-Star Ratings ({len(fiveStar)}):\n")
                fiveStarCounter = 0
                for _, row in fiveStar.iterrows():
                    fiveStarCounter += 1
                    print(f"{format_counter(fiveStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 4:
                print(f"\n\n\n4-Star Ratings ({len(fourStar)}):\n")
                fourStarCounter = 0
                for _, row in fourStar.iterrows():
                    fourStarCounter += 1
                    print(f"{format_counter(fourStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 3:
                print(f"\n\n\n3-Star Ratings ({len(threeStar)}):\n")
                threeStarCounter = 0
                for _, row in threeStar.iterrows():
                    threeStarCounter += 1
                    print(f"{format_counter(threeStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 2:
                print(f"\n\n\n2-Star Ratings ({len(twoStar)}):\n")
                twoStarCounter = 0
                for _, row in twoStar.iterrows():
                    twoStarCounter += 1
                    print(f"{format_counter(twoStarCounter)}({row['rating']})  ||  {row['name']}")
            elif int(responseOne) == 1:
                print(f"\n\n\n1-Star Ratings ({len(oneStar)}):\n")
                oneStarCounter = 0
                for _, row in oneStar.iterrows():
                    oneStarCounter += 1
                    print(f"{format_counter(oneStarCounter)}({row['rating']})  ||  {row['name']}")
            else:
                clear_screen()
                print("\nInvalid star rating. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue...")
            clear_screen()
    else:
        clear_screen()
        print("\nInvalid input. Please type 'M' for movies or 'T' for TV shows.")


# Print Statements

    # print("5-Star Ratings: \n")
    # fiveStarCounter = 0
    # for name in fiveStar["name"]:
    #     fiveStarCounter += 1
    #     print(f"{fiveStarCounter}. {name}")

    # print("\n\n\n4-Star Ratings:\n")
    # fourStarCounter = 0
    # for name in fourStar["name"]:
    #     fourStarCounter += 1
    #     print(f"{fourStarCounter}. {name}")

    # print("\n\n\n3-Star Ratings:\n")
    # threeStarCounter = 0
    # for name in threeStar["name"]:
    #     threeStarCounter += 1
    #     print(f"{threeStarCounter}. {name}")

    # print("\n\n\n2-Star Ratings:\n")
    # twoStarCounter = 0
    # for name in twoStar["name"]:
    #     twoStarCounter += 1
    #     print(f"{twoStarCounter}. {name}")

    # print("\n\n\n1-Star Ratings:\n")
    # oneStarCounter = 0
    # for name in oneStar["name"]:
    #     oneStarCounter += 1
    #     print(f"{oneStarCounter}. {name}")


    # print("5-Star Ratings:\n")
    # movieFiveStarCounter = 0
    # for name in movieFiveStar["name"]:
    #     movieFiveStarCounter += 1
    #     print(f"{movieFiveStarCounter}. {name}")

    # print("\n\n\n4-Star Ratings:\n")
    # movieFourStarCounter = 0
    # for name in movieFourStar["name"]:
    #     movieFourStarCounter += 1
    #     print(f"{movieFourStarCounter}. {name}")

    # print("\n\n\n3-Star Ratings:\n")
    # movieThreeStarCounter = 0
    # for name in movieThreeStar["name"]:
    #     movieThreeStarCounter += 1
    #     print(f"{movieThreeStarCounter}. {name}")

    # print("\n\n\n2-Star Ratings:\n")
    # movieTwoStarCounter = 0
    # for name in movieTwoStar["name"]:
    #     movieTwoStarCounter += 1
    #     print(f"{movieTwoStarCounter}. {name}")

    # print("\n\n\n1-Star Ratings:\n")
    # movieOneStarCounter = 0
    # for name in movieOneStar["name"]:
    #     movieOneStarCounter += 1
    #     print(f"{movieOneStarCounter}. {name}")






