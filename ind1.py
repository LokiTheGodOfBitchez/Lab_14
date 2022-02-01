#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fun(strings):

    def replacer(name, surname):
        nonlocal strings
        repl = strings.replace("%F%", surname)
        repl = repl.replace("%N%", name)
        return repl
    return replacer


if __name__ == '__main__':
    replace = fun("Уважаемый %F% %N%! Вы задолжали кучу лаб по ОПИ!")
    print(replace('Илья', 'Ваньянц'))
