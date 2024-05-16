from lib.models.snake_game import SnakeGame
from players.cli_player import CLIPlayer
from players.wasd_player import WASDPlayer
from lib.models.displays.cli_display import CLIDisplay
from lib.models.displays.color_display import ColorDisplay
from players.breadth_first_search_player import BreadthFirstSearch
from players.perfect_player import PerfectPlayer


if __name__ == "__main__":
    print("Main program starting")
    snake_player = PerfectPlayer()
    snake_display = ColorDisplay()
    snake_game = SnakeGame(
        snake_player, display=snake_display, size=(8, 8), time_delay=0)

    while not snake_game.died:
        snake_game.step()
