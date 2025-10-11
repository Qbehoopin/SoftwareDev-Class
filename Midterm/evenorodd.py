# evenorodd.py

def main():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()