# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
def create_dict(**kwargs):
    result = {}
    for arg_name, arg_value in kwargs.items():
        if isinstance(arg_value, (int, float, str, bool, tuple, frozenset, bytes)):
            result[arg_value] = arg_name
        else:
            result[str(arg_value)] = arg_name
    return result


params_dict = create_dict(name="ivan", age=30, city="krim",
                          favorite_color="red", hobby=["games ps4", "to swim"])
print(params_dict)