function_of_x = input("""
Welcome to the Derivative Calculator!
Enter a function of x [f(x)] that consists 
of 3 values and is separated by spaces...
(i.e. 3x^4 + 5x^2 - 2): 
""")
parts_of_function_of_x = function_of_x.split(' ')
operators = ['+', '-', '*', '**']

class Derivative:
    def __init__(self, parts_of_function_of_x):
        if len(parts_of_function_of_x) != 5:
            raise ValueError("Incorrect Format. There must be exactly 3 terms.")

        self.first_value = parts_of_function_of_x[0]
        self.second_value = parts_of_function_of_x[2]
        self.third_value = parts_of_function_of_x[4]
        self.v_one_d = ''
        self.v_two_d = ''
        self.v_three_d = ''


    def display_values(self):
        print(f"First Value: {self.first_value}")
        print(f"Second Value: {self.second_value}")
        print(f"Third Value: {self.third_value}")

    def coefficient_check(self, value):
        x = [char for char in value]
        counter = 0

        while counter < len(value):
            if value[counter] == 'x':
                break
            counter += 1

        coefficient = value[:counter]

        return int(coefficient)

    def exponent_check(self, value):
        x = [char for char in value]
        counter = 0

        while counter < len(value):
            if value[counter] == '^':
                break
            counter += 1

        exponent = value[counter + 1:]

        return int(exponent)

    def combine_like_terms(self):
        term_one = self.v_one_d
        term_two = self.v_two_d
        term_three = self.v_three_d
        t_o_c = self.coefficient_check(term_one)
        t_t_c = self.coefficient_check(term_two)
        t_th_c = self.coefficient_check(term_three)
        t_o_e = self.exponent_check(term_one)
        t_t_e = self.exponent_check(term_two)
        t_th_e = self.exponent_check(term_three)

        if t_o_e == t_t_e and t_o_e == t_th_e:
            return f"{t_o_c + t_t_c + t_th_c}x^{t_o_e}"
        elif t_o_e == t_t_e and t_o_e != t_th_e:
            return f"{t_o_c + t_t_c}x^{t_o_e} + {t_th_c}x^{t_th_e}"
        elif t_o_e != t_th_e and t_o_e != t_th_e:
            return f"{t_o_c}x^{t_o_e} {parts_of_function_of_x[1]} {t_t_c}x^{t_t_e} {parts_of_function_of_x[3]} {t_th_c}x^{t_th_e}"
        # create a function that checks for like terms and then if grabs the terms and their (+) or (-) sign so that it can calculate the new coefficient.
        # create a check for the exponent that it can only be whole / real numbers
        # create a function that checks that the terms are only being added or subtracted from each other.

    def compute_first_values_derivative(self):
        if "x" in self.first_value:
            if "^" in self.first_value:
                exponent = self.exponent_check(self.first_value)
                coefficient = self.coefficient_check(self.first_value)
                new_coefficient = coefficient * exponent
                new_exponent = exponent - 1
                if new_exponent == 1:
                    self.v_one_d =  f"{new_coefficient}x"
                elif new_exponent == 0:
                    self.v_one_d =  f"{new_coefficient}"
                else:
                    self.v_one_d =  f"{new_coefficient}x^{new_exponent}"

        return ''

    def compute_second_values_derivative(self):
        if "x" in self.second_value:
            if "^" in self.second_value:
                exponent = self.exponent_check(self.second_value)
                coefficient = self.coefficient_check(self.second_value)
                new_coefficient = coefficient * exponent
                new_exponent = exponent - 1
                if new_exponent == 1:
                    self.v_two_d =  f"{new_coefficient}x"
                elif new_exponent == 0:
                    self.v_two_d =  f"{new_coefficient}"
                else:
                    self.v_two_d =  f"{new_coefficient}x^{new_exponent}"

        return ''

    def compute_third_values_derivative(self):
        if "x" in self.third_value:
            if "^" in self.third_value:
                exponent = self.exponent_check(self.third_value)
                coefficient = self.coefficient_check(self.third_value)
                new_coefficient = coefficient * exponent
                new_exponent = exponent - 1
                if new_exponent == 1:
                    self.v_three_d =  f"{new_coefficient}x"
                elif new_exponent == 0:
                    self.v_three_d =  f"{new_coefficient}"
                else:
                    self.v_three_d =  f"{new_coefficient}x^{new_exponent}"

        return ''

    def f_prime_x(self):
        if self.v_one_d != '':
            if self.v_two_d != '':
                if self.v_three_d != '':
                    return f"{self.v_one_d} {parts_of_function_of_x[1]} {self.v_two_d} {parts_of_function_of_x[3]} {self.v_three_d}"
                else:
                    return f"{self.v_one_d} {parts_of_function_of_x[1]} {self.v_two_d}"
            elif self.v_two_d == '' and self.v_three_d != '':
                return f"{self.v_one_d} {parts_of_function_of_x[3]} {self.v_three_d}"
            elif self.v_two_d == '' and self.v_three_d == '':
                return f"{self.v_one_d}"
        elif self.v_one_d == '' and self.v_two_d != '' and self.v_three_d != '':
            return f"{parts_of_function_of_x[1]}{self.v_two_d} {parts_of_function_of_x[3]} {self.v_three_d}"
        elif self.v_one_d == '' and self.v_two_d == '' and self.v_three_d != '':
            return f"{parts_of_function_of_x[3]}{self.v_three_d}"
        elif self.v_one_d == '' and self.v_two_d == '' and self.v_three_d == '':
            return 0

derivative = Derivative(parts_of_function_of_x)
derivative.compute_first_values_derivative()
derivative.compute_second_values_derivative()
derivative.compute_third_values_derivative()

print(derivative.f_prime_x())
print(derivative.combine_like_terms())

"""
Need to work on 
- combining same power values
- reorder so the output is in order of power
"""