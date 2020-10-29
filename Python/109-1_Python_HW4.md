# Python HW4

### 24

### 26
Suppose the count function for a string didn't exist. Define a function that returns the number of non-overlapping occurences of a substring in a string.

### 28
The factorial of a positive integer n (written n!) is the prodect \(1 \cdot 2 \cdot 3 \cdot ... \cdot n\). Write a program tha asks the user to input a positive integer and then calculates and displays the factorial of the number. The program should call a function named getN that gets the input and guarantees that the input is a positive integer. Also, the factorial of the number input should be calculated with a function named fact. See Fig. 4.5.


### 30
Write a pay-raise program that requests a person's first name, last name, and current annual salary, and then displays the person's salary for next year. People earning less than $40,000 will recieve a 5% raise, and those earning $40,000 or more will receive a raise of $2,000 plus 2% of the amount over $40,000. Use functions for input and output, and a function to calculate the new salary. See Fig. 4.7.


### 32
The file Months.txt has 12 lines with each line containing one of the months of the year. Write a program that displays the months containing the letter r. The program should use a global variable months that is initialized as the empty list. The function main should call three functions, one to fill the list months with the contents of the text file, one to delete from the list months the months that do not contain the letter r, and one to display the names of the months remaining in the list. See Fig.4.8.

### 34
A person in the Civil Service Retirement System can retire at age 55 with at least 20 years of service. A simplified variation for the computation of the amount of their pension is as follows:
1. Calcusate the average annual salary for the person's best three years; call it ave.
2. Calculate \(\frac{numberOfMonths}{12}\) and call it yrs.
3. Calculate percentage rate: 1.5% for first five years, 1.75% for next five years, 2% for each additional year. Call it perRate.
4. Take the minimum of perRate and 80%; call it p.
5. The amountt of the ponsion is p*ave.

Write a program that requests the input as shown in Fig. 4.10, and calculates the amount of the pension. The values of ave and p should be computed in functions.
