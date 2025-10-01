# """
# - A function that will take in the input function and then split the input on the space and store in a list
# - create a function that checks that the only letter in the input is x, there are 2 operators between the 3 terms and that each term has a coefficient unless there is an x in the term. Also make sure that the only operators are (+) and (-). If not, raise a ValueError that explains what is wrong with the input to help the user provide the correct format for the input. Consider adding a three-level input that asks for each term on its own. that way it is easier to combine like terms and also ensure correct input.
#
# - create a class called derivative
#     - Break that input up into (+), (-), coefficient, and exponent. Make a function for each that assigns a value in the class (self.___) for each so we can use them throughout the class)
#     - Create a derivative function that multiplies the exponent by the coefficient AND THEN subtract 1 from the exponent.
#     - create a function that will check if the term is a function of x.
#         - If it is a x^2, make sure it returns just x, if it is x then just the coefficient
#     - create a function that combines like terms (looks at the exponent and combines the coefficients
# - the output should be in order of power (ex: 9x^2 + 6x - 3)
# """
#
# import os
#
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
#
# def valid_variable():
#     variable = input("""
# Welcome to the Derivative Calculator!
# Enter 3 terms and I will calculate your derivative...
#
# Step 1 - Enter your variable (i.e. x, y, t):
# """)
#     if not isinstance(variable, str) or len(variable) != 1 or not variable.isalpha():
#         print(f"""
#         Incorrect input ({variable}). Variable must be a single letter.
#         """)
#         return valid_variable()
#     else:
#         return variable
#
# variable = valid_variable()
#
# def variable_check(term, variable):
#     if not any(char.isalpha() for char in term):
#         return True
#     for char in term:
#         if char.isalpha() and char != variable:
#             return False
#     return True
#
# def term_one_check(var):
#     clear_screen()
#     term_one = input("""Term 1 (i.e. 3x^2):
#     """)
#     tf = variable_check(term_one, var)
#     if tf:
#         return term_one
#     else:
#         print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
#         return term_one_check(var)
#
# term_one = term_one_check(variable)
#
# def term_two_check(var):
#     clear_screen()
#     term_two = input("""Term 2:
#     """)
#     tf = variable_check(term_two, var)
#     if tf:
#         return term_two
#     else:
#         print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
#         return term_two_check(var)
#
# term_two = term_two_check(variable)
#
# def term_three_check(var):
#     clear_screen()
#     term_three = input("""Term 3:
#     """)
#     tf = variable_check(term_three, var)
#     if tf:
#         return term_three
#     else:
#         print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
#         return term_three_check(var)
#
# term_three = term_three_check(variable)
#
# def term_filter(term):
#     variable = ''
#     coefficient = 0
#     exponent = 1
#
#
#     for char in term:
#         if char.isalpha():
#             variable = char
#             break
#
#
#     index = term.find(variable)
#     coefficient = term[:index]
#     if coefficient == '' or coefficient == '-':
#         coefficient += '1'
#     coefficient = int(coefficient)
#
#
#     if '^' in term:
#         exp_index = term.find('^')
#         exponent = int(term[exp_index + 1:])
#     elif variable == '':
#         exponent = 0
#
#     if variable == '':
#         if exponent == 0:
#             coefficient = 0
#             return coefficient, variable, exponent
#     else:
#         return coefficient, variable, exponent
#
#
# print(term_filter(term_one))
# print(term_filter(term_two))
# print(term_filter(term_three))
#
# term_one = term_filter(term_one)
# term_two = term_filter(term_two)
# term_three = term_filter(term_three)
#
# equation = []
#
# def calc_derivative(term):
#     if isinstance(term[2], int) and term[2] > 2:
#         equation.append(f"{term[0] * term[2]}{term[1]}^{term[2] - 1}")
#     elif term[1] == '':
#         equation.append('0')
#     # elif len(term) == 1:
#     #     if not any(char.isalpha() for char in term):
#     #         return 0
#     elif isinstance(term[2], str):
#         equation.append(f"{term[0]}")
#     else:
#         equation.append(f"{term[0] * term[2]}{term[1]}")
#
#
# # Original combine_like_terms() with all the IFs:
#     # def combine_like_terms(equation):
#     #     term_one = term_filter(equation[0])
#     #     term_two = term_filter(equation[1])
#     #     term_three = term_filter(equation[2])
#     #
#     #     # Create new value for each line to append to. meaning instead of printing, it stores the new equation here that way you can then create if-statements to check the value of the exponent that way the answer is never (30t^)
#     #
#     #     if term_one[2] == term_two[2] and term_one[2] == term_three[2]:
#     #         if term_one[2] == '':
#     #             return f"{term_one[0] + term_two[0] + term_three[0]}{term_one[1]}"
#     #         else:
#     #             return f"{term_one[0] + term_two[0] + term_three[0]}{term_one[1]}^{term_one[2]}"
#     #         # print(f"{term_one[0] + term_two[0] + term_three[0]}{term_one[1]}^{term_one[2]}")
#     #     elif term_one[2] == term_two[2]:
#     #         if term_one[2] != term_three[2]:
#     #             if term_three[0] < 0:
#     #                 return f"{term_one[0] + term_two[0]}{term_one[1]}{term_one[2]} {term_three[0]}{term_three[1]}^{term_three[2]}"
#     #                 # print(f"{term_one[0] + term_two[0]}{term_one[1]}{term_one[2]} {term_three[0]}{term_three[1]}^{term_three[2]}")
#     #             else:
#     #                 return f"{term_one[0] + term_two[0]}{term_one[1]}{term_one[2]} + {term_three[0]}{term_three[1]}^{term_three[2]}"
#     #                 # print(f"{term_one[0] + term_two[0]}{term_one[1]}{term_one[2]} + {term_three[0]}{term_three[1]}^{term_three[2]}")
#     #     elif term_one[2] == term_three[2]:
#     #         if term_one[2] != term_two[2]:
#     #             if term_two[0] < 0:
#     #                 return f"{term_one[0] + term_three[0]}{term_one[1]}{term_one[2]} {term_two[0]}{term_two[1]}^{term_two[2]}"
#     #                 # print(f"{term_one[0] + term_three[0]}{term_one[1]}{term_one[2]} {term_two[0]}{term_two[1]}^{term_two[2]}")
#     #             else:
#     #                 return f"{term_one[0] + term_three[0]}{term_one[1]}{term_one[2]} + {term_two[0]}{term_two[1]}^{term_two[2]}"
#     #                 # print(f"{term_one[0] + term_three[0]}{term_one[1]}{term_one[2]} + {term_two[0]}{term_two[1]}^{term_two[2]}")
#     #     elif term_one[2] != term_two[2] and term_two[2] == term_three[2]:
#     #         if term_one[0] < 0:
#     #             return f"{term_two[0] + term_three[0]}{term_two[1]}^{term_three[2]} {term_one[0]}{term_one[1]}^{term_one[2]}"
#     #             # print(f"{term_two[0] + term_three[0]}{term_two[1]}^{term_three[2]} {term_one[0]}{term_one[1]}^{term_one[2]}")
#     #         else:
#     #             return f"{term_two[0] + term_three[0]}{term_two[1]}^{term_three[2]} + {term_one[0]}{term_one[1]}^{term_one[2]}"
#     #             # print(f"{term_two[0] + term_three[0]}{term_two[1]}^{term_three[2]} + {term_one[0]}{term_one[1]}^{term_one[2]}")
#     #     elif term_one[2] != term_three[2] and term_two[2] != term_three[2] and term_three[2] != term_one[2]:
#     #         return (f"{term_one[0]}{term_one[1]}^{term_one[2]} {term_two[0]}{term_two[1]}^{term_two[2]} {term_three[0]}{term_three[1]}^{term_three[2]}")
#     #         # print(f"{term_one[0]}{term_one[1]}^{term_one[2]} {term_two[0]}{term_two[1]}^{term_two[2]} {term_three[0]}{term_three[1]}^{term_three[2]}")
#
# def format_term(coef, var, exp):
#     if exp == 0:
#         return f"{coef}"
#     elif exp == 1:
#         return f"{coef}{var}"
#     else:
#         return f"{coef}{var}^{exp}"
#
# # def combine_like_terms(equation):
# #     term_one = term_filter(equation[0])
# #     term_two = term_filter(equation[1])
# #     term_three = term_filter(equation[2])
# #
# #     if term_one[2] == term_two[2] == term_three[2]:
# #         return format_term(term_one[0] + term_two[0] + term_three[0], term_one[1], term_one[2])
# #
# #     elif term_one[2] == term_two[2]:
# #         combined = format_term(term_one[0] + term_two[0], term_one[1], term_one[2])
# #         remaining = format_term(term_three[0], term_three[1], term_three[2])
# #         return f"{combined} + {remaining}" if term_three[0] > 0 else f"{combined} {remaining}"
# #
# #     elif term_one[2] == term_three[2]:
# #         combined = format_term(term_one[0] + term_three[0], term_one[1], term_one[2])
# #         remaining = format_term(term_two[0], term_two[1], term_two[2])
# #         return f"{combined} + {remaining}" if term_two[0] > 0 else f"{combined} {remaining}"
# #
# #     elif term_two[2] == term_three[2]:
# #         combined = format_term(term_two[0] + term_three[0], term_two[1], term_two[2])
# #         remaining = format_term(term_one[0], term_one[1], term_one[2])
# #         return f"{combined} + {remaining}" if term_one[0] > 0 else f"{combined} {remaining}"
# #
# #     else:
# #         parts = [format_term(*term_one), format_term(*term_two), format_term(*term_three)]
# #         output = f" {' '.join(['+ ' + p if not p.startswith('-') else p for p in parts])}"
# #         return output.strip()
#
#
# def combine_like_terms(equation):
#     filtered_terms = [term_filter(term) for term in equation]
#
#     while len(filtered_terms) < 3:
#         filtered_terms.append((0, '', 0))
#
#     term_one, term_two, term_three = filtered_terms
#
#     if term_one[2] == term_two[2] == term_three[2]:
#         return format_term(term_one[0] + term_two[0] + term_three[0], term_one[1], term_one[2])
#
#     elif term_one[2] == term_two[2]:
#         combined = format_term(term_one[0] + term_two[0], term_one[1], term_one[2])
#         remaining = format_term(term_three[0], term_three[1], term_three[2])
#         return f"{combined} + {remaining}" if term_three[0] > 0 else f"{combined} {remaining}"
#
#     elif term_one[2] == term_three[2]:
#         combined = format_term(term_one[0] + term_three[0], term_one[1], term_one[2])
#         remaining = format_term(term_two[0], term_two[1], term_two[2])
#         return f"{combined} + {remaining}" if term_two[0] > 0 else f"{combined} {remaining}"
#
#     elif term_two[2] == term_three[2]:
#         combined = format_term(term_two[0] + term_three[0], term_two[1], term_two[2])
#         remaining = format_term(term_one[0], term_one[1], term_one[2])
#         return f"{combined} + {remaining}" if term_one[0] > 0 else f"{combined} {remaining}"
#
#     else:
#         parts = [format_term(*term_one), format_term(*term_two), format_term(*term_three)]
#         output = f" {' '.join(['+ ' + p if not p.startswith('-') else p for p in parts if not p.startswith('0')])}"
#         return output.strip()
#
#
#
# calc_derivative(term_one)
# calc_derivative(term_two)
# calc_derivative(term_three)
#
# non_zero_equation = [term for term in equation if term != "0"]
#
# if not non_zero_equation:
#     print("0")
# else:
#     print(combine_like_terms(non_zero_equation))


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_variable():
    variable = input("""
Welcome to the Derivative Calculator!
Enter 3 terms and I will calculate your derivative...

Step 1 - Enter your variable (i.e. x, y, t): 
""")
    if not isinstance(variable, str) or len(variable) != 1 or not variable.isalpha():
        print(f"""
        Incorrect input ({variable}). Variable must be a single letter.
        """)
        return valid_variable()
    else:
        return variable

variable = valid_variable()

def variable_check(term, variable):
    if not any(char.isalpha() for char in term):
        return True
    for char in term:
        if char.isalpha() and char != variable:
            return False
    return True

def term_one_check(var):
    clear_screen()
    term_one = input("Term 1 (i.e. 3x^2): ")
    tf = variable_check(term_one, var)
    if tf:
        return term_one
    else:
        print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
        return term_one_check(var)

def term_two_check(var):
    clear_screen()
    term_two = input("Term 2: ")
    tf = variable_check(term_two, var)
    if tf:
        return term_two
    else:
        print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
        return term_two_check(var)

def term_three_check(var):
    clear_screen()
    term_three = input("Term 3: ")
    tf = variable_check(term_three, var)
    if tf:
        return term_three
    else:
        print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
        return term_three_check(var)

term_one = term_one_check(variable)
term_two = term_two_check(variable)
term_three = term_three_check(variable)

def term_filter(term):
    variable = ''
    coefficient = 0
    exponent = 1

    for char in term:
        if char.isalpha():
            variable = char
            break

    if variable:
        index = term.find(variable)
        coefficient_part = term[:index]
        if coefficient_part == '' or coefficient_part == '-':
            coefficient_part += '1'
        coefficient = int(coefficient_part)

        if '^' in term:
            exp_index = term.find('^')
            exponent = int(term[exp_index + 1:])
        else:
            exponent = 1
    else:
        coefficient = int(term)
        exponent = 0

    return coefficient, variable, exponent

term_one = term_filter(term_one)
term_two = term_filter(term_two)
term_three = term_filter(term_three)

# Calculate derivative
equation = []

def calc_derivative(term):
    if term[2] == 0:
        equation.append("0")
    elif term[2] == 1:
        equation.append(f"{term[0]}")
    else:
        equation.append(f"{term[0] * term[2]}{term[1]}^{term[2] - 1}")

def format_term(coef, var, exp):
    if exp == 0:
         return f"{coef}"
    elif exp == 1:
         return f"{coef}{var}"
    else:
         return f"{coef}{var}^{exp}"

def combine_like_terms(equation):
    filtered_terms = [term_filter(term) for term in equation if term != "0"]

    combined = {}

    for coef, var, exp in filtered_terms:
        if exp in combined:
            combined[exp][0] += coef
        else:
            combined[exp] = [coef, var]

    sorted_terms = sorted(combined.items(), key=lambda x: -x[0])

    formatted_terms = []
    for exp, (coef, var) in sorted_terms:
        formatted_terms.append(format_term(coef, var, exp))

    return " + ".join(formatted_terms)

calc_derivative(term_one)
calc_derivative(term_two)
calc_derivative(term_three)

non_zero_equation = [term for term in equation if term != "0"]

if not non_zero_equation:
    print("0")
else:
    result = combine_like_terms(non_zero_equation)
    print(result)
