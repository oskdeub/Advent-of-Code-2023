def read_file(filename):
    with open (filename) as input:
        lines = input.readlines()
    input.close()
    return lines

def find_first_number(string):
    for x in string:
        if x.isdigit():
            return x

# --- Joins the first and last number of string into a two-digit number ---
def get_calibration_value(string):
    reverse_string = string[::-1]
    first_num = find_first_number(string)
    last_num = find_first_number(reverse_string)
    number = first_num + last_num
    return int(number)

# --- Inserts number into index 1 of string ---
def insert_number_after_head(string, number):
    
    return string[:1] + str(number) + string[1:]
    
def replace_spelled_numbers(string):

    num_dict = {
        "one"   :   1,
        "two"   :   2,
        "three" :   3,
        "four"  :   4,
        "five"  :   5,
        "six"   :   6,
        "seven" :   7,
        "eight" :   8,
        "nine"  :   9
    }
    
    #Find spelled numbers in string, insert their corresponding number into the substring 
    for x in num_dict.keys():
        if x in string:
            nSubstring = insert_number_after_head(x, num_dict[x])
            string = string.replace(x, nSubstring)
    return string

def main():
    lines = read_file('input.txt')
    
    for x in range(0, len(lines)):
        lines[x] = replace_spelled_numbers(lines[x])
        
    sum = 0
    for x in lines:
        sum += get_calibration_value(x)
    print(sum)
    
if __name__ == "__main__":
    main()

