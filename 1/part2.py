
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
    #print(number)
    return int(number)
        
def replace_spelled_numbers(string):
    
    #print("finding spelled numbers for " + string)
    spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_dict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    
    found_dict = {}
    indexes = []
    for x in spelled_numbers:
        if x in string:
            print(x + " found at index " + str(string.index(x)))
            found_dict[string.index(x)] = x
            indexes.append(string.index(x))

    '''
    if len(found_dict) > 0:
        order = sorted(found_dict.keys())
        string = string.replace(found_dict[order[0]], str(num_dict[found_dict[order[0]]]), 1)
        print(string)
    '''
    order = sorted(found_dict.keys())
    print(order)
    for x in order:
        #print(found_dict[x])
        #print(num_dict[found_dict[x]])
        new_substring = found_dict[x]
        new_substring = new_substring[:1] + str(num_dict[found_dict[x]]) + new_substring[1:]
        
        string = string.replace(found_dict[x], new_substring)
        
        print(string)
        print("")
        
        # e8ighto1ne8ight = eight8one1i
    '''   
    for x in spelled_numbers:
        if x in string:
            return replace_spelled_numbers(string)
    ''' 
    return string

def main():

    lines = read_file('example2.txt')
    #lines = ["oneight"]

    for x in range(0, len(lines)):
        print("------------------------------")
        print(lines[x])
        lines[x] = replace_spelled_numbers(lines[x])
        print(lines[x])
        print("------------------------------")
    sum = 0
    for x in lines:
        sum += get_calibration_value(x)
    print(sum)
    
if __name__ == "__main__":
    main()

