# timestamp_parser

DESCRIPTION
- This program (aka parser) is based on the output of another program (aka timestamp, not included here). The timestamp program went through a database and collected all of the data regarding the names of the files and the last time each of them were opened, outputting the results into a single column of an excel file. This output was impossible to sort as each file (along with the time and date of its last access in a single cell) was listed with the other files in the same folder beneath the filepath of said folder. This parser program took that excel file and broke it up so each file was associated with a row (instead of a single cell) that contained the name/filepath of the file, the filepath of the folder that the file was in, the date that the file was last accessed and the time of day the file was last accessed. This greatly improved readability and allowed the files to be sorted by the last time they were opened so that all files not opened within the last six months could be marked.

USAGE
- This program is run through the command line with the line "python timestamp_parser_v1_0.py &lt;filename&gt;" but has a reminder of proper usage if this line is not input properly.
- The filename portion is to be filled with the name of the excel file that the user would like to be parsed.

PROGRAM STEPS
- Collect the information from the command line call
- Use pd.read_excel() to read the contents of the file input in the command line
- Use pandas' copy() method to create a copy of the excel file's data
- Create a temporary column (temp) thats a copy of the original messy column to be sliced apart
- Create empty columns for each of the file attributes (file's filepath, folder's filepath, date of last access, time of last access)
- Iterate through the temp column ###TO BE CONTINUED



I created this program to take the output of another program that went through a database and pulled the last time every file was accessed and split it into sections to increase the readability. 

Note: The filepath for each folder was listed on its own and then the contents of the folder were listed below. I took this and copied it into another column, matching with the files, which greatly increased readability and allowed the files to be sorted by the date they were last opened.
