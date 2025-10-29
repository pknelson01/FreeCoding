import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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

tvShowData = pd.read_csv("tvShows.csv")
movieData = pd.read_csv("movies.csv")

fiveStar = tvShowData.loc[tvShowData["rating"] == 5]
fourStar = tvShowData.loc[tvShowData["rating"] == 4]
threeStar = tvShowData.loc[tvShowData["rating"] == 3]
twoStar = tvShowData.loc[tvShowData["rating"] == 2]
oneStar = tvShowData.loc[tvShowData["rating"] == 1]

movieFiveStar = movieData.loc[movieData["rating"] == 5]
movieFourStar = movieData.loc[movieData["rating"] == 4]
movieFourHalfStar = movieData.loc[movieData["rating"] == 4.5]
movieThreeStar = movieData.loc[movieData["rating"] == 3]
movieThreeHalfStar = movieData.loc[movieData["rating"] == 3.5]
movieTwoStar = movieData.loc[movieData["rating"] == 2]
movieTwoHalfStar = movieData.loc[movieData["rating"] == 2.5]
movieOneStar = movieData.loc[movieData["rating"] == 1]
movieOneHalfStar = movieData.loc[movieData["rating"] == 1.5]

while True:
    clear_screen()
    response = input("Welcome to Parker's Movie and TV-Show reviews:\nWould you like to see movies or tv-shows? (M/T)\n(Press Enter to exit): ")
    if response.strip() == "":
        clear_screen()
        print("Generating charts...")

        tv_counts = tvShowData["rating"].value_counts().sort_index()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=tv_counts.index, y=tv_counts.values, palette="coolwarm")
        plt.title("TV Show Ratings Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Number of Shows")
        plt.tight_layout()
        plt.savefig("tvshow_ratings_chart.png")
        plt.close()

        movie_counts = movieData["rating"].value_counts().sort_index()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=movie_counts.index, y=movie_counts.values, palette="magma")
        plt.title("Movie Ratings Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")
        plt.tight_layout()
        plt.savefig("movie_ratings_chart.png")
        plt.close()

        print("Charts saved as 'movie_ratings_chart.png' and 'tvshow_ratings_chart.png'.")
        print("Exiting program. Goodbye!")
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
            rating = float(responseOne)
            if rating == 5:
                print(f"5-Star Ratings ({len(movieFiveStar)}):\n")
                for i, row in enumerate(movieFiveStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 4:
                print(f"4-Star Ratings ({len(movieFourStar)}):\n")
                for i, row in enumerate(movieFourStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 4.5:
                print(f"4.5-Star Ratings ({len(movieFourHalfStar)}):\n")
                for i, row in enumerate(movieFourHalfStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 3:
                print(f"3-Star Ratings ({len(movieThreeStar)}):\n")
                for i, row in enumerate(movieThreeStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 3.5:
                print(f"3.5-Star Ratings ({len(movieThreeHalfStar)}):\n")
                for i, row in enumerate(movieThreeHalfStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 2:
                print(f"2-Star Ratings ({len(movieTwoStar)}):\n")
                for i, row in enumerate(movieTwoStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 2.5:
                print(f"2.5-Star Ratings ({len(movieTwoHalfStar)}):\n")
                for i, row in enumerate(movieTwoHalfStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 1:
                print(f"1-Star Ratings ({len(movieOneStar)}):\n")
                for i, row in enumerate(movieOneStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif rating == 1.5:
                print(f"1.5-Star Ratings ({len(movieOneHalfStar)}):\n")
                for i, row in enumerate(movieOneHalfStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            else:
                print("\nInvalid star rating. Please enter a number between 1 and 5 (or .5 ratings).")
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
                for i, row in enumerate(fiveStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif int(responseOne) == 4:
                print(f"4-Star Ratings ({len(fourStar)}):\n")
                for i, row in enumerate(fourStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif int(responseOne) == 3:
                print(f"3-Star Ratings ({len(threeStar)}):\n")
                for i, row in enumerate(threeStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif int(responseOne) == 2:
                print(f"2-Star Ratings ({len(twoStar)}):\n")
                for i, row in enumerate(twoStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            elif int(responseOne) == 1:
                print(f"1-Star Ratings ({len(oneStar)}):\n")
                for i, row in enumerate(oneStar.itertuples(), start=1):
                    print(f"{format_counter(i)}({row.rating})  ||  {row.name}")
            else:
                print("\nInvalid star rating. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue...")
            clear_screen()
    else:
        clear_screen()
        print("\nInvalid input. Please type 'M' for movies or 'T' for TV shows.")
