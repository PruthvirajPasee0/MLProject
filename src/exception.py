import sys
import logging

def error_message_detail(error,  error_details:sys):
    _,_,tb = sys.exc_info()
    filename = tb.tb_frame.f_code.co_filename
    message="Error in file:[{0}] at line number: [{1}] error message: [{2}]".format(filename, tb.tb_lineno, str(error))
    return message

class  customException(Exception):
    def __init__(self, message, error_details:sys):
        super().__init__(message)
        self.message = error_message_detail(message, error_details=error_details)

    def __str__(self):
        return self.message