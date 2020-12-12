import signal
from importlib import import_module
from popo.character import Character
from popo import g
from popo import color
from popo import config as u
from popo import views as v


def loading():

    # 导入地图/位置
    u.maps = ['home'] + u.maps
    home_scenes = {}
    for (i, mod) in enumerate(u.maps):
        module = import_module('maps.' + mod)
        # 初始化场所模块，值为 App 类的实例
        g.maps[mod] = getattr(module, 'App')(str(i), mod)
        g.scenes[mod] = {}
        
        if i > 0:
            if hasattr(g.maps[mod], 'desc'):
                home_scenes[str(i)] = {'name': g.maps[mod].name, 'desc': g.maps[mod].desc}
            else:
                home_scenes[str(i)] = {'name': g.maps[mod].name}
    g.maps['home'].scenes = home_scenes


def switch_place():

    text = g.current_cmd
    if text is None:
        text = v.sendkey('场所编号:')

    flag = False
    if text != '0':
        for place in g.maps.values():
            if place.id == text:
                g.current_place = place
                flag = True
        if not flag:
            color.error('--- 没有此场所编号 ---', end=False)
            color.next()
    else:
        color.info('~ 你已经在家里了 ~')

    g.current_cmd = None


def switch_scene():

    text = g.current_cmd
    if text is None:
        text = v.sendkey('位置编号:')

    if text == '0':
        g.current_place = g.maps['home']
    else:
        scenes = g.current_place.scenes
        if text in scenes:
            g.current_scene = scenes[text]
            g.current_scene['id'] = text
            g.current_cmd = None
        else:
            color.error('--- 当前场所下没有此位置编号 ---', end=False)
            color.next()
            g.current_cmd = None


def start():

    g.player.show(_map=False)
    color.next('\n按回车键继续')
    g.current_place = g.maps['home']

    while True:
        # '0': 退出当前位置(scene)或场所(place)
        if g.current_cmd == '0':
            # 当前位置(scene)存在，则只退出当前位置，保留当前场所(place)
            if g.current_scene:
                g.current_scene = None
                g.current_cmd = v.sendkey('位置编号:')
            # 当前位置(scene)不存在，，则回家，提示输入场所编号
            else:
                g.current_place = g.maps['home']
                g.current_cmd = None

        # 如果是家，则提示输入场所编号
        elif g.current_place.name == '家':
            switch_place()

        # 如果位置为空，则提示输入位置编号
        elif g.current_scene is None:
            switch_scene()
        # 有场所和位置
        else:
            # 当面交互命令为空，则提示输入交互命令
            if g.current_cmd is None:
                if g.no_this_cmd:
                    g.no_this_cmd = False
                    color.error('--- 当前位置下没有此命令编号 ---', end=False)
                    color.next()
                g.current_cmd = v.sendkey('命令编号:')
            # 有交互命令，执行交互命令
            else:
                if g.current_cmd in g.current_scene['actions']:
                    if g.current_scene['id'] not in g.scenes[g.current_place.module]:
                        module = import_module('maps.' + g.current_place.module)
                        # 初始化位置类，值为 current_scene['class'] 类的实例
                        g.scenes[g.current_place.module][g.current_scene['id']] = getattr(
                            module, g.current_scene['class'])()

                    scene = g.scenes[g.current_place.module][g.current_scene['id']]
                    func = g.current_scene['actions'][g.current_cmd]['func']
                    getattr(scene, func)(g.current_cmd)
                else:
                    g.no_this_cmd = True

                g.current_cmd = None


def signal_handler(signal, frame):

    if g.player:
        g.player.exit()
    else:
        exit(-1)


def app():

    g.clear()

    signal.signal(signal.SIGINT, signal_handler)

    color.tilte(f'~~ 欢迎来到{u.name} ~~', header=False, time=0.1)

    # 读取角色
    loading()
    g.player = Character()
    start()
