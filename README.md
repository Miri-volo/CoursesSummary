# Courses Summary
## How to run:
- Clone this repo
-  Add python interpreter (i use python 3.11.4)
    - ```py -m venv venv```
    - ```.\venv\Scripts\activate```
- run ```pip install -r requirements.txt```
- run main.py

#### Currently showing for Software Engineer, 4th year, Bachelor degree
If you wish to change, change the first lines to your choice:
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
    -  3 for general course (קורס כללי)
    -  2 for regular courses
    -  1 for both.

## Explanation
```def fetch_courses():```  
Fetch relevant courses numbers from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=dco  
Returns an array of strings (courses numbers)  

```def fetch_names(courses):``` (not using this function any more, but it can be helpful)  
Make a dictionary from course number and name from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann  

```def fetch_courses_data(courses):```  
Make a beautiful Excel file from relevant courses information from https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann  





![image](https://github.com/Miri-volo/CoursesSummary/assets/75314138/ca5f5778-1ec5-48f8-861d-41efa81d005e)
