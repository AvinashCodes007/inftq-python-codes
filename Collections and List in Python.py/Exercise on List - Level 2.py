def get_count(num_list):
    count=0
    for i in range(1,len(num_list)):
        
        if num_list[i-1]==num_list[i]:
            count+=1
    return count
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))

# 2nd method

def check_adjacent_duplicates(numbers_list):
    adjacent_count = 0
    previous_number = 0

    for number in numbers_list:
        if previous_number == number:
            adjacent_count += 1
        previous_number = number

    return adjacent_count


numbers_list = [1, 1, 5, 100, -20, -20, 6, 0, 0]
adjacent_count = check_adjacent_duplicates(numbers_list)
print("Count of adjacent occurrences:", adjacent_count)

    
 


