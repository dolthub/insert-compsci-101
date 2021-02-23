import mysql.connector
from datetime import date 
connection = mysql.connector.connect(user='root',
                                     host="127.0.0.1",
                                     port=3307,
                                     database='national_course_catalog_us')
cursor = connection.cursor(buffered=True)
cursor.execute('SET @@autocommit = 1')

catalog_url = "https://dukehub.duke.edu/psp/CSPRD01/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?&cmd=uninav&Rnode=LOCAL_NODE&uninavpath=Root{PORTAL_ROOT_OBJECT}.HighPoint{HIGHPOINT}.Campus%20Experience{HPT_CAMPUS_EXPERIENCE}.Class%20Information{HPT_CX_CLASS_INFORMATION}"
course = "Introduction to Computer Science"
course_id = "COMPSCI 101L"
section = "001-LEC (6673)"
start_date = date(2021, 1, 20).strftime('%Y-%m-%d')
end_date = date(2021, 4, 23).strftime('%Y-%m-%d')
occupancy = 84
capacity = 240
meets = "TuTh 1:45pm - 3:00pm"
college = "DUKE UNIVERSITY"
subject = "COMPUTER SCIENCE"
career = "UNDERGRADUATE"
class_attributes = "(QS) Quantitative Studies" 
description = "Introduction practices and principles of computer science and programming and their impact on and potential to change the world. Algorithmic, problem-solving, and programming techniques in domains such as art, data visualization, mathematics, natural and social sciences. Programming using high-level languages and design techniques emphasizing abstraction, encapsulation, and problem decomposition. Design, implementation, testing, and analysis of algorithms and programs. No previous programming experience required. Not open to students who have taken Computer Science 102, 116, Engineering 103 or Computer Science 201."
instructors = "Astrachan, Fain, Rodger, Stephens-Martinez or Washington"
units = "1"
instruction_mode = "ONLINE"
location = "Online Course"
grading_basis = "GRADED"
term = "2021 Spring Term"
textbooks = "Textbooks to be determined"
components = "Laboratory Required, Lecture Required"
instructors2 = "Alicia Nicki Washington, Susan H Rodger"

query = """
               UPDATE colleges SET catalog_url=%s WHERE college=%s
        """
cursor.execute(query, (catalog_url, college))
query = """
               INSERT INTO subjects (subject, college) VALUES (%s, %s)
        """
cursor.execute(query, (subject, college))
query = """
               INSERT INTO courses (course, course_id, college, subject, class_attributes, units, grading_basis, term, instructors, textbooks, components, instruction_mode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
cursor.execute(query, (course, course_id, college, subject, class_attributes, units, grading_basis, term, instructors, textbooks, components, instruction_mode))
query = """
               INSERT INTO sections (section, course_id, college, occupancy, capacity, start_date, end_date, meets, location, instructors) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
cursor.execute(query, (section, course_id, college, occupancy, capacity, start_date, end_date, meets, location, instructors2))
