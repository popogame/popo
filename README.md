# POPO Game

「泡泡世界」是一个文字版的 RPG 游戏框架，目的是为 Python 初学者提供一个简单有趣的实践项目，来编写自己的游戏，开发者只需要数十行代码即可扩展游戏场所、位置和互动操作。


## 快速开始：

1. 下载代码到本地

2. 安装依赖

```shell
pip install -U colored
```

3. 在命令行中启动游戏

```shell
python start.py
```

## 代码架构

```shell
popo                 # 项目文件夹
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
│  │  home.py        # 场所模块：家，家是初始位置，也是顶级位置，请勿修改
│  │  river.py       # 场所模块：河流
│  │  street.py      # 场所模块：街道
│  └─ __init__.py
│  
└─popo               # POPO Game 核心代码文件夹
    │  character.py  # 角色模块：1.提供角色创建、删除、重命名等操作 2. 提供角色的数据接口
    │  color.py      # 颜色模块：把文本输出为美观的颜色，或逐字输出
    │  config.py     # 配置文件，用户自定义的地图模块，需要在此文件中的 maps 列表中配置
    │  g.py          # 全局变量模块
    │  game.py       # 游戏核心框架模块，提供启动，场所切换，位置切换等功能
    │  pprint.py     # 提供 特色的打印函数
    │  views.py      # 提供各种组合数据的美观输出组件
    └─ __init__.py
```

## 开发地图

### 1. 场所构思

在泡泡的世界里，场所是一个小的活动空间，如：街道、河流、学校，每个场所应该有几个场景位置，如街道场所有打工、购物、吃饭等场景。

### 2. 场所模块

场所模块定义在 maps/ 文件夹下，其中 home.py 默认为「家」，不能修改。street.py, river.py 为框架自带，供游戏体验和开发参考。

### 3. 自定义模块

- 在 maps/ 文件夹下创建一个 .py 文件，如: school.py，代码请参考 street.py，如下为简化代码：

```python
fruit = {                                               # fruit: 这是你需要定义的位置信息，如下：
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
                                                        # fruit, noodle 为上面自定义的位置信息，一定要完整正确  

class Fruit():                                          # Fruit 位置的类
...                                                     # 略过，详情见 street.py 文件
...
...


class Noodle():                                         # Noodle 位置的类

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



- 上述自定义场所模块开发完成后，需在 popo/config.py 中配置到 maps 列表中。例如，我们写了一个 school.py 场所模块，则按如下示例添加即可。

```python
# 此处配置 maps/ 文件夹下(除了 home.py 外)的文件名，不配置的则不会导入
maps = ['street', 'river', 'school']

```

- 启动游戏，试试看你写的游戏吧:)

```shell
python start.py
```