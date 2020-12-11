from popo import g
from popo import config as u
from popo import color
from animation import maps


def confirm():
    print()
    text = input(color.confirm('> 按 y 确认, 按其他键跳过: '))

    if str(text).lower() == 'y':
        return True
    else:
        return False


def sendkey(message='请输入:'):
    while True:
        g.clear()
        current()
        print()
        text = input(color.sendkey(message)).strip()
        if text:
            if text.lower() == 'where':
                print()
                current(_map=False)
                color.next('\n按回车继续')
            elif text.lower() == 'status':
                color.info('\n# 角色当前状态如下:\n')
                g.player.show(_map=False)
                color.next('\n按回车继续')
            elif text.lower() == 'help':
                print()
                for msg in u.help:
                    color.info(msg)
                color.next('\n按回车继续')
            elif text.lower() == 'exit':
                y = confirm()
                if y:
                    g.player.exit()
            elif text.lower() == 'author':
                color.caption('\n' + u.author)
                color.next(' ')
            elif text.lower() == 'version':
                color.caption('\n' + u.version)
                color.next(' ')
            elif text.lower() == 'name':
                color.caption('\n' + g.player.data['name'])
                color.next(' ')
            elif text.lower() == 'rename':
                y = confirm()
                if y:
                    print()
                    name = input(color.rename('请输入新的用户名: '))
                    g.player.rename(name)

                color.info('\n当前用户名: ', end=False)
                color.caption(f' {g.player.data["name"]}')
                color.next(' ')
            elif text.lower() == 'delete':
                y = confirm()
                if y:
                    g.player.delete()
                else:
                    print()
            else:
                break
    return text


def current(_map=True):
    if _map:
        color.vmap(maps.home)
    color.label('当前场所: ')
    place_name = g.current_place.name
    # if place_name != '家':
    #     color.vname('家')
    #     color.info('/', end=False)
    color.vname(place_name)

    if g.current_scene:
        color.info(' | ', end=False)
        color.label('当前位置: ')
        color.vname(g.current_scene['name'])
    else:
        color.info('\n\n当前可以进入的位置如下:\n')
        for _id, scene in g.current_place.scenes.items():
            color.index(f'{_id}. {scene["name"]}')
        if place_name != '家':
            color.info('0. 返回上一层')

    if g.current_scene:
        color.info('\n\n当前支持的命令如下:\n')
        for k, v in g.current_scene['actions'].items():
            color.index(f'{k}. {v["name"]}')
        color.info('0. 返回上一层')


def menu():
    print()
    for message in g.help:
        color.info(message)


def show(_map=True):
    if _map:
        color.vmap(maps.home)

    color.div('-'*6 + '当前状态' + '-'*6)

    color.label('等  级: ')
    color.profile(f'{g.player.level}')

    color.label('生命值: ')
    color.profile(f'{g.player.hp} / {g.player.max_hp}')

    color.label('武力值: ')
    color.profile(f'{g.player.battle}')

    color.label('金  币: ')
    color.profile(f'{g.player.coins}')

    color.div('-'*20)
