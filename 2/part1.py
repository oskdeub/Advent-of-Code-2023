'''
Each time you play this game, he will hide a secret number of cubes of each color in the bag, 
and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, 
the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). 
Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game one, three sets of cubes are revealed from the bag, and then put back again.
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; The third set is only 2 green cubes.

The elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible beacause at one point the Elf showed you 20 red cubes at once;
similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
If you add up add up the IDs of the game that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?
'''
import re
import time

def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

def load_bag(r, g, b):
    bag = [r, g, b]
    return bag

def get_game_id(game):
    return game.split(':', 1)[0][4:]

def get_bag_items(game):
    bags = game.split(':', 1)[1]
    bags = bags.replace('\n', '')
    return bags.split(';')

def split_into_color_array(items):
    split_items = items.split(',')
    red = 0
    green = 0
    blue = 0
    for x in split_items:
        x = x.split(' ')
        if 'red' in x:
            red = int(x[1])
        elif 'green' in x:
            green = int(x[1])
        elif 'blue' in x:
            blue = int(x[1])
        #print(x)
    bag_pick =[red, green, blue]
    #print(bag_pick)
    return bag_pick

def test_bag(game):
    
    gameID = int(get_game_id(game))
    #print(game)
    items = get_bag_items(game)
    games = [gameID]
    for i in items:
        games.append(split_into_color_array(i))
    return games

def evaluate_game(id_picks, bag):
    id = id_picks[0]
    #print("id: " + str(id))
    for i in id_picks[1:]:
        #print(i)
        if (i[0] > bag[0]) or (i[1] > bag[1]) or (i[2] > bag[2]):
            #print("IMPOSSIBLE!!!!!")
            return 0
    return id

def evaluate_games(games, bag):
    sum = 0
    for pick in games:
        sum += evaluate_game(pick, bag)
        #print('Sum = ' + str(sum))
        #time.sleep(2)
    return sum        

def main():

    lines = read_file('input.txt')
    bag = load_bag(12, 13, 14)
    games = []
    for x in lines:
        games.append(test_bag(x))
    
    print(evaluate_games(games, bag))
    #All bag picks are now nicely formatted :)
    
if __name__ == "__main__":
    main()