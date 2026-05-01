def leap_year(year):
    if not year % 4:
        if year % 100:
            return True
        if not year % 400:
            return True
    return False
