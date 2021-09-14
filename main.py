from Game import Game  # import from class Game

game = Game()  # create game object
i = 0  # counter
game.num_line()  # calculating number of lines in the input file

while game.harry.get_health() > 0 and game.voldemort.get_health() > 0 and i < game.line_count:
    game.read_input(i)  # reading the input from file
    game.harry.cast_spell(game.read_power(game.harry.get_spell()))  # harry turn to cast spell
    game.voldemort.cast_spell(game.read_power(game.voldemort.get_spell()))  # Voldemort  turn to cast spell
    game.harry.receive_spell(game.read_power(game.harry.get_spell()), game.read_power(game.voldemort.get_spell()),
                             game.harry.get_spell())
    game.voldemort.receive_spell(game.read_power(game.voldemort.get_spell()), game.read_power(game.harry.get_spell()),
                                 game.voldemort.get_spell())
    game.print_result()         # printing the health and energy of each wizard
    i += 1                      # incrementing to the next line of input in the fiel
game.declare_winner()           # declaring the winner
