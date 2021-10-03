def get_perfect_squares(start: int, end: int):
    for i in range(start, end + 1):
        x = math.sqrt(i)
        if int(x) ** 2 == i:
            print(i, " ")
def main():
    print(get_perfect_squares(5, 16))

if __name__ == "__main__":
    main()