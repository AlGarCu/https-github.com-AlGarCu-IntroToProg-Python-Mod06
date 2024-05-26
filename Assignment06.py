# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Change Log: (Who, When, What)
#   Alejandro Garcia, 5/25/2024, Created Script for A06
# ------------------------------------------------------------------------------------------ #

# Importing json package

import json

## Classes and Functions section

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    AGarcia,5.25.2024, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    AGarcia,5.25.2024, Created Class
    AGarcia,5.25.2024, Added menu output and input functions
    AGarcia,5.25.2024, Added a function to display the data
    AGarcia,5.25.2024, Added a function to display custom error messages
    Agarcia,5.25.2024, Added a function to display full list of student data at the moment of choice 2
    """

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        AGarcia,5.25.2024,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.


    @staticmethod
    def output_student_courses(students:list):
        """ This function displays the full list of students upon selection of choice 2

        ChangeLog: (Who, When, What)
        AGarcia,5.25.2024,Created function

        :return: None
        """
        print("The full list of student data collected follows:")
        #print(students)
        for entries in students:
            print(f"{entries['FirstName']} {entries['LastName']} {entries['CourseName']}")


    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        AGarcia,5.25.2024,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        AGarcia,5.25.2024,Created function

        :return: string with the users choice
        """
        global menu_choice #Giving the function access to modifying the global menu choice

        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return menu_choice

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        global file
        global students

        try:
            file = open(file_name, "w")
            json.dump(students, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course from the user

        ChangeLog: (Who, When, What)
        AGarcia,5.25.2024,Created function

        output impacts directly on students list

        """
        global student

        try:
            # Input the data
            student_first_name = input("Enter the student's name ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's name ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Enter the course's name ")
            if not student_first_name.isalpha():
                raise ValueError("The course name should not contain numbers.")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            students.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

# Defining the Data Constants and including Type hints

MENU: str = '''\
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Defining the Data Variables and including Type hints
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
json_data: str = ''
file = None # Type hint omitted here as potential bug pointed in Module 04 Notes
menu_choice: str = ''
student_data: dict = {} # This dictionary student data dictionary rows for each individual
students: list = [] #  One row per Student
newdata: list = [] # To hold the data only created through the last program run
# Reading the existing contents from the .json file into a list of dictionaries and displaying its contents, now via a function
students = FileProcessor.read_data_from_file(FILE_NAME, student_data=students)
for student in students:
    print(list(student.values())[0],list(student.values())[1],list(student.values())[2])
# Present the menu of choices and Process the data
while True: # Initializing the while loop and calling the menu choice function
    IO.output_menu(menu=MENU)
    IO.input_menu_choice()
    # Menu 1 -- Input user data
    if menu_choice == '1':
        IO.input_student_data(students)# Initializing the if/elif conditional statements
    elif menu_choice == '2':
    # Menu 2 -- Present the current data
        print("The full list of student data collected follows:")
        IO.output_student_courses(students)
    # Menu 3 -- Save the data to a file and display what was added to the initial file
    elif menu_choice == '3':
        IO.write_data_to_file(file_name = FILE_NAME, student_data = student_data)
    # Menu 4 -- Stop the loop
    elif menu_choice == '4': #Granting the option to exit the while loop via choice 4
        break
    else:
        print("Please select a valid option")
        print(menu_choice)
        continue #Reverting back to the start of the while loop for any invalid choice and giving error message






