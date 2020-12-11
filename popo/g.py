import os 
player = ''

maps = {}
scenes = {}

current_area = None
current_scene = None
current_cmd = None
no_this_cmd = False


def clear():
    os.system("cls")