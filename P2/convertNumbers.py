import sys
import time

# Function to read numbers from a file and handle invalid data
def read_file(file_path):
    """Reads numbers from a file and handles invalid data."""
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())  # Attempt to convert each line to an integer
                numbers.append(num)
            except ValueError:
                print(f"Invalid data encountered and ignored: {line.strip()}")  # Warn about invalid data
    return numbers

# Function to convert a number to binary using basic algorithms
def to_binary(number):
    """Converts a number to binary."""
    if number == 0:
        return "0"  # Binary of 0 is "0"
    is_negative = number < 0
    number = abs(number)  # Work with the absolute value
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary  # Build the binary representation
        number //= 2
    return binary if not is_negative else f"-{binary}"  # Add negative sign if needed

# Function to convert a number to hexadecimal using basic algorithms
def to_hexadecimal(number):
    """Converts a number to hexadecimal."""
    if number == 0:
        return "0"  # Hexadecimal of 0 is "0"
    is_negative = number < 0
    number = abs(number)  # Work with the absolute value
    hex_chars = "0123456789ABCDEF"  # Characters for hexadecimal digits
    hexadecimal = ""
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal  # Build the hexadecimal representation
        number //= 16
    return hexadecimal if not is_negative else f"-{hexadecimal}"  # Add negative sign if needed

# Main function to read a file, convert numbers, and save results
def main():
    """Main program to convert numbers to binary and hexadecimal."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <fileWithData.txt>")  # Check for correct usage
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        start_time = time.time()  # Record the start time
        data = read_file(file_path)  # Read and validate the data from the file

        if not data:
            print("No valid data to process.")
            sys.exit(1)

        result_lines = []
        result_lines.append("NUMBER\tBIN\tHEX\n")  # Add header row
        for number in data:
            binary = to_binary(number)  # Convert to binary
            hexadecimal = to_hexadecimal(number)  # Convert to hexadecimal
            result_lines.append(f"{number}\t{binary}\t{hexadecimal}\n")  # Save results

        elapsed_time = time.time() - start_time  # Calculate elapsed time

        result_summary = (
            f"File: {file_path}\n"
            f"Time Elapsed: {elapsed_time:.6f} seconds\n\n"
        )

        # Append results to the output file
        with open("ConvertionResults.txt", "a") as output_file:
            output_file.writelines(result_lines)
            output_file.write(result_summary)

        # Print results to the console
        print("".join(result_lines))
        print(result_summary)

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")  # Handle file not found error
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other errors
        sys.exit(1)

if __name__ == "__main__":
    main()