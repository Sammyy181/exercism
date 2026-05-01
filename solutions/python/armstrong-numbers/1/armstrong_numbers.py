def is_armstrong_number(number):
    
    number_str = str(number)
    number_len = len(number_str)
    sum = 0

    for digit in number_str:
        sum += pow(int(digit), number_len)

    if number == sum:
        return True
    return False