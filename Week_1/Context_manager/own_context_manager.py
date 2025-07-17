class File(object):
    def __init__(self, filename, mode):
        self.file_obj = open(filename, mode)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('own_context_manager_class.txt', 'w') as f:
    f.write("Rewrite file after execute")


"""
1. It passes the type, value and traceback of the error to the __e  xit__ method.
2. It allows the __exit__ method to handle the exception.
3. If __exit__ returns True then the exception was gracefully handled.
4. If anything other than True is returned by the __exit__ method then the exception is raised by the with statement.
"""
