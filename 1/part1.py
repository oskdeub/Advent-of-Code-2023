
def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

def find_first_number(string):
    for x in string:
        if x.isdigit():
            return x
        
def get_calibration_value(string):
    reverse_string = string[::-1]
    first_num = find_first_number(string)
    last_num = find_first_number(reverse_string)
    number = first_num + last_num
    return int(number)

def main():

    lines = read_file('input.txt')
    sum = 0
    for x in lines:
        sum += get_calibration_value(x)
    print(sum)
    
if __name__ == "__main__":
    main()

