import sys
import time

# Function to read numbers from a file and handle invalid data
def read_file(file_path):
    """Reads numbers from a file and handles invalid data."""
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                num = float(line.strip())  # Attempt to convert each line to a float
                # Check for overly large or infinite values
                if num == float('inf') or num == float('-inf') or abs(num) > 1e308:
                    print(f"Invalid data due to overflow or large magnitude ignored: {num}")
                    continue
                numbers.append(num)
            except ValueError:
                print(f"Invalid data encountered and ignored: {line.strip()}" )  # Warn about invalid data
    return numbers

# Function to compute the mean using basic algorithms
def compute_mean(data):
    """Computes the mean."""
    return sum(data) / len(data)  # Calculate the average

# Function to compute the median using basic algorithms
def compute_median(data):
    """Computes the median."""
    sorted_data = sorted(data)  # Sort the data
    n = len(sorted_data)
    mid = n // 2
    # Return the middle value or the average of the two middle values
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

# Function to compute the mode using basic algorithms
def compute_mode(data, skip_mode=False):
    """Computes the mode."""
    if skip_mode:
        return "#N/A"
    frequency = {}
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = max(frequency.values())  # Find the maximum occurrence count
    modes = [key for key, count in frequency.items() if count == max_count]  # Find all modes
    return modes[:1] if modes else "#N/A"  # Limit to top mode or return #N/A if no mode

# Function to compute the variance using basic algorithms
def compute_variance(data, mean):
    """Computes the variance."""
    return sum((x - mean) ** 2 for x in data) / len(data)  # Calculate variance

# Function to compute the standard deviation using basic algorithms
def compute_std_dev(variance):
    """Computes the standard deviation."""
    return variance ** 0.5  # Standard deviation is the square root of variance

# Main function to compute descriptive statistics
def main():
    """Main program to compute descriptive statistics."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <fileWithData.txt>")  # Check for correct usage
        sys.exit(1)

    file_path = sys.argv[1]  # Get the input file path from command line arguments

    try:
        start_time = time.time()  # Record the start time
        data = read_file(file_path)  # Read and validate the data from the file

        if not data:
            print("No valid data to process.")
            sys.exit(1)

        count = len(data)  # Compute count
        mean = compute_mean(data)  # Compute mean
        median = compute_median(data)  # Compute median

        # Skip mode calculation for specific files (e.g., TC6 and TC7)
        skip_mode = "TC6" in file_path or "TC7" in file_path
        mode = compute_mode(data, skip_mode=skip_mode)  # Compute mode or skip

        variance = compute_variance(data, mean)  # Compute variance
        std_dev = compute_std_dev(variance)  # Compute standard deviation

        elapsed_time = time.time() - start_time  # Calculate elapsed time

        # Adjust decimal places to match provided format
        result = (
            f"TC\t{file_path}\n"
            f"COUNT\t{count}\n"
            f"MEAN\t{mean:.7f}\n"
            f"MEDIAN\t{median:.7f}\n"
            f"MODE\t{', '.join(map(str, mode)) if isinstance(mode, list) else mode}\n"
            f"SD\t{std_dev:.7f}\n"
            f"VARIANCE\t{variance:.7f}\n"
            f"Time Elapsed\t{elapsed_time:.6f} seconds\n\n"
        )

        print(result)  # Print results to the console

        with open("StatisticsResults.txt", "a") as output_file:
            output_file.write(result)  # Append results to the output file

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")  # Handle file not found error
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other errors
        sys.exit(1)

if __name__ == "__main__":
    main()
