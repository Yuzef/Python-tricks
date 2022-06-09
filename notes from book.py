# this is a file for tests

def yell(text):
    return text.upper() + '!'

bark = yell

print(bark('гав'))

# del yell  а доступ к функции через другое имя bark остался 

print(bark('гав'))


# functions can be added to a list
func = [bark, str.lower, str.capitalize]
print(func)
# access is the same
for f in func:
    print(f, f('всем привет'))

print(1,2,50,bark("efwef"))
# calling object-function without assigning a variable
print(func[0]('приветище'))

# function inside another function
# например, на результирующее приветствие можно влиять,
# передавая различные функции
def greet(func):
    greeting = func('Привет! Я - программа Python')
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower() + '...'

greet(whisper)
# таким образом мы раздаем "поведение"
# Функции, которые в качестве аргументов
# могут принимать другие функции, называются
# Функциями более высокого порядка (higher-order function)
# Классический пример такой функции:
gr_list = list(map(bark,['эй', 'привет', 'здравствуй']))
print(gr_list)

# -------------------------------------------------------
#NESTED FUNCTIONS OR INNER FUNCTIONS - ВЛОЖЕННЫЕ ФУНКЦИИ

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

print(speak('Привет, Мир'))

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if  volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(0.3))
print(get_speak_func(0.7))

speak_func = get_speak_func(0.7)
print(speak_func('Привет'))

# c.72
# Таким образом функции могут возвращать линии поведения

# -------------------------------------------------------
# ВНУТРЕННИЕ ФУНКЦИИ МОГУТ
# ЗАХВАТЫВАТЬ И УНОСИТЬ С СОБОЙ ЧАСТЬ СОСТОЯНИЯ
# РОДИТЕЛЬСКОЙ ФУНКЦИИ

# перепишем код функции get_speak_func
# новая версия сразу принимает аргументы text и volume,
# чтобы немедленно сделать возвращаемую функцию вызываемой
# Также нет аргумента text во внутренних функциях
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
    
print(get_speak_func('Привет, Мир', 0.7)())
# Функции, которые таким образом помнят значения из своего
# контекста, называются лекс.ЗАМЫКАНИЯМИ (lexical closure)
# Значения запоминаются, даже когда поток управления
# программы больше не находится в этом контексте

# ПРАКТИЧЕСКИЙ СМЫСЛ
# Функции могут не только возвращать линии поведения,
# но и предварительно КОНФИГУРИРОВАТЬ эти линии поведения.

def make_adder(n):
    def add(x):
        return x + n
    return add

# make_adder служит ФАБРИКОЙ для создания и конфигурирования
# функций-сумматоров

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

# -------------------------------------------------------
# ОБЪЕКТЫ МОГУТ ВЕСТИ СЕБЯ КАК ФУНКЦИИ

# Не все объекты являются функциями, но они могут быть
# сделаны ВЫЗЫВАЕМЫМИ

# Если объект является вызываемым, то с ним можно
# использовать синтаксис функций

# Всё приводится в действие дандер-методом __call__

class Adder:
    def __init__(self, n): # теперь у объекта есть аттрибут
        self.n = n         # n = тому с чем его проинициализировали

    def __call__(self, x): # если вызовем объект как ф-цию,
        return self.n + x  # то исполн-ся этот метод

plus_4 = Adder(4)
print(plus_4(5))

# Произошел "вызов" экземпляра объекта в качестве ф-ции,
# что сводится к исполнению метода __call__ этого объекта.

# НЕ ВСЕ ОБЪЕКТЫ ЯВЛЯЮТСЯ ВЫЗЫВАЕМЫМИ
# Пр-ка через встроенную ф-цию callable

print(callable(plus_4))
print(callable(Adder(4)))
print(callable(yell))
print(callable('Привет'))

# -------------------------------------------------------
# с.75 ЛЯМБДЫ - Ф-ЦИИ ОДНОГО ВЫРАЖЕНИЯ
# (небольшие анонимные ф-ции через ключ. слово lambda)

# От обычной ф-ции ничем не отличаются - возвращают
# объект-функцию
add = lambda x, y: x + y
print(add(5, 3))

# функциональное выражение
print((lambda x, y: x + y)(5,3))
# не пришлось связывать объект-функцию с именем (анонимность)

# лямбды ограничены одним-единственным выражением - в лямбдах
# не могут применяться инструкции или аннотации
# return присутствует НЕЯВНО
# Лямбды также называют ФУНКЦИЯМИ ОДНОГО ВЫРАЖЕНИЯ






























