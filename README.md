# Courses Summary

Create a pretty Excel summary of courses you may take next semester at Ben Gurion
University. Including:

- Course name
- Course number
- Course credits (only courses with 1 or more credits are shown)
- Has a final exam?
- Has a midterm exam?
- Has homework?
- Has mandatory attendance?
- Location (in-person, hybrid or online).
- Summary
- Syllabus link

https://github.com/Miri-volo/CoursesSummary/assets/75314138/c5c6104c-2ab6-4a87-85dc-4dad2f27fa0c

## Quick-Start Guide

It is recommended to use Python 3.11.4.

1. Clone this repository
2. Create a virtual environment: `py -m venv venv`
3. Activate the virtual environment: `./venv/Scripts/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Run the program: `python main.py`

You will then be prompted with a link to the course to manually fill information
that can not be inferred.

```
קורס: מי כתב את התנ"ך? מבוא לספרות המקרא 121.1.1551:
קישור:
https://bgu4u.bgu.ac.il/pls/scwp/!app.ann?lang=he&rc_rowid=&lang=he&st=a&step=3&rn_course=1551&rn_course_details=&rn_course_department=121&rn_course_degree_level=1&rn_course_ins=0&rn_year=2024&rn_semester=1&oc_course_name=&oc_end_time=&oc_lecturer_first_name=&oc_lecturer_last_name=&oc_start_time=&on_campus=&on_common=0&on_course=&on_course_degree_level=1&on_course_degree_level_list=1&on_course_department=&on_course_department_list=&on_course_ins=0&on_course_ins_list=0&on_credit_points=&on_hours=&on_lang=0&on_semester=2024&on_year=1
לחץ על הקישור ומלא את הפרטים
מבחן? (כן/לא/אנטר/כל דבר שתרצה)
כן
בוחן? (כן/לא/אנטר/כל דבר שתרצה)
לא
עבודות? (כן/לא/אנטר/כל דבר שתרצה)
לא
נוכחות חובה? (כן/לא/אנטר/כל דבר שתרצה)
כן
אם טעית ואתה רוצה לכתוב מחדש את הקורס הזה תכתוב: שגיאה, אחרת תלחץ Enter
```

By default it is configured for the 4th year of a Software Engineering Bachelor's
degree. If you wish to change it, modify the variables defined at the top of the
script to your preference:

```
year = '2024' #שנה
semester = '1' #סמסטר
department = "373" #מחלקה
year_degree = "4" # שנה בתואר
degree_level = "1" #תואר ראשון
gloabl_courses = "3" #רק כללי
```

- **year** - Current year
- **semester** - Current semester:
    - 1 - fist/autumn semester
    - 2 - second/spring semester
    - 3 - summer semester
- **department** - Department number:
    - 373 Software Engineering
    - 202 Computer Science
    - Any other department...
- **year_degree** - Degree year:
    - 1 - Fist year
    - 2 - Second year
    - 3 - Third year
- **degree_level** - Academic degree level:
    - 1 - Bachelor's degree
    - 2 - Master's degree
    - 3 - Doctoral degree
- **gloabl_courses** - Course types to show:
    - 3 - General courses (קורס כללי)
    - 2 - Regular courses
    - 1 - Both

## Explanations

**Note:** I am decoding Hebrew with ``iso8859-8``.

### `def fetch_courses()`

Fetch relevant course numbers from `https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=dco`
using the regex `[0-9]{3}.[0-9].[0-9]{4}`. Unfortunately, if there are notes with
course number it will consider it as a course you may take. 

### `def fetch_names(courses)`

(not using this function any more, but it may be helpful)  
Make a dictionary from course number and name from
`https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann`.

### `def fetch_courses_data(courses)`

Fetch data of relevant courses from `https://bgu4u.bgu.ac.il/pls/scwp/!app.gate?app=ann`.
Make a dictionary from course number as a key, and course information as a value.
The information includes: 

- Course name
- Course number
- Degree credits
- Location (in-person, hybrid or online)
- Summary
- Syllabus link

The information the user must input manually for a course:

- If it has a final exam?
- If it has a midterm exam?
- If it has homework?
- Is attendance mandatory?

### `def makeExel(coursesData)`

Make a beautiful Excel file from relevant courses information.

## Helpful Packages Used

- [PyQuery](https://pypi.org/project/pyquery/) for HTML parsing and querying
- [Pandas with XlsxWriter](https://xlsxwriter.readthedocs.io/working_with_pandas.html) for making beautiful Excel files
- [PyPDF2](https://pypi.org/project/PyPDF2/) for parsing PDF files
