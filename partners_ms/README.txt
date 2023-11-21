1. How to request data. To request data you should type 'run' to the file that the microservice will read from. 
For example I have it writting to phrase.txt. 
An example program function would be:
    with open('phrase.txt', 'w') as file:
        file.write('run')

2. How to recieve data. To recieve dat it would essentially be the same thing. However instead you will read from a text file. 
An example program call would be: 
    with open('phrase.txt', 'r') as phrase_file:
        phrase = phrase_file.read()

3. 