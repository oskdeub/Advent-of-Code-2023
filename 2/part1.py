# bag of red, green, or blue cubes
# each time we play, the elf hides a secret amount of cubes of each color in the bag
# Goal: Figure out information about the number of cubes

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, 
# show them to you, and then put them back in the bag. He'll do this a few times per game.

# you play several games and keep track of each the infromation from the games. (puzzle input)
# Each game is listen with an ID number followed by a semicolon-separated list of subsets of cubes that were revealed from the bag.
#For example, the record of a few games might look like this:
'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

