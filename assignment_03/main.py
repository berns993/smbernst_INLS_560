# This program determines whether you are qualified for a job (good luck!)

MIN_EXPERIENCE = 10  # The minimum number of relevant work experiences
MIN_YEARS = 5         # The minimum years of work
CONSTANT_1 = '5 years of relevant experience'
CONSTANT_2 = 'a specialist degree or equilvant relevant years of experience.'

# Get the applicant's number of relevant experiences.
work_history = float(input('Enter your number of relevant experiences (internships not included): '))

# Get applicant's number of years with relevant work experience.
years_on_job = int(input('Enter the number of ' +
                         'years employed (not including time in school): '))

# Determine whether the applicant qualifies for the job.
if work_history >= MIN_EXPERIENCE and years_on_job >= MIN_YEARS:
    print('Congratulations! You meet the minimum qualifications for the job. Someone from HR will be in touch to schedule an interview.')
else:
    print(f'''You do not qualify.
    You need {CONSTANT_1} and {CONSTANT_2}

    Due to the high volume of applications, we are not able to provide individual feedback to candidates. However, we do hope you'll stay connected with us and keep an eye on our future career opportunities. If a suitable position opens up again, we would be happy to hear from you and consider your application.
    ''')
