"""
Kanji Counter Project - Book Object
This module contains the Book class for tracking JLPT level kanji/vocab counts.
"""


class Book:
    """
    Represents a book with associated kanji/vocab counts by JLPT level (N1-N5).
    
    Attributes:
        title (str): The title of the book
        isbn (str): The ISBN code of the book
        n5_value (int): Count of N5 level kanji/vocab
        n4_value (int): Count of N4 level kanji/vocab
        n3_value (int): Count of N3 level kanji/vocab
        n2_value (int): Count of N2 level kanji/vocab
        n1_value (int): Count of N1 level kanji/vocab
    """
    
    def __init__(self, title, isbn):
        """
        Initialize a Book object with title and ISBN.
        All kanji/vocab counts are initialized to 0.
        
        Args:
            title (str): The book title
            isbn (str): The ISBN code
        """
        self.title = title
        self.isbn = isbn
        self.n5_value = 0
        self.n4_value = 0
        self.n3_value = 0
        self.n2_value = 0
        self.n1_value = 0
    
    # ============ GETTER METHODS ============
    # TODO: Implement getter for N5 value
    # Instructions: Create a method called get_n5() that returns self.n5_value
    
    # TODO: Implement getter for N4 value
    # Instructions: Create a method called get_n4() that returns self.n4_value
    
    # TODO: Implement getter for N3 value
    # Instructions: Create a method called get_n3() that returns self.n3_value
    
    # TODO: Implement getter for N2 value
    # Instructions: Create a method called get_n2() that returns self.n2_value
    
    # TODO: Implement getter for N1 value
    # Instructions: Create a method called get_n1() that returns self.n1_value
    
    # ============ SETTER METHODS ============
    # TODO: Implement setter for N5 value
    # Instructions: Create a method called set_n5(value) that sets self.n5_value to the given value
    
    # TODO: Implement setter for N4 value
    # Instructions: Create a method called set_n4(value) that sets self.n4_value to the given value
    
    # TODO: Implement setter for N3 value
    # Instructions: Create a method called set_n3(value) that sets self.n3_value to the given value
    
    # TODO: Implement setter for N2 value
    # Instructions: Create a method called set_n2(value) that sets self.n2_value to the given value
    
    # TODO: Implement setter for N1 value
    # Instructions: Create a method called set_n1(value) that sets self.n1_value to the given value
    
    # ============ UTILITY METHODS ============
    # TODO: Implement total_values() method
    # Instructions: Create a method that returns the sum of all kanji/vocab counts
    # (n5_value + n4_value + n3_value + n2_value + n1_value)
    
    # TODO: Implement print_values() method
    # Instructions: Create a method that prints the book information in a readable format
    # Format suggestion:
    #   Title: [book title]
    #   ISBN: [isbn code]
    #   N5: [count]
    #   N4: [count]
    #   N3: [count]
    #   N2: [count]
    #   N1: [count]
    #   Total: [total count]


def main():
    """
    Main method to run the Kanji Counter program.
    
    TODO: Step 1 - Load the PDF file
    Instructions: Use a PDF parsing library (PyPDF2 or pdfplumber recommended)
    to read the PDF file and extract text content.
    Reference: You'll need to specify the path to the PDF file to scan.
    
    TODO: Step 2 - Parse the extracted text
    Instructions: Extract kanji and vocabulary from the text.
    Consider using a Japanese text analysis library like MeCab or Janome.
    
    TODO: Step 3 - Load the kanji database
    Instructions: Load your provided kanji/vocab database (likely the JSON file in data/)
    Verify what format the database uses (mappings of kanji to JLPT levels).
    
    TODO: Step 4 - Match and count kanji/vocab
    Instructions: Iterate through extracted kanji/vocab and match them against
    the database to determine their JLPT levels (N1-N5).
    Keep a count for each level.
    
    TODO: Step 5 - Create Book object and populate values
    Instructions: Instantiate a Book object with the title and ISBN.
    Use the setter methods to populate each level count from Step 4.
    
    TODO: Step 6 - Display results
    Instructions: Use the print_values() method to display the final counts.
    
    Example flow:
    >>> book = Book("Sample Book", "978-1234567890")
    >>> book.set_n5(50)
    >>> book.set_n4(35)
    >>> book.print_values()
    """
    pass


if __name__ == "__main__":
    main()
