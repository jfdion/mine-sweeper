from minesweeper.game import Game

game = Game()

while True:
    if not game.running():
        game.start()
    game.update()



