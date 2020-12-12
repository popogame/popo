# POPO Game <sub>coding is game</sub>

「泡泡世界」是一个文字版的 RPG 游戏框架，目的是为 Python 初学者提供一个简单有趣的实践项目，轻松开发出属于自己的游戏，开发者只需要数十行代码即可扩展游戏场所、位置和互动操作。


## 系统及软件需求

- 本项目为纯 Python 项目，支持 Windows/MacOS/Linux 等系统
- python 3.7+


## 快速开始：

1. 下载代码到本地，如果是解压包，请解压

2. 安装依赖

```shell
pip install -U colored
```

3. 为了更好的体验游戏，Windows 系统下命令行终端建议使用 Hyper

    - 请自行下载安装：[官网下载](https://hyper.is/)

    - 把 Hyper 添加到右键菜单

        在你的电脑上打开 Hyper，依次点击左上角 `菜单按钮` -> `plugins` -> `install Hyper CLI command in PATH`
        然后，在任意文件夹下，右键，可以发现有一个选项:`Open Hyper here`，点击即可在当前目录打开 Hyper

    - Hyper 还支持一些插件和主题，感兴趣的可自己选择安装。[Hyper 主题](https://hyper.is/themes)

4. 在命令行终端中启动游戏

    - 进入已下载的项目文件夹 `popo`（如果是下载的压缩包，解压后可能是文件夹 `pop-main`）下，右键点击 `Open Hyper here`
       
        > 或者在打开的 CMD 终端上，切换到已下载的项目文件夹

    - 执行如下命令：

        ```shell
        python start.py
        ```

## 代码架构

```shell
popo                 # 项目文件夹，如果是下载的压缩包，解压后可能是文件夹 `pop-main`
│
│  README.md         # 说明文档
│  start.py          # 启动脚本: python start.py
│
├─animation          # 字符画地图，过场字符动画
│  │  maps.py        # 地图字符画定义文件
│  │  __init__.py    
│
├─data               # 游戏数据文件夹，请勿修改
│      data.json     # 实际使用的数据文件
│      default.json  # 初始配置，当重建角色时使用
│
├─maps               # 地图模块，开发者实际在这个目录编写游戏逻辑代码
│  │  home.py        # 场所模块：家。自带模块，家是初始场所，也是顶级位置，不能修改
│  │  river.py       # 场所模块：河流。自带模块，可继续二次开发
│  │  street.py      # 场所模块：街道。自带模块，可继续二次开发
│  └─ __init__.py
│  
└─popo               # POPO Game 核心代码文件夹
    │  character.py  # 角色模块：1.提供角色创建、删除、重命名等操作 2. 提供角色的数据接口
    │  color.py      # 颜色模块：把文本配置为美观的颜色打印，或逐字打印
    │  config.py     # 配置文件，用户自定义的地图模块，需要在此文件中的 maps 列表中配置
    │  g.py          # 全局变量模块
    │  game.py       # 游戏核心框架模块，提供启动，场所切换，位置切换等功能
    │  pprint.py     # 提供特色的打印函数
    │  views.py      # 提供各种组合数据的美观输出组件
    └─ __init__.py
```

## 开发地图

### 1. 场所构思

在泡泡的世界里，场所是一个小的活动空间，如：街道、河流、学校，每个场所应该有几个位置能够发生故事场景，如街道场所有水果店、面馆等位置（故事场景）。

### 2. 场所模块

场所模块定义在 maps/ 文件夹下，其中 home.py 默认为「家」，不能修改。street.py, river.py 为框架自带，供游戏体验、开发参考或二次开发。

### 3. 开发场所模块

- 在 maps/ 文件夹下创建一个 .py 文件，如: school.py，代码请参考 street.py，如下为简化代码及说明：

```python
fruit = {                                               # fruit: 这是你需要定义的位置变量名
    'name': '泡泡水果店',                                # name: 位置名称
    'class': 'Fruit',                                   # class: 位置的类名称，本例为 Fruit，后面需真实定义 class Fruit
    'actions': {'1': {'name': '收银', 'func': 'cash'},  # actions: 本位置中支持的互动操作集合，'1', '2' 为命令编号，必须是字符类型
                '2': {'name': '领工钱', 'func': 'wage'} #  │   name: 互动操作名称 
                }                                       #  └─  func: 互动操作的函数名称，该函数应写在本位置类中 \
}                                                       # 本例中 cash 和 wage 函数都应该写在Fruit类中

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
                                                        # fruit, noodle 为上面自定义的位置信息变量名

class Fruit():                                          # 定义位置类: Fruit
...                                                     # 略过，详情见 street.py 文件
...
...


class Noodle():                                         # 定义位置类: Noodle

    def __init__(self):                                      
        pass

    def order(self, text):                              # 在位置信息中定义的 order 互动操作函数，必须在此位置类中定义
        color.next('开发中...', header=True)

    def dine(self, text):
        color.next('开发中...', header=True)            # 在位置信息中定义的 dine 互动操作函数，必须在此位置类中定义

    def pay(self, text):
        color.next('开发中...', header=True)            # 在位置信息中定义的 pay 互动操作函数，必须在此位置类中定义

```

- 编写自定义的互动操作

请参考 street.py 中 Fruit 的互动操作 cash, wage 的实现

```python
class Fruit():

    def __init__(self):
        self.paid = 0  # 定义玩家赚的金币数
        self.fine = 0  # 定义玩家被扣罚的金币数

    def cash(self, text):

        cart = sample(prices.keys(), randint(1, 4))  # 在购物车中随机生成1~4种要购买的水果
        weight = {}  # 水果重量表
        total = 0    # 预期总价格
        # color.info 打印提示性信息，浅灰色字体
        color.info('\n有一位顾客的购物清单如下:\n') 
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
            g.player.coins = -10  # 实际扣除操作，用户金币 -10
            color.talk('啊哦，收银错误，倒扣10块！')  # 打印失败对话

    def wage(self, text):

        if self.fine > 0:
            color.talk(f'钱都收错了，真是不用心啊，你被罚了 { self.fine} 元')
            if self.paid > 0:
                color.talk(f'不过好在你也算对了几次，赚了 {self.paid} 元')
        elif self.paid == 0:
            color.talk('你今天偷懒了吧，都没来上班，还想要工钱？')
        else:
            g.player.coins = self.paid  # coins 为 setter 属性赋值，会自动为 coins 加上 paid，相当于 coins += paid
            color.talk(f'恭喜你，今天赚了 {self.paid - self.fine} 元!')
            color.talk(f'你现在总金币为: {g.player.coins} 元。')
```

- 上述自定义场所模块开发完成后，需在 popo/config.py 中配置到 maps 列表中。例如，我们写了一个 school.py 场所模块，则按如下示例添加即可。

```python
# 此处配置 maps/ 文件夹下(除了 home.py 外)的文件名，不配置的则不会导入
maps = ['street', 'river', 'school']

```

- 启动游戏，试试看你写的游戏吧:)

```shell
python start.py
```