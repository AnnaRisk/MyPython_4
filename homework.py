# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

def func(arg1, arg2, arg3="third"):
    print(arg1, arg2, arg3)

func("hello!", arg2=123, arg3="321")


def open_browser():
    pass
#func("тест1", "тест2", "тест3")

def go_to_companyname_homepage():
    pass

#func (arg1="привет", arg2 = "название", arg3= "компании")

def find_registration_button_on_login_page():
    pass

#func("проверка", "связи", "дз4")


func (open_browser(),go_to_companyname_homepage(),find_registration_button_on_login_page())

l = (open_browser,go_to_companyname_homepage,find_registration_button_on_login_page)
for func.__name__ in l:
  string =  func.__name__
    print(string)