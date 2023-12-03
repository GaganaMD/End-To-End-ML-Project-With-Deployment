# For custom exception handeling in python

import sys

def error_message_detail(error,error_detail:sys):
    # Extracting detailed information about the error

    _,_,exc_tb=error_detail.exc_info()
    # Ignoring the first 2 levels of the error traceback

    file_name=exc_tb.tb_frame.f_code.co_filename

    # Constructing a detailed error message
    error_message="Error occured in the python script [{0}] at line: [{1}]  error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
    
    

class CustomException(Exception):
        def __init__(self,error_message,error_detail:sys):
            # Calling the constructor of the parent class (Exception)

            super.__init__(error_message)
            # Inheriting the error message from the parent class

            # Creating a detailed error message using the helper function
            self.error_message=error_message_detail(error_message,error_detail=error_detail)
            
        def __str__(self):
            # Overriding the __str__ method to return the detailed error message
            return self.error_message

             