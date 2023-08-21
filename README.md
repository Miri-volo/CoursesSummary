# Courses Summary
Summary of courses (exel file, that you can filter by your choise) you can take next semester, includes:
- course name
- course number
- credits to degree
- if it has exam?
- if it has midterm exam?
- if it has homework?
- is attendance mandatory?
- location (zoom, class or hybrid)
- summary
- link to the course syllabus
## How to run:
- Clone this repo
-  Add python interpreter (i use python 3.11.4)
    - ```py -m venv venv```
    - ```.\venv\Scripts\activate```
- run ```pip install -r requirements.txt```
- run main.py

#### Currently showing for Software Engineer, 4th year for Bachelor degree
If you wish to change, change the first lines of the code to your choice:
```
year = '2024' #שנה
semester = '1' #סמסטר
department = "373" #מחלקה
year_degree = "4" # שנה בתואר
degree_level = "1" #תואר ראשון
gloabl_courses = "3" #רק כללי
```
- **year** - the current year 
- **semester** - the current semseter
    -  1- fist semster/autumn
    -  2- second semester/spring
    -  3- summer semester
- **department** - department number -
    -  373 software engineerig
    -  202 computer science
    -  ... any other department
- **year_degree** - degree year
    -  1- fist year
    -  2- second year
    -  3- third year
- **degree_level** - academic degree
    -  1- bachelor
    -  2- master
    -  3- Doctor 
- **gloabl_courses**- which courses to show
    -  3 for general courses (קורס כללי)
    -  2 for regular courses
    -  1 for both.

## Explanation
Note: I am decoding Hebrew with ``iso8859-8``.

```def fetch_courses():```  
Fetch relevant courses numbers from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=dco usinig regex ```[0-9]{3}.[0-9].[0-9]{4}``` -unfortunately, if there are notes with course number it will consider it as a course that you can take. 

```def fetch_names(courses):``` (not using this function any more, but it can be helpful)  
Make a dictionary from course number and name from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann  

```def fetch_courses_data(courses):```  
Fetch data for relevant courses information from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann.  
Make a dictionary from course number as a key, and all the information as a value.
The information it get from the link: 
- course name
- course number
- credits to degree
- location (zoom, class or hybrid)
- summary
- link to the course syllabus

The information the user must put manually for given link:
- if it has exam?
- if it has midterm exam?
- if it has homework?
- is attendance mandatory?

```def makeExel(coursesData):```
Make a beautiful Excel file from relevant courses information.



## Helpful packages i used:
- <a href="https://pypi.org/project/pyquery/">PyQuery</a>- converts html to text
- <a href="https://xlsxwriter.readthedocs.io/working_with_pandas.html">Pandas and XlsxWriter</a> to make beautiful exel file and table.
- <a href="https://pypi.org/project/PyPDF2/">PyPDF2</a> for reading PDF file.
- <a>
