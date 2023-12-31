# Made by Miri Volozhinsky
import PyPDF2
import requests
import re
from urllib.request import urlopen
from pyquery import PyQuery as pq
import pandas as pd

year = '2024'  # שנה
semester = '1'  # סמסטר
department = "373"  # מחלקה
year_degree = "4"  # שנה בתואר
degree_level = "1"  # תואר ראשון
gloabl_courses = "3"  # רק כללי


# fetch a list of courses
def fetch_courses():
    url = "https://reports4u.bgu.ac.il/reports/rwservlet?cmdkey=PROD&server=aristo4stu419c&report=acrr008w&desformat=pdf&DESTYPE=cache&P_YEAR={}&P_SEMESTER={}&P_INSTITUTION=0&P_DEGREE_LEVEL={}&P_DEPARTMENT={}&P_GLOBAL_COURSES={}&P_PATH=1&P_SPEC=&P_YEAR_DEGREE={}&P_SORT=1&P_WEB=1&P_SPECIAL_PATH=0&envid=NOENBIDI".format(
        year, semester, degree_level, department, gloabl_courses, year_degree)
    data = requests.get(url)
    with open('courses.pdf', 'wb') as f:
        f.write(data.content)
    pdfFileObj = open('courses.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pages = pdfReader.pages
    courses = []
    for pageObj in pages:
        text = pageObj.extract_text()
        courses = courses + re.findall("[0-9]{3}.[0-9].[0-9]{4}", text)
    pdfFileObj.close()
    print("הקורסים שאתה יכול לקחת הורדו לתקייה שלך לקובץ בשם courses.pdf")
    return courses


# make a dict of {number: course_name}, not in use
def fetch_names(courses):
    degress = set()
    for course in courses:
        degress.add(course.split('.')[1])
    coursesNames = {}
    for degree in degress:
        url = "https://bgu4u.bgu.ac.il/pls/scwp/!app.ann?lang=he&st=a&step=2&oc_course_name=&on_course_ins=0&on_course_ins_list=0&on_course_department=&on_course_department_list=&on_course_degree_level={}&on_course_degree_level_list={}&on_course=&on_credit_points=&on_hours=&on_year={}&on_semester={}&oc_lecturer_last_name=&oc_lecturer_first_name=&oc_start_time=&oc_end_time=&on_campus=".format(
            degree, degree, year, semester)
        page = urlopen(url)
        html_bytes = page.read().decode("iso8859-8")
        htmlText = pq(html_bytes).text().split('\n')[11:]
        index = 0
        while True:
            if index >= len(htmlText):
                break
            coursesNames[htmlText[index]] = htmlText[index + 2]
            index += 3

    return coursesNames


# fetch data for each course
def fetch_courses_data(courses):
    coursesData = {}
    for course in courses:
        info = course.split('.')
        number = info[2]
        department = info[0]
        degree = info[1]
        url = "https://bgu4u.bgu.ac.il/pls/scwp/!app.ann?lang=he&rc_rowid=&lang=he&st=a&step=3&rn_course={}&rn_course_details=&rn_course_department={}&rn_course_degree_level={}&rn_course_ins=0&rn_year={}&rn_semester={}&oc_course_name=&oc_end_time=&oc_lecturer_first_name=&oc_lecturer_last_name=&oc_start_time=&on_campus=&on_common=0&on_course=&on_course_degree_level={}&on_course_degree_level_list={}&on_course_department=&on_course_department_list=&on_course_ins=0&on_course_ins_list=0&on_credit_points=&on_hours=&on_lang=0&on_semester={}&on_year={}" \
            .format(number, department, degree, year, semester, degree, degree, year, semester)
        page = urlopen(url)
        html_bytes = page.read().decode("iso8859-8")
        text = pq(html_bytes).text()
        data = text.split('\n')
        summary = ""
        try:
            if data[18] != '0.0':  # only courses with credits
                for i in range(len(data)):
                    if data[i] == 'תקציר:':
                        if data[i + 1] != 'ביבליוגרפיה:':
                            summary = data[i + 1]
                        break
                location = re.findall("(?:מקוון|היברידי|בכיתה)", text)
                location = set(location) if len(location) > 0 else {}
                courseName = data[13]
                finishInput = False
                while not finishInput:
                    print("קורס: " + courseName + " " + course + ":\nקישור:\n" + url + "\nלחץ על הקישור ומלא את הפרטים")
                    print("אם תטעה, ניתן בסוף לתקן")
                    print("מבחן? (כן/לא/אנטר/כל דבר שתרצה)")
                    exam = input()
                    print("בוחן? (כן/לא/אנטר/כל דבר שתרצה)")
                    midterm = input()
                    print("עבודות? (כן/לא/אנטר/כל דבר שתרצה)")
                    hw = input()
                    print("נוכחות חובה? (כן/לא/אנטר/כל דבר שתרצה)")
                    mandatory = input()
                    print("אם טעית ואתה רוצה לכתוב מחדש את הקורס הזה תכתוב: שגיאה, אחרת תלחץ Enter")
                    finish = input()
                    finishInput = finish != "שגיאה"
                    coursesData[course] = {"שם": courseName, "מספר": course, "נקז": data[18], "תקציר": summary,
                                           'מבחן': exam, 'בוחן': midterm, 'עבודות': hw, 'נוכחות חובה': mandatory,
                                           'מיקום': location,
                                           "קישור": url}
        except Exception as e:
            print("course: " + course + " URL: " + url + "\nerror: " + str(e))
    return coursesData


# make a beautiful exel file
def makeExel(coursesData):
    df = pd.DataFrame(coursesData.values(), index=coursesData.keys())
    df = df[['שם', 'מספר', 'נקז', 'מבחן', 'בוחן', 'עבודות', 'נוכחות חובה', 'מיקום', 'תקציר', 'קישור']]
    excel_filename = 'coursesSummary.xlsx'
    excel_writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False, sheet_name='Courses', startrow=1, header=False)
    worksheet = excel_writer.sheets['Courses']
    num_rows, num_cols = df.shape
    column_settings = [{'header': column} for column in df.columns]
    worksheet.add_table(0, 0, num_rows, num_cols - 1, {'columns': column_settings})
    wrap_format = excel_writer.book.add_format({'text_wrap': True})
    wrap_format.set_align('center')
    wrap_format.set_align('vcenter')
    for i, column in enumerate(df.columns):
        column_len = max(df[column].astype(str).apply(len).max(), len(column))
        worksheet.set_column(i, i, column_len * 2, wrap_format)
    worksheet.set_column('A:A', 30, wrap_format)
    worksheet.set_column('I:I', 100, wrap_format)
    excel_writer.close()
    print("קובץ אקסל נוצר בתקייה שלך בשם coursesSummary.xlsx")


if __name__ == '__main__':
    courses = fetch_courses()
    coursesData = fetch_courses_data(courses)
    makeExel(coursesData)
