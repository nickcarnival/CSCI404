1. Names and CSM Campus IDs of the students of the project team: 
Nicholas Carnival 10798955, David Stonecipher 10863871

2. What programming language is used:
Python3

3. What OS is used to compile and run the codes: 
Windows or Linux, no compiling required. 
As long as the computer has the main Python libraries installed (queue, main, math, sys) it should work with just the command line arguments.

4. How the code is structured:
The script files is in the src directory.

The code all runs from the main method. Main handles the command line arguments and calling all of the other functions.
The first thing that main does is call parse_input which adds all of the cities and their weights to a python dictionary.
The return from parse_input is then passed into the find_route method along with the source and destination city.
This uses a uniform cost search algorithm to find the best route if a route exists. If a route does not exist, it just returns NoneType.
After the best route has been found, print_results is called which handles output formatting. It will either print the route that
was taken or it will print an infinite route, as requested.

5. How to run the code:
You run this code exactly how it is specified in the project requirements.

Note: This program will only work with python3 because python2 does not have the queue library installed, 
and we tried to have no dependencies that weren't standard

General Format: 'python3 find_route.py input_filename origin_city destination_city' 

Example: 'python3 src/find_route.py inputs/input.txt Bremen Frankfurt'

All of these arguments are relative directories.