name = input('Ваше имя: ')
age_str = input('Ваш возраст: ')
subjects_str = input('Любимые предметы (через запятую): ')
age = int(age_str)
subjects_list = [subject.strip() for subject in subjects_str.split(",")]
student = {
    'name': name,
    'age': age,
    'subjects': subjects_list
}
print('=' * 30)
print('АНКЕТА СТУДЕНТА')
print('=' * 30)
print('Имя:', student['name'])
print('Возраст:', student['age'])
print('Любимые предметы:', student['subjects'])
print('=' * 30)
