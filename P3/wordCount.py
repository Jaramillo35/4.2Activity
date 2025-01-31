import sys
import time

# Function to read words from a file and handle invalid data
def read_file(file_path):
    """Reads words from a file and handles invalid data."""
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            line_words = line.strip().split()  # Split line into words
            words.extend(line_words)
    return words

# Function to compute word frequency using basic algorithms
def compute_word_frequency(words):
    """Computes the frequency of each word using basic algorithms."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Main function to read a file, compute word frequencies, and save results
def main():
    """Main program to compute word frequencies."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")  # Check for correct usage
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        start_time = time.time()  # Record the start time
        words = read_file(file_path)  # Read and validate the data from the file

        if not words:
            print("No valid data to process.")
            sys.exit(1)

        word_frequencies = compute_word_frequency(words)  # Compute word frequencies

        # Prepare results for display and saving
        result_lines = []
        result_lines.append("WORD\tFREQUENCY\n")  # Add header row
        for word, frequency in sorted(word_frequencies.items()):  # Sort alphabetically
            result_lines.append(f"{word}\t{frequency}\n")

        elapsed_time = time.time() - start_time  # Calculate elapsed time

        result_summary = (
            f"File: {file_path}\n"
            f"Total Words: {len(words)}\n"
            f"Distinct Words: {len(word_frequencies)}\n"
            f"Time Elapsed: {elapsed_time:.6f} seconds\n\n"
        )

        # Append results to the output file
        with open("WordCountResults.txt", "a") as output_file:
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
