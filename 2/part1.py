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