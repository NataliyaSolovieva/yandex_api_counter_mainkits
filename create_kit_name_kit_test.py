import sender_stand_request
import data


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    # Копируется словарь с телом запроса из файла data
    current_kit_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_kit_body['name'] = name
    return current_kit_body


# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа раавен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле name и оно не пустое
    assert kit_response.json()['name'] == kit_body['name']


# Функция негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную response сохраняется результат
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа раавен 400
    assert response.status_code == 400


# Тест 1. Успешное создание набора. Допустимое количество символов (1)
def test_create_new_client_kit_1_letter_in_name_get_success_response():
    positive_assert('а')


# Тест 2. Успешное создание набора. Допустимое количество символов (511)
def test_create_new_client_kit_511_letter_in_name_get_success_response():
    positive_assert('Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    # abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')


# Тест 3. Ошибка. Количество символов меньше допустимого (0)
def test_create_new_client_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400('')


# Тест 4. Ошибка. Количество символов больше допустимого (512)
def test_create_new_client_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400('Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        # abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                        #abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')


# Тест 5. Успешное создание набора. Разрешены английские буквы
def test_create_new_client_kit_english_letter_in_name_get_success_response():
    positive_assert('QWErty')


# Тест 6. Успешное создание набора. Разрешены русские буквы
def test_create_new_client_kit_russian_letter_in_name_get_success_response():
    positive_assert('Мария')


# Тест 7. Успешное создание набора. Разрешены спецсимволы
def test_create_new_client_kit_special_characters_in_name_get_success_response():
    positive_assert('"№%@",')


# Тест 8. Успешное создание набора. Разрешены пробелы
def test_create_new_client_kit_spaces_allowed_in_name_get_success_response():
    positive_assert(' Человек и КО ')


# Тест 9. Успешное создание набора. Разрешены цифры
def test_create_new_client_kit_numbers_allowed_in_name_get_success_response():
    positive_assert(' Человек и КО ')


# Тест 10. Ошибка. Параметр не передан в запросе
def test_create_new_client_kit_parameter_not_passed_in_name_get_error_response():
    # В переменную kit_body не передается тело запроса
    kit_body = {}
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа раавен 400
    assert response.status_code == 400


# Тест 11. Ошибка. Передан другой тип параметра (число)
def test_create_new_client_kit_other_parameter_type_in_name_get_error_response():
    negative_assert_code_400(123)


