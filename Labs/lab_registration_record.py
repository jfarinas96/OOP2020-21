# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    """
    Class to represent student data.
    ...
    Attributes:
    -----------
        Class variables: UNDERGRADUATE, PORSTGRADUATE

        study_type : int
            Variable that holds the student's study type,
            undergraduate or postgraduate.

        __f_name : str
            Variable that holds the first name of student.

        __l_name : str
            Variable that holds the last name of student.

        courses : list
            Variable that holds the courses of each student.

    Methods:
    --------
        first_name:
            Property getter method that returns the first name
            of the student.

        last_name:
            Property getter method that returns the
            last name of the student
            Property setter method that sets the last
            name of the student.

        return_student_info
            Method that returns:
                study_type
                first_name
                last_name
    """
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, study_type, f_name, l_name):
        """
        Constructs the necessary attributes for the
        Student object.

        Parameters:
        -----------
            study_type : int
                0 = Undergraduate and 1 = Postgraduate.

            f_name : str
                First name of student.

            l_name
                Last name of student.

        Instance variables:
        -------------------
            study_type : int
                Variable that holds the student's study type,
                undergraduate or postgraduate.

            __f_name : str
                Variable that holds the first name of student.

            __l_name : str
                Variable that holds the last name of student.

            courses : list
                List that holds the courses of each student.
        """
        self.study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.courses = []

    @property
    def first_name(self):
        """
        Property method to return the first name of the student.

        Parameters: None.
        -----------

        Returns:
        --------
            __f_name : str
                First name of the student.
        """
        return self.__f_name

    @property
    def last_name(self):
        """
        Property method to return the last name of the student.

        Parameters: None.
        -----------

        Returns:
        --------
            __l_name : str
                Last name of the student.
        """
        return self.__l_name

    @last_name.setter
    def last_name(self, value):
        """
        Property method to set the last name of the student.
        Checks that value being set is a string.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        if type(value) == str:
            self.__l_name = value
        else:
            raise Exception("Error, cannot set this name.")

    def return_student_info(self):
        """
        Returns all student information.

        Parameters: None.
        -----------

        Returns:
        --------
            study_type :  int
                Student's study type, 0 = undergraduate
                and 1 = postgraduate.
            __f_name : str
                First name of student.
            __l_name : str
                Last name of student.
        """
        return self.study_type, self.first_name, self.last_name


class RegistrationData:
    """
    Class to represent student registration data.
    ...
    Attributes:
    -----------
        __address : str
            Variable that holds the student's address.

        __registration fee : int
            Variable that holds the student's fees.

        student_object : object from Student class
            Contains variables:
                study_type
                f_name
                l_name

        __s_id : str
            Variable that holds the student's id.

    Methods:
    --------
        address:
            Property getter and setter method for the
            student's address.

        reg_fee:
            Property getter method that returns the student's
            registration fee.

        student_id_property:
            Property getter and setter method for the
            student's id.

        display_student_data:
            Method to display student data, such as:
                Student info: student_object(study_type, f_name, l_name), __s_id, student_object.courses
                Address: __address
                Registration fee: __registration_fee
    """

    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        """
        Constructs the necessary attributes for the
        Student object.

        Parameters:
        -----------
            address : str
            registration_fee : int
            study_type : int
            f_name : str
            l_name : str
            s_id : str

        Instance variables:
        -------------------
            __address : str
                Student address

            __registration_fee : str
                Student registration fee

            student_object : object from Student Class
                Contains variables:
                    study_type, f_name, l_name

            __s_id :  str
                Student id
        """
        self.__address = address
        self.__registration_fee = registration_fee
        self.student_object = Student(study_type, f_name, l_name)
        self.__s_id = s_id

    @property
    def address(self):
        """
        Property method to return the address of the student.

        Parameters: None.
        -----------

        Returns:
        --------
            __address : str
                Student address
        """
        return self.__address

    @address.setter
    def address(self, value):
        """
        Property method to set the address of the student.
        Checks that value being set is a string.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        if type(value) == str:
            self.__address = value
        else:
            raise Exception("Error, cannot set this address")

    @property
    def reg_fee(self):
        """
        Property method to return student's registration fee.

        Parameters: None.
        -----------

        Returns:
        --------
            __registration_fee : int
                Student registration fee
        """
        return self.__registration_fee

    @property
    def student_id_property(self):
        """
        Property method to return student id.

        Parameters: None.
        -----------

        Returns:
        --------
            __s_id : str
                Student id
        """
        return self.__s_id

    @student_id_property.setter
    def student_id_property(self, value):
        """
        Property method to set the student id.
        Checks that value being set is a string.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        if type(value) == str:
            self.__s_id = value
        else:
            raise Exception("Error, cannot set this id")

    def display_student_data(self):
        """
        Displays student data, such as:
            Student info: student_object(study_type, f_name, l_name),
            __s_id, student_object.courses
            Address: __address
            Registration fee: __registration_fee

        Parameters: None.
        -----------

        Returns: None.
        """
        print("Student Info: {0[0]}, {0[1]} {0[2]}, {1}, {2}".format(self.student_object.return_student_info(),
                                                                     self.student_id_property, self.student_object.courses))
        print("Address: " + self.address)
        print("Registration Fee: {0}".format(self.reg_fee))
        print("")


r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property = "C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses.append(course)
r.display_student_data()

# print(RegistrationData.__doc__)
