import datetime


class InvalidDataError(Exception):
    pass


def validate_data(data):
    # Разбиваем введенные данные на список
    input_data = data.split()

    # Проверяем, что количество данных соответствует требованиям
    if len(input_data) != 6:
        raise InvalidDataError("Неверное количество данных")

    # Проверяем формат фамилии, имени и отчества
    if not all(name.isalpha() for name in input_data[:3]):
        raise InvalidDataError("Неверный формат фамилии, имени или отчества")

    # Проверяем формат даты рождения
    try:
        birth_date = datetime.datetime.strptime(input_data[3], "%d.%m.%Y")
    except ValueError:
        raise InvalidDataError("Неверный формат даты рождения")

    # Проверяем формат номера телефона
    if not input_data[4].isdigit():
        raise InvalidDataError("Неверный формат номера телефона")

    # Проверяем формат пола
    if input_data[5] not in ['m', 'f']:
        raise InvalidDataError("Неверный формат пола")

    # Возвращаем данные в виде словаря
    return {
        'surname': input_data[0],
        'name': input_data[1],
        'patronymic': input_data[2],
        'birth_date': input_data[3],
        'phone_number': input_data[4],
        'gender': input_data[5]
    }


def write_to_file(data):
    # Открываем файл для записи
    try:
        file_name = data['surname'] + '.txt'
        with open(file_name, 'a') as file:
            # Записываем данные в файл
            file.write(
                f"{data['surname']} {data['name']} {data['patronymic']} {data['birth_date']} {data['phone_number']} {data['gender']}\n"
            )
            print("Данные успешно записаны в файл.")
    except IOError as e:
        print(f"Произошла ошибка при записи в файл: {str(e)}")


def main():
    try:
        # Запрашиваем данные у пользователя
        user_input = input("Введите данные ФИО, дата рождения (00.00.0000), номер тел и пол (f или m): ")

        # Проверяем и обрабатываем введенные данные
        try:
            parsed_data = validate_data(user_input)
        except InvalidDataError as e:
            print(f"Неверные данные: {str(e)}")
            return

        # Записываем данные в файл
        write_to_file(parsed_data)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
