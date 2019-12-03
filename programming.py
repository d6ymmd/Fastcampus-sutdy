class War:
    War_part = []
    
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp
        War.War_part.append(self)
        # BOSS = War(name = '보스', atk = 1500, hp = 2000)
        # user_name = input('캐릭터의 이름을 지어주세요!')
        # USER = War(name = user_name, atk = 500, hp = 2000)

    def level_up(self):
        n = int(input('가ㅇ화를 몇 번 하시겠습니까?'))
        while n:
            BOSS.hp += 300
            USER.hp += 1000
            USER.atk += 500 
        print('{}의 공격력은 {}, 체력은 {}입니다').format(user_name, USER.atk, USER.hp)
        print('보스의 공격력은 {}, 체력은 {}입니다.').format(BOSS.atk, BOSS.hp)

    def fight(self):
        while True:
            BOSS.hp -= USER.atk
            USER.hp -= BOSS.hp
            if BOSS.hp < 0 or USER.hp < 0:
                break

        if USER.hp < 0:
            print('보스를 처치 할 수 없습니다.')
        else:
            print('''
            {user_name}가 {}만에 보스를 처치했습니다
            {user_name}의 남은 체력은 {USER.hp}입니다.
            ''')

BOSS = War(name = '보스', atk = 1500, hp = 2000)
user_name = input('캐릭터의 이름을 지어주세요!')
USER = War(name = user_name, atk = 500, hp = 2000)

