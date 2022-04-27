from abc import ABC, abstractmethod
import pygame.image


class Pieces:
    def __init__(self, chess_color, x, y):
        self._chess_color = chess_color
        self._image = pygame.Surface((25, 25))
        self._position = (x, y)

    def get_color(self):
        return self._chess_color

    def set_image(self, image):
        self._image = image

    def get_image(self):
        return self._image

    def get_position(self):
        return self._position


class Pawn(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "Pawn"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":
            return pygame.image.load("assets/pawn_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/pawn_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")


class Knight(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "Knight"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":
            return pygame.image.load("assets/knight_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/knight_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")


class Bishop(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "Bishop"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":
            return pygame.image.load("assets/bishop_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/bishop_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")


class Rook(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "Rook"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":
            return pygame.image.load("assets/rook_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/rook_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")


class Queen(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "Queen"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":

            return pygame.image.load("assets/queen_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/queen_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")


class King(Pieces):
    def __init__(self, chess_color, x, y):
        super().__init__(chess_color, x, y)
        self._type = "King"
        self.set_image(self.piece_image())

    def piece_image(self):
        if self._chess_color == "black":
            return pygame.image.load("assets/king_black.png").convert_alpha()
        else:
            return pygame.image.load("assets/king_white.png").convert_alpha()

    def move(self):
        print(f"I'm a {self.get_color()} {self._type}")
