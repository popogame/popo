from random import randint, sample
from popo import g
from popo import color # color 模块提供彩色打印、逐字打印等效果


fruit = {                                               # fruit: 这是你需要定义的位置变量名
    'name': '泡泡水果店',                                # name: 位置名称
    'class': 'Fruit',                                   # class: 位置的类名称，本例为 Fruit，后面需真实定义 class Fruit
    'desc': '可以打零工赚钱的地方',                       # desc: 可写可不写，此位置的补充描述
    'actions': {'1': {'name': '收银',                    # actions: 本位置中支持的互动操作集合，'1', '2' 为命令编号，必须是字符类型
                      'func': 'cash', 
                      'desc': '打个零工赚点小钱吧'},      # desc: 可写可不写，此交互操作的补充描述

                '2': {'name': '领工钱', 'func': 'wage'}  #  name: 互动操作名称 
                }                                        #  func: 互动操作的函数名称，该函数应写在本位置类中 \
}                                                        # 本例中 cash 和 wage 函数都应该写在Fruit类中

noodle = {
    'name': '重庆小面馆',
    'class': 'Noodle',
    'actions': {'1': {'name': '点单', 'func': 'order'},
                '2': {'name': '开吃', 'func': 'dine'},
                '3': {'name': '买单', 'func': 'pay'}
                }
}


class App():                                            # 框架约定的场所类名称，统一为 App，不可修改

    def __init__(self, _id, module):                    # 框架约定，不可修改
        self.id = _id                                   # 框架约定，不可修改
        self.module = module                            # 框架约定，不可修改

        self.name = '泡泡大街'                          # name: 定义场所名称
        self.level = 1                                  # level: 定义角色能够进入此场所的最低等级(待实现)
        self.scenes = {'1': fruit, '2': noodle}         # scenes: 定义本场所包含的位置集合，'1', '2' 为地点编号，必须是字符类型 \
                                                        # fruit, noodle 为上面自定义的位置信息，一定要完整正确 
        self.desc = '商业大街，请尽情探索吧'              # 可写可不写，此场所的补偿描述

prices = {'橘子': 3, '葡萄': 12, '毛桃': 9, '香蕉': 6, '苹果': 7, '榴莲': 48}


class Fruit():

    def __init__(self):
        self.paid = 0  # 定义玩家赚的工钱
        self.fine = 0  # 定义玩家被扣罚的工钱

    def cash(self, text):

        cart = sample(prices.keys(), randint(1, 4))  # 在购物车中随机生成1~4种要购买的水果
        weight = {}  # 水果重量表
        total = 0    # 预期总价格
        # color.info 打印提示性信息，浅灰色字体
        color.info('\n有一位顾客的购物清单如下:\n')
        color.info('-----------------------') 
        for fruit in cart:
            weight[fruit] = randint(1, 9)  # 为购物车中的水果称重（此处为 1~9 随机赋值）
            total += prices[fruit] * weight[fruit]  # 计算预期总价格
            # color.option 打印重点内容或用户选项，以 0.1 秒间隔逐字打印，蓝色字体            
            color.option(f'{fruit:>4}  {prices[fruit]:>2} * {weight[fruit]}')  # 打印购物清单给用户查看
        color.info('-----------------------')
        # color._input 彩色字体提示用户输入信息
        text = color._input('总价格:')  # 提示用户计算出总价格
        if text == str(total):  # 用户输入和预期总价格比较，注意：用户输入都是字符串，需把 total 转化为 str
            self.paid += 10     # 用户计算正确，佣金 +10
            # color.talk 打印对话，以 0.1 秒间隔逐字打印，粉色字体
            color.talk('收银正确，请继续加油吧~')  # 打印恭喜对话，
        else:  # 如果用户输入的计算结果有误
            self.fine += 10  # 罚款记录项 +10
            g.player.coins_plus(-10)  # 实际扣除操作，用户金币 -10
            color.talk('啊哦，收银错误，倒扣 10 金币！')  # 打印失败对话
            color.talk(f'你现在总金币为: {g.player.coins} 金币。')

    def wage(self, text):

        balance = self.paid - self.fine  # 结余
        paid = self.paid  # 临时保持工钱变量
        fine = self.fine  # 临时保持罚金变量

        if self.paid > 0:
            g.player.coins_plus(self.paid)  # 支付工钱，即玩家金币 + paid

        self.paid = 0  # 清空玩家待结算工钱
        self.fine = 0  # 清空玩家结算钱被扣的工钱

        if fine > 0:
            color.talk(f'钱都收错了，真是不用心啊，你被罚了 {fine} 金币！')
            if paid > 0:
                color.talk(f'不过好在你也算对了 {paid // 10} 次，赚了 {paid} 金币！')
                if balance == 0:
                    color.talk(f'罚金与工钱正好抵消，你今天白干了，小兄die~')
                elif balance > 0:
                    color.talk(f'扣去罚金，你今天赚了 {balance} 金币！')
                else:
                    color.talk(f'真是白痴啊，金币没赚到，还被扣去 {balance} 金币！')
        else:
            if paid == 0:
                color.talk('你今天偷懒了吧，都没来上班，还想要工钱？')
            else:
                color.talk(f'恭喜你，今天赚了 {balance} 金币!')

    
        color.talk(f'你现在总金币为: {g.player.coins} 金币！')


class Noodle():                                         # 定义位置类: Noodle

    def __init__(self):                                      
        pass

    def order(self, text):                              # 在位置信息中定义的 order 互动操作函数，必须在此位置类中定义
        color.next('开发中...', header=True)

    def dine(self, text):
        color.next('开发中...', header=True)            # 在位置信息中定义的 dine 互动操作函数，必须在此位置类中定义

    def pay(self, text):
        color.next('开发中...', header=True)            # 在位置信息中定义的 pay 互动操作函数，必须在此位置类中定义
