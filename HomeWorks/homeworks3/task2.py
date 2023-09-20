""""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

text = '5. «Почему это я должен тестировать? Я же не тестировщик!» ' \
       'В некоторых командах ответственность за отладку всецело лежит на тестировщиках.\
Разработчики не утруждают себя тратой времени на самые очевидные unit-тесты. Они уверены,\
что это не их работа. По большому счету, так и есть,\
    хотя существуют разные точки зрения на вопрос (с мнениями сообщества можно ознакомиться здесь).\
Что может пойти не так: Тестировщикам в такой ситуации приходится разбираться со всеми \
недочетами подряд — даже с самыми примитивными и глупыми ошибками. Разумеется, это раздражает.\
Как быть: Многие разработчики выступают за самостоятельные тесты перед отправкой в QA-отдел. ' \
       'Это помогает не только разгрузить тестировщиков, но и научиться смотреть на продукт с точки' \
       ' зрения критика и пользователя. Есть мнение, что это полезно для профессионалов и лучшим ' \
       'образом сказывается на конечном результате. Для тех, кто не хочет себя утруждать проверками,' \
       ' есть автоматические инструменты. Они помогают найти самые очевидные баги. ' \
       'В любом случае — даже если в команде есть QA-инженеры, жесткое разделение на разработчиков' \
       ' и QA — не самый оптимальный подход.'
from collections import Counter
import re

cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', text))
print(cnt.most_common(10))