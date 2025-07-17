class StrAttributes:
    @staticmethod
    def upper_case_str(upper_name: str) -> str:
        return upper_name.upper()

    @staticmethod
    def lower_case_str(lower_name: str) -> str:
        return lower_name.lower()

    @staticmethod
    def capitalize_case_str(capitalize_first_letter: str) -> str:
        return capitalize_first_letter.capitalize()

    @staticmethod
    def title_case_str(title_str: str) -> str:
        return title_str.title()

    @staticmethod
    def swap_case_str(swap_str: str) -> str:
        return swap_str.swapcase()

    print("upper_case_str:", upper_case_str("roy"))
    print("lowe_case_str:", lower_case_str("ROY"))
    print("capitalize_case_str:", capitalize_case_str("roooOOOO"))
    print("title_case_str:", title_case_str("Pathetic, Prophecy, Divine, The Tale, Kingdom"))
    print("swap_case_str:", swap_case_str("LETS FIND how this really WORK."))


class StrBooleanAttributes:
    @staticmethod
    def is_alpha_case(is_alpha: str) -> bool:
        return is_alpha.isalpha()

    @staticmethod
    def is_digit_case(is_digit: str) -> bool:
        return is_digit.isdigit()

    @staticmethod
    def is_alpha_numeric(is_a_num: str) -> bool:
        return is_a_num.isalnum()

    @staticmethod
    def is_lower_case(is_lower: str) -> bool:
        return is_lower.islower()

    @staticmethod
    def is_upper_case(is_upper: str) -> bool:
        return is_upper.isupper()

    @staticmethod
    def is_space_case(is_space: str) -> bool:
        return is_space.isspace()

    @staticmethod
    def is_title_case(is_title: str) -> bool:
        return is_title.istitle()


    print(f"\nNOW THIS IS THE BOOLEAN TASKS:")
    print("is_alpha_case:", is_alpha_case("Hello"))
    print("is_alpha_case:", is_alpha_case("is an alphabetic?"))
    print("is_alpha_case:", is_alpha_case("98097865746753647657687{>{>?:"))
    print("is_digit:", is_digit_case("4567890"))
    print("is_digit:", is_digit_case("76"))
    print("is_lower_case:", is_lower_case("NO"))
    print("is_lower_case:", is_lower_case("yes"))
    print("is_upper_case:", is_upper_case("no"))
    print("is_upper_case:", is_upper_case("YES"))
    print("is_space_case:", is_space_case(" no "))
    print("is_space_case:", is_space_case(" "))
    print("is_title_case:", is_title_case("yeS"))
    print("is_title_case:", is_title_case("Yes"))
