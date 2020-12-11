# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

# Lab Test 2
# Author: Janae Fariñas
# Date: 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.characters = []
        self.__cursor = 0
        self.filename = file_name

    @property
    def cursor_prop(self):
        return self.__cursor

    @cursor_prop.setter
    def cursor_prop(self, value):
        if self.__cursor > len(characters) + 1:
            raise Exception("Only one letter at a time")
        else:
            self.__cursor = value

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor_prop, character)
        self.cursor_prop += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        del self.characters[self.cursor_prop]

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        if steps + self.cursor_prop > len(characters):
            raise IndexError("Out of range")
        if steps <= 0:
            raise IndexError("Out of range - must be a whole number")
        else:
            self.cursor_prop += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        if steps > self.cursor_prop:
            raise IndexError("Out of range")
        if steps <= 0:
            raise IndexError("Out of range - must be a whole number")
        else:
            self.cursor_prop -= steps


# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

doc.backward(4)
doc.delete()
doc.insert('n')
doc.save()
