from time import sleep


# 段落打印，段首空一行
def p_print(text):

    print('\n' + text)


# 文本打印，自定义尾部换行
def text_print(text, end=True):
    if end:
        print(text)
    else:
        print(text, end='')


# 逐个字符打印
def char_print(text, header=True, end=True, time=0):
    if header:
        print()
    for c in text:
        print(c, end='', flush=True)
        if time:
            sleep(time)
    if end:
        print()
