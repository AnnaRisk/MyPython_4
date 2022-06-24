# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

def func(arg1, arg2, arg3="third"):
    print(arg1, arg2, arg3)



def open_browser(browser,version,arg3="100"):
    pass
#func("тест1", "тест2", "тест3")

def go_to_companyname_homepage(open,page,company):
    pass

#func (arg1="привет", arg2 = "название", arg3= "компании")

def find_registration_button_on_login_page(click,button,login):
    pass

#func("проверка", "связи", "дз4")


l = (open_browser,go_to_companyname_homepage,find_registration_button_on_login_page)

for s in l:
    print(s)
