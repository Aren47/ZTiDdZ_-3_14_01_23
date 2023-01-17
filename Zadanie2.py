import random

a = '0987654321QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlzZXxCcVvBbNnMm!@#$%^&*()_+1234567890'

dlugosc_hasla = 9

haslo = ''.join(random.sample(a,dlugosc_hasla))
print(haslo)