import itertools
import pygame as pg
import pieces


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = (254, 243, 206)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class ChessGame:
    def __init__(self):
        pg.init()
        self.display_width = 608
        self.display_height = 608
        self.piece_selected = False
        self.gameDisplay = pg.display.set_mode((self.display_width, 820))
        self.image_size = 50
        self.tile_size = 76
        self.brown = (149, 69, 53)
        self.beige = (254, 243, 206)
        self.moving = False
        self.play_again = Button('red', 200, 760, 200, 60, 'Play Again')
        self.white_eat, self.black_eat = 0, 0
        self.pieces = []

        self.pieces.append(pieces.Queen("black", 1, ((self.display_width / 8) * 3 + (self.tile_size - self.image_size) / 2),
            (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Queen("white", 2, ((self.display_width / 8) * 3 + (self.tile_size - self.image_size) / 2),
            ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.King("black", 3, ((self.display_width / 8) * 4 + (self.tile_size - self.image_size) / 2),
            (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.King("white", 4, ((self.display_width / 8) * 4 + (self.tile_size - self.image_size) / 2),
            ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Rook("black", 5, ((self.tile_size - self.image_size) / 2),
            (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Rook("white", 6, ((self.tile_size - self.image_size) / 2),
            ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Rook("black", 7, ((self.display_width / 8) * 7 + (
            self.tile_size - self.image_size) / 2), (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Rook("white", 8, ((self.display_width / 8) * 7 + (
            self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Knight("black", 9, ((self.display_width / 8) + (
            self.tile_size - self.image_size) / 2), (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Knight("white", 10, ((self.display_width / 8) + (
            self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Knight("black", 11, ((self.display_width / 8) * 6 + (
            self.tile_size - self.image_size) / 2), (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Knight("white", 12, ((self.display_width / 8) * 6 + (
            self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Bishop("black", 13, ((self.display_width / 8) * 2 + (
            self.tile_size - self.image_size) / 2), (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Bishop("white", 14, ((self.display_width / 8) * 2 + (
            self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        self.pieces.append(pieces.Bishop("black", 15, ((self.display_width / 8) * 5 + (
            self.tile_size - self.image_size) / 2), (self.display_height / 8) + (self.tile_size - self.image_size) / 2))
        self.pieces.append(pieces.Bishop("white", 16, ((self.display_width / 8) * 5 + (
            self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 8 + (self.tile_size - 50) / 2)))
        
        j = 0
        for i in range(8):
            self.pieces.append(pieces.Pawn("black", 17 + j, ((self.display_width / 8) * i + (
                self.tile_size - self.image_size) / 2), (self.display_height / 8) * 2 + (self.tile_size - self.image_size) / 2))
            j+=1
            self.pieces.append(pieces.Pawn("white", 17 + j, ((self.display_width / 8) * i + (
                self.tile_size - self.image_size) / 2), (self.display_height / 8) * 7 + (self.tile_size - 50) / 2))
            j+=1

    def catch_pieces(self, x, y):
        move = True
        check = False
        for p in self.pieces:
            if p._get_rect().collidepoint(self.get_pieces_coordinates(x),self.get_pieces_coordinates(y)):
                p.select()
                check = True
                break
        if check is False:
                move = False
        if move is True:
            self.piece_selected = True
        self.moving = move

    def get_pieces_coordinates(self, value):
        value = int(value / self.tile_size) * self.tile_size
        return value + 25 # image size / 2

    def put_pieces(self, x, y):
        move = True
        check = False

        for p in self.pieces:
            if p.is_selected() is True:
                eat = self.check_eating(self.get_pieces_coordinates(x), self.get_pieces_coordinates(y), p)
                if eat == False:
                   return
                p.unselect(self.get_pieces_coordinates(x), self.get_pieces_coordinates(y))
                check = True
                break

        if check is False:
            move = False
        if move is True:
            self.piece_selected = False
        self.moving = move

    def check_eating(self, x, y, p2):
        for p in self.pieces:
            if p._get_rect().collidepoint(x, y):
                if p.get_id() == p2.get_id():
                   return True
                if p.get_color() == "black" and p2.get_color() == "white":
                    p.set_position(self.black_eat, 690)
                    p._set_rect(self.black_eat, 690)
                    self.black_eat = self.black_eat + 30
                    return True
                if p.get_color() == "white" and p2.get_color() == "black":
                    p.set_position(self.white_eat, 10)
                    p._set_rect(self.white_eat, 10)
                    self.white_eat = self.white_eat + 30
                    return True
                return False


    def move_pieces(self, x, y):
        for p in self.pieces:
            if p.is_selected() is True:
                p.set_position(x, y)
                break

    def display_pieces(self):
        for p in self.pieces:
            p.display_piece(self.gameDisplay, self.pieces)

    def print_board(self):

        pg.display.set_caption('Chess Game')

        colors = itertools.cycle((self.beige, self.brown))

        width, height = 8 * self.tile_size, 8 * self.tile_size
        background = pg.Surface((width, height))

        for y in range(0, height, self.tile_size):
            for x in range(0, width, self.tile_size):
                rect = (x, y, self.tile_size, self.tile_size)
                pg.draw.rect(background, next(colors), rect)
            next(colors)

        clock = pg.time.Clock()
        crashed = False

        while not crashed:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    crashed = True
                if event.type == pg.MOUSEBUTTONDOWN and self.piece_selected is False:
                    pos = pg.mouse.get_pos()
                    if self.play_again.isOver(pos):
                        return True
                    x, y = event.pos
                    self.catch_pieces(x, y)
                elif event.type == pg.MOUSEBUTTONDOWN and self.piece_selected is True:
                    x, y = event.pos
                    self.put_pieces(x, y)
                elif event.type == pg.MOUSEMOTION:
                    pos = pg.mouse.get_pos()
                    if self.play_again.isOver(pos):
                        self.play_again.color = (149, 69, 53)
                    else:
                        self.play_again.color = (254, 243, 206)
                    if self.moving:
                        self.move_pieces(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
                else:
                    pass

            self.gameDisplay.fill((255, 255, 255))
            self.gameDisplay.blit(background, (0, 76))

            self.display_pieces()
            self.play_again.draw(self.gameDisplay)

            pg.display.update()
            clock.tick(60)

        pg.quit()
        return False

def play():
    my_chess = ChessGame()
    return my_chess.print_board()

def main():
    while True:
        if play() is False:
            break

if __name__ == '__main__':
    main()
