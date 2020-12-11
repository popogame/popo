from random import randint, sample
from popo import g
from popo import color


fruit = {
    'name': '泡泡水果店',
    'class': 'Fruit',
    'actions': {'1': {'name': '收银', 'func': 'cash'},
                '2': {'name': '领工钱', 'func': 'wage'}
                }
}

noodle = {
    'name': '重庆小面馆',
    'class': 'Noodle',
    'actions': {'1': {'name': '点单', 'func': 'order'},
                '2': {'name': '开吃', 'func': 'dine'},
                '3': {'name': '买单', 'func': 'pay'}
                }
}


class App():

    def __init__(self, _id, module):
        self.id = _id
        self.module = module

        self.name = '泡泡大街'
        self.level = 1
        self.scenes = {'1': fruit, '2': noodle}


prices = {'橘子': 3, '葡萄': 12, '毛桃': 9, '香蕉': 6, '苹果': 7, '榴莲': 48}


class Fruit():

    def __init__(self):
        self.paid = 0
        self.fine = 0

    def cash(self, text):

        cart = sample(prices.keys(), randint(1, 4))
        weight = {}
        total = 0
        # checklist = ''
        color.info('\n有一位顾客的购物清单如下:\n')
        for fruit in cart:
            weight[fruit] = randint(1, 9)
            total += prices[fruit] * weight[fruit]
            color.option(f'{fruit:>4}  {prices[fruit]:>2} * {weight[fruit]}')
        color.info('-----------------------')
        text = color._input('总价格:')
        if text == str(total):
            self.paid += 10
            color.talk('收银正确，请继续加油吧~')
        else:
            self.fine += 10
            g.player.coins = -10
            color.talk('啊哦，收银错误，倒扣10块！')

    def wage(self, text):

        if self.fine > 0:
            color.talk(f'钱都收错了，真是不用心啊，你被罚了 { self.fine} 元')
            if self.paid > 0:
                color.talk(f'不过好在你也算对了几次，赚了 {self.paid} 元')
        elif self.paid == 0:
            color.talk('你今天偷懒了吧，都没来上班，还想要工钱？')
        else:
            g.player.coins = self.paid
            color.talk(f'恭喜你，今天赚了 {self.paid - self.fine} 元!')
            color.talk(f'你现在总金币为: {g.player.data["coins"]["balance"]} 元。')


class Noodle():

    def __init__(self):
        pass

    def order(self, text):
        color.next('开发中...', header=True)

    def dine(self, text):
        color.next('开发中...', header=True)

    def pay(self, text):
        color.next('开发中...', header=True)
