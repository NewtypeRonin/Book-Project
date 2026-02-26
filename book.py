"""
Kanji Counter Project - Book Object
This module contains the Book class for tracking JLPT level kanji/vocab counts.
"""
from PYPDF2 import PdfReader  # For PDF parsing
import json  # For loading the kanji database


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
    def get_n5(self):
        return self.n5_value
    
    def get_n4(self):
        return self.n4_value

    def get_n3(self):
        return self.n3_value
    
    def get_n2(self):
        return self.n2_value
    
    def get_n1(self):
        return self.n1_value
    
    # ============ SETTER METHODS ============
    def set_n5(self, value):
        self.n5_value = value
    
    def set_n4(self, value):
        self.n4_value = value
    
    def set_n3(self, value):
        self.n3_value = value
    
    def set_n2(self, value):
        self.n2_value = value
    
    def set_n1(self, value):
        self.n1_value = value
    
    # ============ UTILITY METHODS ============
    # TODO: Implement total_values() method
    # Instructions: Create a method that returns the sum of all kanji/vocab counts
    # (n5_value + n4_value + n3_value + n2_value + n1_value)
    def total_values(self):
        return self.n5_value + self.n4_value + self.n3_value + self.n2_value + self.n1_value
    
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
    def print_values(self):
        print(f"Title: {self.title}")
        print(f"ISBN: {self.isbn}")
        print(f"N5: {self.n5_value}")
        print(f"N4: {self.n4_value}")
        print(f"N3: {self.n3_value}")
        print(f"N2: {self.n2_value}")
        print(f"N1: {self.n1_value}")
        print(f"Total: {self.total_values()}")


def main():
    """
    Main method to run the Kanji Counter program.
    
    TODO: Step 1 - Load the PDF file
    Instructions: Use a PDF parsing library (PyPDF2 or pdfplumber recommended)
    to read the PDF file and extract text content.
    Reference: You'll need to specify the path to the PDF file to scan.
    reader = PdfReader("path_to_your_book.pdf")
    #number of pages = len(reader.pages)
    #for page in reader.pages:
    #    text = page.extract_text()
    #    # Process the text to extract kanji/vocab
    
    
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
