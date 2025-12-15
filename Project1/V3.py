import sys
import math
from collections import defaultdict

from Project1.data import runtests


# ------------------------------------------------------------
# Funkcja rozkładająca liczbę na czynniki pierwsze
# Zwraca słownik: prime -> exponent
# ------------------------------------------------------------
def factorize_number(number):
    factors = defaultdict(int)

    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors[divisor] += 1
            number //= divisor
        divisor += 1

    if number > 1:
        factors[number] += 1

    return factors


# ------------------------------------------------------------
# Generowanie wszystkich dzielników na podstawie faktoryzacji
# ------------------------------------------------------------
def generate_all_divisors(prime_factors):
    divisors = [1]

    for prime, exponent in prime_factors.items():
        new_divisors = []
        current_power = 1

        for _ in range(exponent):
            current_power *= prime
            for existing_divisor in divisors:
                new_divisors.append(existing_divisor * current_power)

        divisors.extend(new_divisors)

    return divisors


# ------------------------------------------------------------
# Główne rozwiązanie
# ------------------------------------------------------------
def solve( scores ) :
    input_data = sys.stdin.read().strip().split()
    input_index = 0

    number_of_elements = int(input_data[input_index])
    input_index += 1

    values = []
    luck_values = []

    for _ in range(number_of_elements):
        value = int(input_data[input_index])
        luck = float(input_data[input_index + 1])
        input_index += 2

        values.append(value)
        luck_values.append(luck)

    # --------------------------------------------------------
    # Słownik: divisor -> suma luck dla wszystkich liczb
    # podzielnych przez ten divisor
    # --------------------------------------------------------
    total_luck_for_divisor = defaultdict(float)

    for index in range(number_of_elements):
        current_value = values[index]
        current_luck = luck_values[index]

        prime_factors = factorize_number(current_value)
        all_divisors = generate_all_divisors(prime_factors)

        for divisor in all_divisors:
            total_luck_for_divisor[divisor] += current_luck

    # --------------------------------------------------------
    # Szukanie najlepszego wyniku
    # --------------------------------------------------------
    best_result = 0.0

    for divisor, summed_luck in total_luck_for_divisor.items():
        current_score = summed_luck - 5.0 * math.log10(divisor)
        if current_score > best_result:
            best_result = current_score

    # --------------------------------------------------------
    # Wynik
    # --------------------------------------------------------
    print(best_result)


# ------------------------------------------------------------
# Uruchomienie
# ------------------------------------------------------------
runtests( solve )