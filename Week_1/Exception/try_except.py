import logging


def safe_divide():
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print("Running")
        print(number1 / number2)
    except ValueError:
        logging.error(f"Must be integer.", exc_info=True)
    except ZeroDivisionError:
        logging.error(f"You cannot divide by zero.", exc_info=True)
    else:
        logging.info("App successfully execute.")
    finally:
        logging.info("App successfully executed.")
        print("Executed")
        

safe_divide()