def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

def main():

    lines = read_file('example1.txt')
    #find rows cols with no galaxies #
    #expand empty rows + cols
    #find shortest paths between galaxies, only going up, down, left or right
    

    print(sum)
if __name__ == "__main__":
    main()