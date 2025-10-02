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
    term_one = input("Term 1 (i.e. 3x^2): ")
    tf = variable_check(term_one, var)
    if tf:
        return term_one
    else:
        print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
        return term_one_check(var)


def term_two_check(var):
    term_two = input("Term 2: ")
    tf = variable_check(term_two, var)
    if tf:
        return term_two
    else:
        print(f"Incorrect variable, please enter terms using {var} or no variable at all.")
        return term_two_check(var)


def term_three_check(var):
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
