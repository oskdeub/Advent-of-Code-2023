def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

def main():

    lines = read_file('example1.txt')
    print(str(len(lines)))
    for x in range(0, len(lines)):
        x.replace('\n', '')
        print(x)
    
if __name__ == "__main__":
    main()