import random
import time
from monster import wooden_sword, slime, gobline


def fight( sword, monster ):
    while monster.monster_hp > 0:
        print('Что вы хотиде сделать')
        time.sleep(0.5)
        print("(вы можете 'ударить' ,'защититься' ")
        def_or_atk = input()
        monster.attack()
        if 'ударить' == def_or_atk:
            if sword == '1 - 4':
                monster.monster_hp = monster.monster_hp - (random.randint(1, 4 )+ player.exp)
                print('Вы оставили монстру',monster.monster_hp,'хп')
                if monster.monster_hp <= 0 :
                    break
        ataca = random.randint(1, 3)
        if ataca <= 2 :
            if def_or_atk == 'защититься':
                monster.def_attack()
                print('Монстер атакует но вы блокируете большую часть его атаки и он оставляет вам', player.hp, 'хп')
            else:
                monster.attack()
                print('Монстер атакует и оставляет вам', player.hp, 'хп')
        else:
            monster.super_attack()
            print('Вы видете что монстр заряжает удар')

    player.exp += 1
    player.hp += 5
    return monster , player.hp, player.exp


while True:
    print('Вы хотите начать?')
    print('(да или нет)')
    start = input()
    if start == 'да':
        print('Вы начинающий путешественник который решил искоренить зло которое досаждает деревне много лет')
        time.sleep(0.6)
        print('Вы уже идёте в подземелье ,и тут вспоминаете, что не купили мечь ! Теперь вы идёте в кузнечную ')
        time.sleep(0.6)
        print('На последние деньги вы покупаете оловянный меч. и наконец идёте в подземелье')
        time.sleep(0.6)
        print('Вы открываете ворота и заходите в подземелье.')
        time.sleep(0.6)
        print('Вы на первом этаже этого подземелья')
        time.sleep(0.6)
        print('Вы видете обычного слизня .Вы вступаете с ним в бой')
        fight( wooden_sword, slime)

        if player.hp <= 0:
            break
        print('Вы подняли 1 уровень и исццелии 5хп')
        print(player.hp)
        time.sleep(0.6)
        print('Дверь впереди открываеться вас, вы входите в неё')
        time.sleep(0.6)
        print('Войдя в новою комнату вы видете одиноко стоящего гоблина.')
        time.sleep(0.6)
        print('вы вступаете с ним в бой')
        fight(wooden_sword, gobline)

    elif start == 'нет':
        break
    else:
        print('мы вас не поняли скажите')


