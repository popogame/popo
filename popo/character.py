import os
import json
from time import sleep
from popo import color
from popo import g
from popo import views as v


class Character:

    def __init__(self):

        with open('data/data.json', 'r', encoding='utf8')as f:
            self.data = json.load(f)

            # 初始化角色: 读取角色属性，如果无名称，则提示用户输入名字
            name = self.data['name']
            if not name:
                name = color._input(' 一个角色名字:')
                self.data['name'] = name
                self.save()
                color.info('# 创建人物成功')

            # 已有名字，直接进入角色
            else:
                color.info('\n# 角色加载成功')

    @property
    def coins(self):
        return self.data['coins']["balance"]

    @coins.setter
    def coins(self, value):
        if isinstance(value, int):
            self.data['coins']["balance"] += value
            self.save()

    @property
    def level(self):
        return self.data["status"]["level"]

    @level.setter
    def level(self, value):
        if isinstance(value, int):
            self.data["status"]["level"] += value
            self.save()

    @property
    def hp(self):
        return self.data["status"]["hp"]

    @hp.setter
    def hp(self, value):
        if isinstance(value, int):
            self.data["status"]["hp"] += value
            self.save()

    @property
    def max_hp(self):
        return self.data["status"]["max_hp"]

    @max_hp.setter
    def max_hp(self, value):
        if isinstance(value, int):
            self.data["status"]["max_hp"] += value
            self.save()

    @property
    def battle(self):
        return self.data["status"]["battle"]

    @battle.setter
    def battle(self, value):
        if isinstance(value, int):
            self.data["status"]["battle"] += value
            self.save()

    def show(self, _map=True):

        v.show(_map)

    def save(self):

        with open('data/data.json', 'w', encoding='utf8')as f:
            json.dump(self.data, f)

    def exit(self):
        g.clear()
        self.show(_map=False)

        color.tilte('~~ 即将退出游戏，欢迎下次光临 ~~', time=0.1)
        exit(0)

    def rename(self, name):

        if name.strip():
            self.data['name'] = name
            self.save()
        else:
            color.error('--- 用户名无效 ---')

    def delete(self):

        with open('data/default.json', 'r', encoding='utf8')as f:
            self.data = json.load(f)
            self.save()

            os.system("cls")
            color.error('--- 当前角色已删除 ---\n')
            color.info('--- 游戏即将退出，请重启动游戏 ---')
            exit(0)
