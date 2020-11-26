import module
import unittest
from unittest.mock import patch
from random import randint


class TestEvolution(unittest.TestCase):

    def test_next_player(self):
        """ unit test for module.next_player(num: int, players: list)"""
        # type(num) == int
        num_test_cases_not_int = ['1', '', [1], (1,), {1: 1}]
        for test_case in num_test_cases_not_int:
            self.assertRaises(AssertionError, module.functions.next_player, test_case, [1, 2, 3])
        # type(players) == list
        players_test_cases_not_list = ['1', '', (1,), {1: 1}]
        for test_case in players_test_cases_not_list:
            self.assertRaises(AssertionError, module.functions.next_player, 1, test_case)
        # 1 < len(plyesrs) <= 7
        players_test_case = [-1000000000, -1, 0, 1, 8, 1000000000]
        for test_case in players_test_case:
            self.assertRaises(AssertionError, module.functions.next_player, 1, test_case)
        # 0 <= num <= len(players)
        players_test_case = [1, 2, 3]  # relevant
        num_test_cases = [-100000000000, -1, 4, 100000000000]
        for test_case in num_test_cases:
            self.assertRaises(AssertionError, module.functions.next_player, test_case, players_test_case)
        # num = 0
        self.assertEqual(module.functions.next_player(0, [1, 2, 3]), 1)
        # num = len(players) - 1
        self.assertEqual(module.functions.next_player(2, [1, 2, 3]), 0)
        # relevant test
        for i in range(10):
            players = [[1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]]
            num_variants = [randint(0, 1), randint(0, 3), randint(0, 6)]
            result = map(module.functions.next_player, num_variants, players)
            answer_matrix = [(n + 1) % len(p) for n, p in zip(num_variants, players)]
            # print(answer_matrix)
            for a, r in zip(answer_matrix, result):
                self.assertEqual(r, a)
        print('module.next_player(num: int, players: list) - OK')

    def test_take_cards(self):
        """
        unit test for module.take_cards(number: in, card_set: list) function
        """
        # type(num) == int
        num_test_cases_not_int = ['1', '', [1], (1,), {1: 1}]
        for test_case in num_test_cases_not_int:
            self.assertRaises(AssertionError, module.functions.take_cards, test_case, [1, 2, 3])
        # type(cars set) == list
        card_test_cases_not_list = ['1', '', (1,), {1: 1}]
        for test_case in card_test_cases_not_list:
            self.assertRaises(AssertionError, module.functions.take_cards, 1, test_case)
        # number > 0
        num_test_cases = [-100000000000, -1, 0]
        for test_case in num_test_cases:
            self.assertRaises(AssertionError, module.functions.take_cards, test_case, [1, 2, 3])
        # number < len(cars) -> return -1
        for i in range(10):
            cards = [1 * randint(1, 100)]
            num = len(cards) + randint(1, 100)
            self.assertEqual(module.functions.take_cards(num, cards), -1)
        # relevant answer
        for i in range(10):
            cards = [x for x in range(randint(1, 100))]
            start_len_cards = len(cards)
            num = randint(1, len(cards))
            # print(f'num={num}\tlen_cards={len(cards)}')
            result = module.functions.take_cards(num, cards)
            # print(f'new len_cards={len(cards)}')
            self.assertEqual(len(result), num)
            self.assertEqual(type(result), list)
            # print(len(cards))
            self.assertEqual(len(cards), start_len_cards - num)
        print('module.take_cards(number: int, card_set: list)- OK')

    def test_faza_razvitija(self):
        """
        unit test for faza_razvitija(players: list, number: int) function
        """

        players_list = [module.Player('first_player'), module.Player('second_player')]
        cards = [("ostr", "zhir"), ("topo", "zhir"), ("para", "hish"), ("para", "zhir"),
                 ("norn", "zhir"), (["sotr"], "hish"), (["sotr"], "zhir"), ("jado", "hish"),
                 ("komm", "zhir"), ("spac", "hish"), ("mimi",), (["simb"],),
                 ("pada",), ("pira",), ("otbr",), ("bist",), ("vodo",), ("vodo",),
                 (["vzai"], "hish"), ("bols", "zhir"), ("bols", "hish")]
        hands = [("ostr", "zhir"), ("ostr", "zhir")]
        for player in players_list:
            player.get_cards_hand().extend(hands)
        first_number = 0
        razvitie = module.Faza_Razvitija(players_list, first_number)
        """# if all players say pass (len(list_of_pass = len(players))
        razvitie.list_of_pass = players_list[:]
        razvitie.faza_rezvitija_function()
    # if current player in list_say_pass - next player
        razvitie = module.Faza_Razvitija(players_list[:], first_number)
        razvitie.list_of_pass.append(first_number)
        razvitie.faza_rezvitija_function()
    # if player has not cards in his hand - automatic pass
        players_list[0].set_cards_hand([])
        razvitie = module.Faza_Razvitija(players_list, first_number)
        razvitie.faza_rezvitija_function()
    #if active player don't have animals
        razvitie.test = True
        razvitie.faza_rezvitija_function()
        """

    def test_make_property(self):
        """
        unit test for make_property function
        """

        class Player(module.Player):
            def take_handcard(self):
                return 'hish',

        class functions_test(module.functions):

            @staticmethod
            def input_function(alternatives, greeting: str):
                return next(answers_generator)

        def gen_answer():
            # put here answers to question in list
            answers = ['1', 'y']
            for answer in answers:
                yield answer

        answers_generator = gen_answer()

        def clear_players(playerslist):
            playerslist = []

        players_list = [Player(str(x)) for x in range(3)]

        player = players_list[0]
        """# player has one animal
        player.get_player_animals().append(module.Animal())
        self.assertEqual(functions_test.make_property(player, players_list), 1)
        self.assertEqual('property' in player.get_player_animals()[0].get_animal_properties(), True)
        # if property value in animal_properties
        clear_players(players_list)
        players_list = [Player(str(x)) for x in range(3)]
        player = players_list[0]
        player.get_player_animals().append(module.Animal())
        player.get_player_animals()[0].get_animal_properties().append('property')
        self.assertEqual(functions_test.make_property(player, players_list), 0)
        self.assertEqual(('property',) in player.get_cards_hand(), True)
        
        # if property value == hish and pada in animal properties
        clear_players(players_list)
        players_list = [Player(str(x)) for x in range(3)]
        player = players_list[0]
        player.get_player_animals().append(module.Animal())
        player.get_player_animals()[0].get_animal_properties().append('hish')
        self.assertEqual(functions_test.make_property(player, players_list), 0)
        self.assertEqual(('pada',) in player.get_cards_hand(), True)
        """
        # if property value == pada and hish in animal properties
        clear_players(players_list)
        players_list = [Player(str(x)) for x in range(3)]
        player = players_list[0]
        player.get_player_animals().append(module.Animal())
        player.get_player_animals()[0].get_animal_properties().append('pada')
        self.assertEqual(functions_test.make_property(player, players_list), 0)
        self.assertEqual(('hish',) in player.get_cards_hand(), True)
        # todo похоже надо писать отдельнцю функцию дял каждой проверки - а то они мешают друг другу

    def test_init_Eating_Phase(self):
        """
        unit test for Eating_Phase constructor
        """
        # player not a list (int instead)
        self.assertRaises(AssertionError, module.Eating_Phase, players=1, first_number_player=0,
                          eating_base=5)
        # len of players < 1
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player()], first_number_player=0,
                          eating_base=5)
        # len of players > 8
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player() for x in range(9)],
                          first_number_player=0, eating_base=5)
        # not all players instances of Player() class
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player(), 1], first_number_player=0,
                          eating_base=5)
        # first number is no int type
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player='1', eating_base=5)
        # first number < 0
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player=-1, eating_base=5)
        # first number == 0
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player=0, eating_base=5)
        # first number > len(players)
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player=3, eating_base=5)
        # eating base not int type
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player=1, eating_base='5')
        # eating base < 0
        self.assertRaises(AssertionError, module.Eating_Phase, players=[module.Player, module.Player()],
                          first_number_player=1, eating_base=-1)

    def test_get_grazing_count(self):
        """
        unit test for Player.get_grazing_count()
        """

        rand_animals = [module.Animal() for x in range(randint(1, 10))]
        for item in rand_animals:
            item.grazing = True
        # if player.get_grazing_count == len(animals)
        player = module.Player()
        player.animals = rand_animals
        self.assertEqual(player.get_grazing_count(), len(rand_animals))
        # if no animals with grazing property
        rand_animals = [module.Animal()]
        player.animals = rand_animals
        self.assertEqual(player.get_grazing_count(), 0)
        # if player has not animals at all
        player.animals = []
        self.assertEqual(player.get_grazing_count(), 0)

    def test_grazing_function(self):
        """
        unit test for grazing function
        """

        # define user input function
        def test_input1(*args):
            return '6'

        def test_input2(*args):
            return '2'

        players = [module.Player() for x in range(5)]
        # add grazing animlas to Player[0]
        grazing_animal = module.Animal()
        grazing_animal.grazing = True
        for i in range(5):
            players[0].animals.append(grazing_animal)
        # instance of eating Phase class
        eating_phase = module.Eating_Phase(players=players, first_number_player=0, eating_base=5)
        # eating base < 0
        eating_phase.eating_base = 0
        self.assertRaises(AssertionError, eating_phase.grazing_function, players[0])
        # player has not grazing animals
        eating_phase.eating_base = 5
        self.assertRaises(AssertionError, eating_phase.grazing_function, players[1])
        # destroy  elements > of eating base
        eating_phase.eating_base = 5
        self.assertRaises(AssertionError, eating_phase.grazing_function, players[0],
                          test_input1)
        # destroy 2 elements of red fish
        eating_phase.eating_base = 5
        eating_phase.grazing_function(players[0], test_input2)
        self.assertEqual(eating_phase.eating_base, 3)

    def test_take_red_fish(self):
        """
        unit test for module.eating_phase.take_red_fish function
        """
        # emulation user input
        def fun(*args):
            answers = ['1', '2', '1', '1', '2', '1', '1', '1', '1', '1']
            for item in answers:
                yield item

        f = fun()

        def user_input(*ars):
            return next(f)

        def standard_values(player):
            """
            set player's animals property to default values
            """
            for animal in player.animals:
                animal.hungry = 1
                animal.fat = 0
                animal.fat_cards_count = 0
                animal.simbiosys = []
                animal.communication = []
                animal.cooperation = []

        players = [module.Player() for x in range(5)]
        eating_phase = module.Eating_Phase(players, first_number_player=0, eating_base=5)
        # adding animals to player
        for i in range(3):
            players[0].animals.append(module.Animal())
        players[0].animals[0].hungry = 0
        # if animal is not hungry and has no free fat (look at text this animal is not hungry and is enough fat!
        # Choose another animal!) next animal is hungry
        eating_phase.eating_base = 5
        eating_phase.take_red_fish(players[0], user_input) # answers [0], [1]
        self.assertEqual(players[0].animals[1].hungry, 0)
        self.assertEqual(players[0].animals[1].fat, 0)
        self.assertEqual(eating_phase.eating_base, 4)
        # return standard values
        standard_values(players[0])
        # if animal is not hungry but has free fat
        eating_phase.eating_base = 5
        players[0].animals[0].hungry = 0
        players[0].animals[0].fat_cards_count = 1
        eating_phase.take_red_fish(players[0], user_input) # answers[2]
        self.assertEqual(eating_phase.eating_base, 4)
        self.assertEqual(players[0].animals[0].fat, 1)
        # return standards values
        standard_values(players[0])
        # if animal has hungry simbiont - it can't eat
        eating_phase.eating_base = 5
        # add symbiosis
        players[0].animals[0].add_symbiosys(players[0].animals[1])
        # symbiosys is hungry
        # look at text 'one of its symbionts is hungry: {symbiont} - this animal cant eat'
        eating_phase.take_red_fish(players[0], user_input) # answers [3], [4]
        self.assertEqual(eating_phase.eating_base, 4)
        # now symbiont is not hungry
        players[0].animals[1].hungry = 0
        eating_phase.take_red_fish(players[0], user_input) # answers [5]
        self.assertEqual(eating_phase.eating_base, 3)
        self.assertEqual(players[0].animals[0].hungry, 0)
        # set default values
        standard_values(players[0])
        eating_phase.eating_base = 5
        # todo if eating base is not empty and if all animals are symbiosys each to other (say pass before take red fish function)
        # if animal has communication
        # make communication property 0-1
        players[0].animals[0].add_communication(players[0].animals[1])
        players[0].animals[1].add_communication(players[0].animals[0])
        # 1. if communicator is hungry and there are enough red fish
        eating_phase.take_red_fish(players[0], user_input) # answers [6]
        self.assertEqual(eating_phase.eating_base, 3)
        self.assertEqual(players[0].animals[0].hungry, 0)
        self.assertEqual(players[0].animals[1].hungry, 0)
        self.assertEqual(players[0].animals[0].fat, 0)
        self.assertEqual(players[0].animals[1].fat, 0)
        # 2. if communicaotor is not hungry, but is  enough fat and there are enough red fish
        standard_values(players[0])
        eating_phase.eating_base = 5
        # make communication property 0-1
        players[0].animals[0].add_communication(players[0].animals[1])
        players[0].animals[1].add_communication(players[0].animals[0])
        players[0].animals[1].hungry = 0
        players[0].animals[1].fat_cards_count = 1
        eating_phase.take_red_fish(players[0], user_input)  # answers [7]
        self.assertEqual(eating_phase.eating_base, 3)
        self.assertEqual(players[0].animals[0].hungry, 0)
        self.assertEqual(players[0].animals[1].hungry, 0)
        self.assertEqual(players[0].animals[0].fat, 0)
        self.assertEqual(players[0].animals[1].fat, 1)
        # 3. if communicator is hungry but there are not enpugh red fish
        standard_values(players[0])
        eating_phase.eating_base = 1
        # make communication property 0-1
        players[0].animals[0].add_communication(players[0].animals[1])
        players[0].animals[1].add_communication(players[0].animals[0])
        eating_phase.take_red_fish(players[0], user_input)  # answers [8]
        self.assertEqual(eating_phase.eating_base, 0)
        self.assertEqual(players[0].animals[0].hungry, 0)
        self.assertEqual(players[0].animals[1].hungry, 1)
        self.assertEqual(players[0].animals[0].fat, 0)
        self.assertEqual(players[0].animals[1].fat, 0)
        # 4. if communicator is not hungry but has extra fat card - but not enough red fish
        standard_values(players[0])
        eating_phase.eating_base = 1
        # make communication property 0-1
        players[0].animals[0].add_communication(players[0].animals[1])
        players[0].animals[1].add_communication(players[0].animals[0])
        players[0].animals[1].hungry = 0
        players[0].animals[1].fat_cards_count = 1
        eating_phase.take_red_fish(players[0], user_input)  # answers [9]
        self.assertEqual(eating_phase.eating_base, 0)
        self.assertEqual(players[0].animals[0].hungry, 0)
        self.assertEqual(players[0].animals[1].hungry, 0)
        self.assertEqual(players[0].animals[0].fat, 0)
        self.assertEqual(players[0].animals[1].fat, 0)
        # todo make cooperation property test 26 11 2020
if __name__ == '__main__':
    unittest.main()
