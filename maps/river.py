from popo import g
from popo import color



lane = {
    'name': '滨河跑道',
    'class': 'Lane',
    'actions': {'1': {'name': '慢跑', 'func': 'walk'},
                '2': {'name': '休息', 'func': 'rest'}
                }
}


bay = {
    'name': '钓鱼小湾',
    'class': 'Bay',
    'actions':  {'1': {'name': '投食', 'func': 'feed'},
                 '2': {'name': '下钩', 'func': 'fishing'},
                 '3': {'name': '收工', 'func': 'ending'}
                 }
}


class App():

    def __init__(self, _id, module):
        self.id = _id
        self.module = module

        self.name = '富春河畔'
        self.level = 5
        self.scenes = {'1': lane, '2': bay}


class Lane():

    def __init__(self):
        pass

    def walk(self, text):
        color.next('开发中...', header=True)

    def rest(self, text):
        color.next('开发中...', header=True)


class Bay():

    def __init__(self):
        pass

    def feed(self, text):
        color.next('开发中...', header=True)

    def fishing(self, text):
        color.next('开发中...', header=True)

    def ending(self, text):
        color.next('开发中...', header=True)
