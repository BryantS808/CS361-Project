import time

# Function to write "run" to phrase.txt
def write_run_to_file():
    with open('phrase.txt', 'w') as file:
        file.write('run')

# Function to read and print the phrase from phrase.txt
def read_and_print_phrase():
    while(True):
        with open('phrase.txt', 'r') as file:
            content = file.read()
            if content == 'run':
                print("Running the other script...")
                time.sleep(2)  # Simulating some processing time
            else:
                with open('phrase.txt', 'r') as phrase_file:
                    phrase = phrase_file.read()
                    print("Received phrase:", phrase)
                    # Clear the file after reading
                    time.sleep(2)
                    with open('phrase.txt', 'w') as clear_file:
                        clear_file.write('')
                exit()

# Write "run" to the file
write_run_to_file()

# Simulate running the other script
# In a real scenario, this would be where you run your other script
time.sleep(2)  # Simulating some processing time

# Read and print the phrase from the file and clear it
read_and_print_phrase()