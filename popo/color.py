from colored import fg, attr
from popo import pprint as p
from popo import views as v


reset = attr('reset')


def next(message='', header=False):
    if header:
        print()
    message = fg(242) + message + reset
    back = fg(114) + '↵' + reset
    input(message + back)


def _input(message=''):
    print()
    notice = fg(114) + '> 请输入' + reset
    message = fg(242) + message + reset
    while True:
        text = input(notice + message + ' ').strip()
        if text:
            break
    return text


def tilte(text, header=True, end=True, time=0.1):  # 标题提示语，首尾换行，逐字打印
    color = fg(4)
    p.char_print(color + text + reset, header, end, time)


def info(text, end=True):  # 系统信息，浅灰色，直接打印，自定义尾换行
    color = fg(242)
    p.text_print(color + text + reset, end)


def caption(text, end=False):  # 系统重要信息，如用户名，版本
    color = fg(69)
    p.text_print(color + text + reset, end)


def error(text, end=True):  # 错误信息，需空一行打印
    color = fg(166)
    p.text_print(color + '\n' + text + reset, end)


def talk(text, header=True, end=False, time=0.1):  # 对话信息
    color = fg(182)
    p.char_print(color + text + reset, header, end, time)
    next()


def option(text, header=False, end=True, time=0.1):  # 用户选项
    color = fg(26)
    p.char_print(color + text + reset, header, end, time)


def div(text, end=True):
    color = fg(240)
    p.text_print(color + text + reset, end)


def label(text, end=False):  # 标签名，首尾都不换行
    color = fg(12)
    p.text_print(color + text + reset, end)


def vname(text, end=False):
    color = fg(140)
    p.text_print(color + text + reset, end)


def profile(text):
    color = fg(140)
    p.text_print(color + text + reset)


def index(text, end=True):
    color = fg(221)
    p.text_print(color + text + reset, end)


def sub(text, end=True):  # 下标信息，浅灰色，直接打印，自定义尾换行
    color = fg(239)
    p.text_print(color + ' (' + text + ')' + reset, end)


def vmap(text):
    color = fg(221)
    p.text_print(color + text + '\n' + reset)


def confirm(text):
    color = fg(208)
    return color + text + reset


def sendkey(text):
    notice = fg(114) + '> 请输入' + reset
    cmd = fg(242) + ' 指令' + reset
    _or = fg(172) + ' | ' + reset
    message = fg(242) + text + reset
    return notice + cmd + _or + message + ' '


def rename(text):
    return fg(114) + text + reset
