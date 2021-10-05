import math


def get_leap_years(start: int, end: int) -> list[int]:
    list = []
    for i in range(start, end + 1):
        if i % 4 == 0:
            list.append(i)
    return list
def test_get_leap_years():
    assert get_leap_years(2000, 2008) == [2000, 2004, 2008]
    assert get_leap_years(2000, 2009) == [2000, 2004, 2008]
    assert get_leap_years(2015, 2025) == [2016, 2020, 2024]

def get_perfect_squares(start: int, end: int) -> list[int]:
    list = []
    for i in range(start, end + 1):
        x = math.sqrt(i)
        if int(x + 0.5) ** 2 == i:
            list.append(i)
    return list
def test_get_perfect_squares():
    assert get_perfect_squares(5, 16) == [9, 16]
    assert get_perfect_squares(23, 55) == [25, 36, 49]
    assert get_perfect_squares(62, 90) == [64, 81]

def is_palindrome(n) -> bool:
    n1 = 0
    n2 = n
    while n2:
        n1 = n1 * 10
        n1 = n1 + n2 % 10
        n2 = n2 // 10
    if n1 == n:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(12) is False
    assert is_palindrome(121) is True
    assert is_palindrome(5) is True

def main():
    while True:
        print('5. Determină dacă un număr dat este palindrom.')
        print('11. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).')
        print('12. Afișează toate pătratele perfecte dintr-un interval închis dat.')
        print('x. Iesire din program - exit.')
        optiune = input('Alege optiunea: ')
        if optiune == '5':
            n = int(input("Cititi numarul: "))
            print(is_palindrome(n))
        elif optiune == '11':
            start = int(input('Inceput: '))
            end = int(input('Sfarsit: '))
            print(get_leap_years(start, end))
        elif optiune == '12':
            start = int(input('Inceput: '))
            end = int(input('Sfarsit: '))
            print(get_perfect_squares(start, end))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

test_get_leap_years()
test_get_perfect_squares()
test_is_palindrome()
main()