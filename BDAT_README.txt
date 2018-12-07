Big Data Analytics Tool (BDAT.py)

Specifications Update: Spring 2018

Author: Alex Knoepfler
Advisor: Dr. Ning Yu
In Collaboration with James Finn & Samuel Cherwonik

System Requirements:

Windows 7 or Higher

Python 3.X or Higher

TensorFlow

AMD A9 2.5GHz / Intel I3 2.5GHz  Or Higher performance CPU

4GB RAM or Higher

At least 4GB of hard drive space including
data files.

A GPU is NOT required.  Note that TensorFlow only supports
INTEL GPUs.

Tested On:

Windows 10
Python 3.6
AMD FX-6350 3.5 GHZ Six-Core
16 GB RAM
2 TB Hard Drive
GPU Specs are absent as the test GPU was AMD/ATI based.

FUNCTIONS:

extractCol(filepath, n)
	
	@param filepath - contains the system's file path to the datafile
	@param n - is the column number to be extracted.
	
This function extracts a column (selected by the user) and
writes it to a txt file.

booleanToCol(out)

	@param out - contains the list of regular expressions
	
This function takes a list of regular expressions as a paramater
then parses the regular expressions as a numeric value.

The value assignment is such for three regular expressions
		-1 , 0 , 1
		
uniqueClasses(filepath, n)*(See Inteded Improvements)
	
	@param Filepath - contains the filepath to the datafile
	@param n - is the column number to be extracted.
	
This function extracts unique occurrences in a given column (n)
and prints the resulting list to the command line.

numeric(unique) ***This must be used on numeric data only***
	
	@param unique - a list of unique occurrences of column values
	
For numeric data types only, using the list of unique column values this function
sorts the list in ascending order.

stats(out, unique)

	@param out - contains the list of regular expressions.
	@param unique - a list of unique occurrences of column values.
	
Taking the lists of unique occurrences and all values, this function calculates
ratios for each unique occurrence using a Bayesian algorithm.

main()

Contains variable declarations for:

	filepath - contains the system's file path to the data file
	
	A for-loop contains using range**(See comments) of columns to be extracted, calculates
	statistics or find unique occurrences.
	
	At the user's discretion the range for the for-loop can be altered to
	to calculate statistics and create lists for all columns contained 
	in the data set.
	
	
	 
Intended Improvements:
	
	*Per scholarly recommendation the brute-force like nature of uniqueClasses() 
	will be replaced by a Boyer-Moore-Horspool Algorithm for pattern recognition.
	
	The theoretical speed up will be from O(m * n) to O(m + n) : Where m is the
	number of columns in the dataset and n is the number of rows.

Comments:
	
	**A command line based user-input for a range values can be implemented
	 at a users request.  Due to the large volume of statistics calculated on
	 the datasets the BDAT.py was implemented as an immutable software.