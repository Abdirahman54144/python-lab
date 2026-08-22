from utils import square, is_even, celsius_to_fahrenheit

def run_program():
    try:
        val = float(input("Enter a number: "))
        print(f"Square of {val}: {square(val)}")
        print(f"Is {val} even?: {is_even(int(val))}")
        print(f"{val}°C in Fahrenheit: {celsius_to_fahrenheit(val)}°F")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    run_program()
