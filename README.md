# CPSC_481_Project_1
Write a Python class, WolfGoatCabbage, that describes the Wolf, goat and cabbage problem (same problem from HW #2) and can then be used to solve it by calling a search algorithm. 
The class must extend class Problem in the search.py code.
Represent the state by a set of characters, representing the objects on the left bank. Use the characters: ‘F’, ‘G’, ‘W’, ‘C’. Note that it is sufficient to represent the objects on one bank since the remaining will be on the other bank. E.g., {‘F’, ‘G’} represents Farmer and Goat on the left bank and Wolf and Cabbage on the right.
An action in this puzzle is 1-2 objects crossing in the boat. Represent an action as a set of characters representing the objects crossing. E.g., {‘F’, ‘G’} represents the farmer and goat crossing. Note that it is not necessary to represent the direction of the boat as this will be clear from the state (e.g., if the farmer is on the left, then the boat will have to cross to the right).
The class should be usable in the main function below to print the sequence of actions to reach the goal state.
