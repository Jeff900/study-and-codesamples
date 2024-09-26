"""template_generator generates textual templates based on template files and
command line user input. It is an extension on a little school project and
primarily intented as reference and portfolio.
"""

from os import listdir

def get_templates() -> dict:
    """Read the templates in files in folder `templates`. Stores filenames as
    key and file content as value.
    """
    templates = []
    for file in listdir('./templates'):
        templates.append(file)
    return templates

def is_valid_template(template: str) -> bool:
    """Verifies if template exists"""
    if not template in templates:
        return False
    return True


def contains_numbers(string: str) -> bool:
    """Checks if string contains decimal numbers."""
    for item in string:
        if item.isdecimal():
            return True
    return False


def is_name_valid(name: str) -> bool:
    """Verifies if string has valid length, if string does not start with upper
    case and if characters are all alphabetical"""
    if not 2 <= len(name) <= 10:
        return False
    if not name[0].isupper():
        return False
    if not name.isalpha():
        return False
    return True


def is_title_valid(title: str) -> bool:
    """Verifies if string has valid length and if does not contain numbers"""
    if not len(title) >= 10:
        return False
    if contains_numbers(title):
        return False
    return True


def is_salary_valid(salary: str) -> bool:
    """Verifies to format of salary and of the salary is withing particular
    range"""
    salary = float(salary.replace('.', '').replace(',', '.'))
    if type(salary) != float:
        return False
    if not 20000.00 <= float(salary) <= 80000.00:
        return False
    return True


def is_date_valid(date: str) -> bool:
    """Verifies the date format (YYYY-MM-DD)"""
    year, month, day = date.split('-')
    month, day = int(month), int(day)

    if not year in ('2021', '2022'):
        return False
    if not 1 <= month <= 12:
        return False
    if not 1 <= day <= 31:
        return False
    return True


def job_offer_template():
    with open('./templates/' + template_type, 'r') as f:
        template = f.read()
    template = template.format(
        first_name=first_name,
        last_name=last_name,
        job_title=job_title,
        annual_salary=annual_salary,
        start_date=start_date
    )
    return template


def job_rejection_template():
    with open('./templates/' + template_type, 'r') as f:
        template = f.read()
    template = template.format(
        first_name=first_name,
        last_name=last_name,
        job_title=job_title,
        feedback=feedback
    )
    # if not feedback == '':
    #     template = template + f'Here we would like to provide you our feedback about the interview.\n{feedback}\n'
    return template


another_template = 'Yes'
templates = get_templates()

while another_template == 'Yes':
    template_type = input('Job Offer or Rejection? ')
    while not is_valid_template(template_type):
        template_type = input('Job Offer or Rejection? ')
    first_name = input('First Name? ')
    last_name = input('Last Name? ')
    job_title = input('Job Title? ')

    if is_name_valid(first_name) and is_name_valid(last_name)\
        and is_title_valid(job_title):

        if template_type == 'job_offer':
            annual_salary = input('Annual Salary? ')
            start_date = input('Starting Date? (YYYY-MM-DD) ')
            if is_salary_valid(annual_salary) and is_date_valid(start_date):
                print(job_offer_template())
            else:
                print('Input error')
        elif template_type == 'rejection':
            give_feedback = input('Want to add feedback? ')
            if give_feedback == 'Yes':
                feedback = input('Feedback? ')
            else:
                feedback = ''

            print(job_rejection_template())
    else:
        print('Input error')

    another_template = input('Another template? (Yes/No) ')
