import os
import time

def convert_units(input_str):
    # Extracting the units and amount from the input string
    start_unit = int(input_str[0])
    convert_to_unit = int(input_str[1])
    amount = float(input_str[2:])

    # Conversion factors
    grams_to_oz = 0.03527396
    grams_to_lbs = 0.00220462
    oz_to_grams = 28.3495
    oz_to_lbs = 0.0625
    lbs_to_grams = 453.592
    lbs_to_oz = 16

    # Performing the conversion
    if start_unit == 1 and convert_to_unit == 2:
        result = amount * grams_to_oz
        result_unit = "oz"
    elif start_unit == 1 and convert_to_unit == 3:
        result = amount * grams_to_lbs
        result_unit = "lbs"
    elif start_unit == 2 and convert_to_unit == 1:
        result = amount * oz_to_grams
        result_unit = "g"
    elif start_unit == 2 and convert_to_unit == 3:
        result = amount * oz_to_lbs
        result_unit = "lbs"
    elif start_unit == 3 and convert_to_unit == 1:
        result = amount * lbs_to_grams
        result_unit = "g"
    elif start_unit == 3 and convert_to_unit == 2:
        result = amount * lbs_to_oz
        result_unit = "oz"
    else:
        # Invalid conversion
        return "Invalid conversion units"

    # Formatting the result string
    result_str = f"{result:.2f} {result_unit}"
    return result_str

print("STARTING UNIT CONVERTER SERVICE...")

# Change these to the filepaths for the text file that is taken as an input, and the text file used to receive the output
INPUT_FILEPATH = 'inputService.txt'
OUTPUT_FILEPATH = 'outputService.txt'

units = ['g', 'oz', 'lb']

# Example usage:
#input_string = "1240"
#result = convert_units(input_string)
#print(f"Conversion Result: {result}")


while True:
    f = open(INPUT_FILEPATH, 'r', encoding="utf-8") # Change the inputService.txt to a text file that you want to read to start the unit conversion
    data = f.read()
    
    # Attempt to convert the files when there is anything in the .txt file
    if data:
        converted_unit = convert_units(data)
        if converted_unit != "Invalid conversion units":
            f.close()
            f = open(INPUT_FILEPATH, 'w', encoding="utf-8").close() # Erase file contents
        
        f = open(OUTPUT_FILEPATH, 'w', encoding="utf-8")
        f.write(converted_unit)
        f.close()

        



