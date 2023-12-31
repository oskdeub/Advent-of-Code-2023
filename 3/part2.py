import re

def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

symbols = '@#%&=-+?/$*'

def isSymbol(ch):
    if ch in symbols:
        return True
    return False

def get_sym_coords(lines):
    sym_coords = []
    for i in lines:
        for s in symbols:
            if s in i:
                #print(s + " " + str(lines.index(i)) + ", "+ str(i.index(s)))
                sym_coords.append([lines.index(i), i.index(s)])
    return sym_coords

def check_line(y, i_s, i_e, line):
    start = i_s
    end = i_e
    
    #Offset start and end by 1 to include symbols in the corners, but only if not outside of line range 0, 9
    if i_s > 0:
        start = start -1
    if i_e < (len(line) - 1):
        end = end + 1
    for i in range(start, end+1):
        if isSymbol(line[i]):
            return True
    return False

def check_before(x, line):
    if isSymbol(line[x-1]):
        return True
    return False

def check_after(x, line):
    if isSymbol(line[x+1]):
        return True
    return False

def find_symbols_adjacent(y, i_start, i_end, lines):
    top_row = False
    bot_row = False
    if y == 0:
        top_row = True
    elif y == len(lines)-1:
        bot_row = True
    
    if not top_row:
        if check_line(y, i_start, i_end, lines[y-1]):
            return True
    if not bot_row:
        if check_line(y, i_start, i_end, lines[y+1]):
            return True
        
    if i_start > 0:
        if check_before(i_start, lines[y]):
            return True
    
    if i_end < len(lines) - 1:
        if check_after(i_end, lines[y]):
            return True
    
    return False

def main():

    lines = read_file('input.txt')

    sum = 0
    
    sym_coord = get_sym_coords(lines)
    
    """for y in range (0, len(lines)):
        nums = re.findall(r'\d+', lines[y])
        for i in nums:
            i_start = lines[y].index(i)
            i_end = lines[y].index(i) + len(i) - 1
            #replaces the number found in the line
            #print("{}, {} - {}".format(i, i_start, i_end ))
            if find_symbols_adjacent(y, i_start, i_end, lines):
                print("{}   found @     {},{}".format(int(i), y, i_start))
                sum = sum + int(i)

    print(sum)
    """
if __name__ == "__main__":
    main()