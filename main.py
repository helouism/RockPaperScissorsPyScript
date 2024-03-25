import random
from pyscript import document

games_result = []

# Dictionary of all of the possible outcome 
combinations = {
    11 : "Computer picks Rock too, It's a Draw",
    22 : "Computer picks Paper too, It's a Draw",
    33 : "Computer picks Scissors too, It's a Draw",
    12 : "Computer picks Paper, You Lose",
    13 : "Computer picks Scissors, You Win",
    21 : "Computer picks Rock, You Win",
    23 : "Computer picks Scissors, You Lose",
    31 : "Computer picks Rock, You Lose",
    32 : "Computer picks Paper, You Win"
}

class Game:

        # Access combinations key to output the winner

    def rock(event):
        games_result.append(str(1))
        games_result.append(str(random.randint(1,3)))
        games_result_converted = "".join(games_result)
        output_div = document.querySelector("#output")
        output_div.innerText = combinations[int(games_result_converted)]
        games_result.clear()


    def paper(event):
        games_result.append(str(2))
        games_result.append(str(random.randint(1,3)))
        games_result_converted = "".join(games_result)
        print(combinations[int(games_result_converted)])
        output_div = document.querySelector("#output")
        output_div.innerText = combinations[int(games_result_converted)]
        games_result.clear()

    def scissors(event):
        games_result.append(str(3))
        games_result.append(str(random.randint(1,3)))
        games_result_converted = "".join(games_result)
        print(combinations[int(games_result_converted)])
        output_div = document.querySelector("#output")
        output_div.innerText = combinations[int(games_result_converted)]
        games_result.clear()
