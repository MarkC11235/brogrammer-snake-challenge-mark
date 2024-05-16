import numpy as np
import pygame as pg

from lib.models.snake_player import SnakePlayer
from lib.models.game_action import GameAction
from lib.models.game_state import GameState


class PerfectPlayer(SnakePlayer):

    def __init__(self):
        pg.init()
        self.prev_move = GameAction.UP
        self.cycle_state = 0
        self.inner_cycle = 0
        
    def move_to_top_left(self, state: GameState) -> GameAction:
        if state.head_pos.x > 0:
            return GameAction.LEFT
        elif state.head_pos.y > 0:
            return GameAction.UP
        return None

    def get_action(self, state: GameState) -> GameAction:
        print(state.board)
        print(state.head_pos)
        print(state.size)
        if self.cycle_state == 0:
            move = self.move_to_top_left(state)
            if move is not None:
                return move
            else:
                self.cycle_state = 1
                return GameAction.RIGHT
        elif self.cycle_state == 1:
            if state.head_pos.x < state.board.shape[0] - 1:
                return GameAction.RIGHT
            else:
                self.cycle_state = 2
                return GameAction.DOWN
        elif self.cycle_state == 2:
            if state.head_pos.x > 1:
                return GameAction.LEFT
            else:
                self.cycle_state = 1
                self.inner_cycle += 1
                if self.inner_cycle == state.board.shape[1]/2:
                    self.cycle_state = 0
                    self.inner_cycle = 0
                    return GameAction.LEFT
                return GameAction.DOWN

    def notify_end_of_game(self, game_state: GameState) -> None:
        print("Game over")
        return

    def notify_win(self):
        print("Game beat!")
        return
