class Pokemon:
    POKEMON_LIST = []

    def __init__(self, name, type):
        self.friends = []
        self.name = name
        self.type = type
        self.__level = 1
        Pokemon.POKEMON_LIST.append(self)
    
    @property
    def level(self):
        print (self.__level)

    def level_up(self):
        self.__level x1
    
    def add_friend(self, pokemon):
        # self.pokemon = []
        self.friends.append(pokemon)

    def show_friends(self):
        if len(self.friends) == 0:
            print(f'{self.name}에게는 친구가 없습니다...')
        else:
            result = '{}의 친구들: {} (총 {}마리)'.format(self.name,
                ', '.join([pokemon.name for pokemon in self.friends]),
                len(self.friends)
            )
            print(result)

        # for문, list comprehension + (f-string or str.fomat) 세가지 사용해보기
        # else:
        #     result = '{}의 친구들: {} (총 {}마리)'.format(self.name,
        #         self.friends,
        #         print(len(self.friends)),
        #     )
        #     print(result)


    # def show_friends(self):
    #     if len(self.friends) == 0:
    #         print(f'{self.name}에게는 친구가 없습니다...')
    #     else:
    #         result = f'{self.name}의 친구들: {', '.join([pokemon.name for pokemon in self.friends])}'
    #         print(result)

    # 표현식으로 바꿔서 해보기
    # 할당을 할거면 안에 할당
    # @classmethod
    # def show_total_okemon(cls):
    #     if len(cls.POKEMON_LIST) > 0:
    #         print(f'전체 포켓몬: {POKEMON_LIST}(총 {len(cls.POKEMON_LIST)})')
    #     else:
    #         print('포켓몬이 없습니다...')

    @classmethod
    def show_total_pokemon(cls):
        if len(cls.POKEMON_LIST) == 0:
            print('포켓몬이 없습니다...')
        else:
            result = '전체 포켓몬: {pokemon_list} (총 {pokemon_count}마리)'.format(
                pokemon_list = ', '.join([Pokemon.name for Pokemon in cls.POKEMON_LIST]),
                pokemon_count = len(cls.POKEMON_LIST),  ## 두 번 계산함. 위에 정의해줘도 됨(if문 위에). 
            )
            print(result)
        

Pokemon.show_total_pokemon()

pikachu = Pokemon(name='피카츄', type='전기')
pikachu.level

pikachu.level_up()
pikachu.level

butterfree = Pokemon(name='버터플', type='벌레')
starmie = Pokemon(name='아쿠스타', type='물')
eevee = Pokemon(name='이브이', type='노멀')
pikachu.show_friends()


pikachu.add_friend(butterfree)   ##제대로 했다면 pikachu.add_friend(3) 이런식으로도 동작해야함 
pikachu.add_friend(starmie)
pikachu.show_friends()

Pokemon.show_total_pokemon()
