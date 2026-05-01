def is_armstrong_number(number):
    
    number_str = str(number)
    number_len = len(number_str)
    sum_digits = 0

    for digit in number_str:
        sum_digits += pow(int(digit), number_len)

    if number == sum_digits:
        return True
    return False