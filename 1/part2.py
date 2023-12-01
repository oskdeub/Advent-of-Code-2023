
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

def replace_spelled_numbers(string):
    
    #print("finding spelled numbers for " + string)
    spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_dict = {
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
    
    found_spelled_numbers = {}
    
    for x in spelled_numbers:
        if x in string:
            #print(x + " found at index " + str(string.index(x)))
            found_spelled_numbers[string.index(x)] = x
            # string = string.replace(x, str(num))
            # Problem, eightwothree should return 83, not eigh23. Since it checks for two before eight this become wrong.
            # The number found first is priority, so index matters here.
        
    #print(string)
    
    if len(found_spelled_numbers) > 0:
        #print(found_spelled_numbers)
        order = sorted(found_spelled_numbers.keys())
        #print(order[0])
        #print(found_spelled_numbers[order[0]])
        string = string.replace(found_spelled_numbers[order[0]], str(numbers_dict[found_spelled_numbers[order[0]]]))
        #print(string)
    
    for x in spelled_numbers:
        if x in string:
            return replace_spelled_numbers(string)
    
    return string
    #now only replace them one at a time, to make sure none goes lost when the substring is replaced with a number
    
    #Replace first found spelled number with corresponding number using the numbers_dict dictionary.
    
            

def main():

    lines = read_file('example2.txt')

    for x in range(0, len(lines)):
        lines[x] = replace_spelled_numbers(lines[x])
        print(lines[x])
    
    sum = 0
    for x in lines:
        sum += get_calibration_value(x)
    print(sum)
    
if __name__ == "__main__":
    main()

