#all global variables to be put here

aboutMessage = """
A program to extract survey responses data from Excel spreadsheets.

It parses and cleans the spreadsheet data, then analyzes the responses' patterns. In the end, it generates visualizations such as charts and tables

Any questions about this program?
Don't ask this question. Stop asking us questions. Please look at our Github https://www.github.com/.
"""
instructions = """
How to use the survey excel grapher?

Remove any rows above the table header. The table header must be on row 1.
Add a row below the header, and indicate on every corresponding question column the question type.
Write in full terms e.g. "multiple choice", "open ended" without hypens or semicolons.
SAVE THE EXCEL FILE AS A NEW FILE SO THAT YOUR ORIGINAL FILE IS INTACT!!!

Open the NEW EXCEL FILE.

There can be rows between the header and your first data row, for footnotes or annotations.
Indicate the first data row that you want the program to process.

There can be columns on the left before your first data column, for ID or S/N, etc. 
Indicate the first data column that you want the program to process.

Finally, select what graph output you desire. Then click "analyze data" and view your graphs on your web browser :D

If you want to see this screen again, click "how to use" :)

For easter egg, click "about program" ;)
"""
excel_file_path = ""
df = None
mcqQuestions = []
openEndedQuestions = []