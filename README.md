# CS361-Project
# Here is the test commit to my cs361 repo Username:BryantS808


Communication Contract 
1. How to request data. To request data you should type 'run' to the file that the microservice will read from. 
For example I have it writting to phrase.txt. 
An example program function would be:
    with open('phrase.txt', 'w') as file:
        file.write('run')

2. How to recieve data. To recieve dat it would essentially be the same thing. However instead you will read from a text file. 
An example program call would be: 
    with open('phrase.txt', 'r') as phrase_file:
        phrase = phrase_file.read()

3. UML
    ![CS361 HW8](https://github.com/BryantS808/CS361-Project/assets/109177265/3a9faf07-770b-40f7-be66-4d3a1c77c1bb)

