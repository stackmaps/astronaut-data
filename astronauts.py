import csv

with open('astronauts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    navy_astronauts = []
    
    for row in readCSV:
        
        #Use if statements to print the name of the astronaut whose undergraduate major was aeronautical engineering, graduate major was aerospace engineering, and has spent 205 hours in space flight.
            #The if statement will contain 3 conditions



        #Use an if statement to print the name of the astronaut whose total hours spent in space flight and space walks  is 297 hours.
            #In the dataset, all values are stored as strings, but in order to find the total hours spent in space flight and space walks, they need to be converted to numbers using: float()



        #Create a function that creates a one-sentence summary of each astronaut.
            #You can include whatever information you want but it must include the astronaut's name and missions.


        #How many astronauts from the dataset served in the US Navy? Append their names in the list called navy_astronauts and then print the list.
            #First create an empty list in which you will use append the names of the astronauts. Create this list outside of the for loop.
        

