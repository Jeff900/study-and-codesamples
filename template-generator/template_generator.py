from os import listdir

def get_templates() -> dict: 
    """Read the templates in files in folder `templates`. Stores filenames as
    key and file content as value.
    """
    templates = {}
    for file in listdir('./templates'):
        with open('./templates/' + file, 'r') as f:
            templates[file] = f.read()
    return templates


def contains_numbers(string):
    for item in string:
        if item.isdecimal():
            return True
    return False


def is_name_valid(name: str) -> bool:
    # First and last names: each minimum two characters and maximum ten
    # characters;
    # containing only alphabets, both starting with capital letters
    if not 2 <= len(name) <= 10:
        return False
    if not name[0].isupper():
        return False
    if not name.isalpha():
        return False
    return True


def is_title_valid(title: str) -> bool: 
    # Job title: minimum 10 characters without numbers
    if not len(title) >= 10:
        return False
    if contains_numbers(title):
        return False
    return True


def is_salary_valid(salary: str) -> bool:
    # Salary: valid floating point number between (and including) 20.000,00 and
    # 80.000,00
    salary = float(salary.replace('.', '').replace(',', '.'))
    if not type(salary) == float:
        return False
    if not 20000.00 <= float(salary) <= 80000.00:
        return False
    return True


def is_date_valid(date: str) -> bool:
    # Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31
    # month between 1 - 12, year only 2021 and 2022.
    year, month, day = date.split('-')
    month, day = int(month), int(day)

    if not year in ('2021', '2022'):
        return False
    if not 1 <= month <= 12:
        return False
    if not 1 <= day <= 31:
        return False
    return True


def job_offer_template(first_name, last_name, job_title, annual_salary, start_date):
    template = f'''Here is the final letter to send:
Dear {first_name} {last_name},
After careful evaluation of your application for the position of {job_title},
we are glad to offer you the job. Your salary will be {annual_salary} euro annually.
Your start date will be on {start_date}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
'''
    return template


def job_rejection_template(first_name, last_name, job_title, feedback):
    template = f'''Here is the final letter to send:
Dear {first_name} {last_name},
After careful evaluation of your application for the position of {job_title},
at this moment we have decided to proceed with another candidate.
'''
    print('Feedback:', feedback)
    if not feedback == '':
        template = template + f'Here we would like to provide you our feedback about the interview.\n{feedback}\n'
    template = template + 'We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.\n'
    template = template + 'Sincerely,\nHR Department of XYZ'
    return template


another_template = input('Another template? (Yes/No) ')

while another_template == 'Yes':
    template_type = input('Job Offer or Rejection? ')
    first_name = input('First Name? ')
    last_name = input('Last Name? ')
    job_title = input('Job Title? ')

    # print('is name valid:', is_name_valid(first_name))
    # print('is name valid:', is_name_valid(last_name))
    # print('is title valid:', is_title_valid(job_title))

    if is_name_valid(first_name) and is_name_valid(last_name)\
        and is_title_valid(job_title):

        if template_type == 'Job Offer':
            annual_salary = input('Annual Salary? ')
            start_date = input('Starting Date? (YYYY-MM-DD) ')
            if is_salary_valid(annual_salary) and is_date_valid(start_date):
                print(job_offer_template(
                    first_name, last_name, job_title, annual_salary, start_date))
            else:
                print('Input error')
        elif template_type == 'Rejection':
            give_feedback = input('Want to add feedback? ')
            if give_feedback == 'Yes':
                feedback = input('Feedback? ')
            else:
                feedback = ''

            print(job_rejection_template(
                first_name, last_name, job_title, feedback))
    else:
        print('Input error')

    another_template = input('Another template? (Yes/No) ')
