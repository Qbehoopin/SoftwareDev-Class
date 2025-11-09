"""Flow Chart to Python Code Example

This module documents a simple flowchart logic and contains a Python implementation.

Flowchart:
Start
count = 0
sum = 0
repeat
    Prompt user for a score
    score = input -> float
    sum = sum + score
    counter = counter + 1
repeat while (counter < 5)
average = sum / 5
if (average >= 70) then (yes)
    display "Passed - Average: " + average
else (no)
    display "Failed - Average: " + average
endif
Stop
"""

# Python Code Implementation
def main():
    total = 0.0
    for i in range(1, 6):
        try:
            score = float(input(f"Enter score {i}: "))

            total += score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
            while True:
                try:
                    score = float(input(f"Enter score {i} (retry): "))
                    total += score
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

    average = total / 5
    status = "Passed" if average >= 70 else "Failed"
    print(f"{status} - Average: {average:.2f}")

if __name__ == "__main__":
    main()

