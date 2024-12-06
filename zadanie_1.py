def is_valid_string(s):
    return len(s) >= 3

cities = input("Введите названия городов через пробел: ").split()

valid_cities = [city for city in cities if is_valid_string(city)]

print(valid_cities)
