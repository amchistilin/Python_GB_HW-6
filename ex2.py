# программа смешивает имена валадельцев телефонов с их номерами
employee_numbers = [89161234567, 89091111111]
employee_names = ["Маша", "Валентин"]

zipped_values = zip(employee_names, employee_numbers)
new_list = list(zipped_values)

print(new_list)