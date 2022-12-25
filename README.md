# Timestamp Parser

DESCRIPTION
- This program (aka parser) is based on the output of another program (aka timestamp, not included here). The timestamp program went through a database and collected all of the data regarding the names of the files and the last time each of them were opened, outputting the results into a single column of an excel file. This output was impossible to sort as each file (along with the time and date of its last access in a single cell) was listed with the other files in the same folder beneath the filepath of said folder. This parser program took that excel file and broke it up so each file was associated with a row (instead of a single cell) that contained the name/filepath of the file, the filepath of the folder that the file was in, the date that the file was last accessed and the time of day the file was last accessed. This greatly improved readability and allowed the files to be sorted by the last time they were opened so that all files not opened within the last six months could be marked.

USAGE
- This program is run through the command line with the line "python timestamp_parser_v1_0.py &lt;filename&gt;" but has a reminder of proper usage if this line is not input properly.
- The filename portion is to be filled with the name of the excel file that the user would like to be parsed.

PROGRAM STEPS

(Indented steps involve iterating through the temp column)
- Collect the information from the command line call
- Use pd.read_excel() to read the contents of the file input in the command line
- Use pandas' copy() method to create a copy of the excel file's data
- Create a temporary column (temp) thats a copy of the original messy column to be sliced apart
- Create empty columns for each of the file attributes (file's filepath, folder's filepath, date of last access, time of last access)
  - Pull the filepath of each folder and place it in the folder filepath column of each file cell
  - Put NaN in all of the cells that didn't contain individual files (Clear all the filepath/extra cells)
  - Clean up cells so next parsing steps are easier
  - Pull the last date accessed from the file cells and place it in the last date accessed column of those rows, then delete that infromation from the file cells
- Remove the spacing in the last date accessed column using pandas' replace() method
  - Pull the last time accessed from the file cells and place it in the last time accessed column of those rows, then delete that information from the file cells
- Clean up the spacing in the last time accessed column using pandas' replace() method
  - Pull the filename from the file cells, combine it with the filepath column information from the same row, and populate the file filepath column in the same row with the new string
- Make sure everything is separated by a single space in the file filepath column using pandas' replace() method
- Remove the first character of each cell in the file filepath column to remedy a spacing issue
- Iterate through the file filepath column, cleaning away any cells in the folder filepath column that correspond to empty cells in the file filepath column
- Make sure everything is separated by a single space in the folder filepath column using pandas' replace() method
- Remove the first character of each cell in the folder filepath column to remedy a spacing issue
- Remove the temp column using pandas' drop() method
- Write the edited data into a new excel file using pd.ExcelWriter()
- Save that file
- Print "Finished"
