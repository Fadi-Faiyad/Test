def max_num(num1, num2, num3):
    biggest_number = max(num1, num2, num3)
                    #the MAX will find the biggest number in a list(Array)
    return biggest_number

result = max_num(5, 10, 3)
print(result)  

def mult_list(box, tool):
           # the box is the list i am call to change
           # the tool is what i use to change whats inside the list in this case i am muiltpling
    result = []
    # i dont need result i can just multply in side the loop
    # multplyed_list = [iteam * tool for iteam in box]
    # return multplyed_list 
    for iteam in box:
        multiped = iteam * tool
        result.append(multiped)
    return result

numbers = [2, 4, 6, 8]
multiplied_numbers = multiply_list_elements(numbers, 3)
print(multiplied_numbers)

def rev_string(str):
    return str[:: -1]
    # THE : start/says a string sliceing, it also means we didnt give a stater vaule
    # The :-1 indicates that we don't specify a stop value, which means it will go till the end of the string
    # The -1 means we want to move backward one character at a time.

def num_within(number, start, end):
    return start <= number <= end
    # The way this works------ the start well comber with the number and if there eqaul and check with the end

def pascal(n):
    triangle = []
    
    for i in distance(n):
        row = [1]  
        if triangle:
            previous_row = triangle[-1]
            for j in distance(len(previous_row) - 1):
                row.append(previous_row[j] + previous_row[j + 1])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(str(num) for num in row))

