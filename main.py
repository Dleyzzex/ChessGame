import itertools
import pygame as pg
import pieces


class ChessGame:
    def __init__(self):
        pg.init()
        self.display_width = 608
        self.display_height = 608
        self.piece_selected = False
        self.gameDisplay = pg.display.set_mode((self.display_width, self.display_height))
        self.image_size = 50
        self.tile_size = 76
        self.brown = (149, 69, 53)
        self.beige = (254, 243, 206)
        self.moving = False

        self.QUEEN_BLACK = pieces.Queen("black", ((self.display_width / 8) * 3 + (self.tile_size - self.image_size) / 2),
                                        (self.tile_size - self.image_size) / 2)
        self.QUEEN_WHITE = pieces.Queen("white", ((self.display_width / 8) * 3 + (self.tile_size - self.image_size) / 2),
                                        ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))
        self.KING_BLACK = pieces.King("black", ((self.display_width / 8) * 4 + (self.tile_size - self.image_size) / 2),
                                        (self.tile_size - self.image_size) / 2)
        self.KING_WHITE = pieces.King("white", ((self.display_width / 8) * 4 + (self.tile_size - self.image_size) / 2),
                                        ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))

        self.ROOK_BLACK_1 = pieces.Rook("black", ((self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.ROOK_WHITE_1 = pieces.Rook("white", ((self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))
        self.ROOK_BLACK_2 = pieces.Rook("black", ((self.display_width / 8) * 7 + (
                    self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.ROOK_WHITE_2 = pieces.Rook("white", ((self.display_width / 8) * 7 + (
                    self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))

        self.KNIGHT_BLACK_1 = pieces.Knight("black", ((self.display_width / 8) + (
                    self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.KNIGHT_WHITE_1 = pieces.Knight("white", ((self.display_width / 8) + (
                    self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))
        self.KNIGHT_BLACK_2 = pieces.Knight("black", ((self.display_width / 8) * 6 + (
                    self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.KNIGHT_WHITE_2 = pieces.Knight("white", ((self.display_width / 8) * 6 + (
                    self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))

        self.BISHOP_BLACK_1 = pieces.Bishop("black", ((self.display_width / 8) * 2 + (
                    self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.BISHOP_WHITE_1 = pieces.Bishop("white", ((self.display_width / 8) * 2 + (
                    self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))
        self.BISHOP_BLACK_2 = pieces.Bishop("black", ((self.display_width / 8) * 5 + (
                    self.tile_size - self.image_size) / 2), (self.tile_size - self.image_size) / 2)
        self.BISHOP_WHITE_2 = pieces.Bishop("white", ((self.display_width / 8) * 5 + (
                    self.tile_size - self.image_size) / 2), ((self.display_height / 8) * 7 + (self.tile_size - 50) / 2))

        self.PAWN_BLACK, self.PAWN_WHITE = [], []
        for i in range(8):
            self.PAWN_BLACK.append(pieces.Pawn("black", ((self.display_width / 8) * i + (
                        self.tile_size - self.image_size) / 2), (self.display_height / 8) + (
                                                      self.tile_size - self.image_size) / 2))
            self.PAWN_WHITE.append(pieces.Pawn("white", ((self.display_width / 8) * i + (
                        self.tile_size - self.image_size) / 2), (self.display_height / 8) * 6 + (
                                                      self.tile_size - 50) / 2))

    def catch_pieces(self, x, y):
        move = True

        if self.QUEEN_WHITE._get_rect().collidepoint(x, y):
            self.QUEEN_WHITE.select()
        elif self.QUEEN_BLACK._get_rect().collidepoint(x, y):
            self.QUEEN_BLACK.select()
        elif self.KING_WHITE._get_rect().collidepoint(x, y):
            self.KING_WHITE.select()
        elif self.KING_BLACK._get_rect().collidepoint(x, y):
            self.KING_BLACK.select()
        elif self.ROOK_WHITE_1._get_rect().collidepoint(x, y):
            self.ROOK_WHITE_1.select()
        elif self.ROOK_WHITE_2._get_rect().collidepoint(x, y):
            self.ROOK_WHITE_2.select()
        elif self.ROOK_BLACK_1._get_rect().collidepoint(x, y):
            self.ROOK_BLACK_1.select()
        elif self.ROOK_BLACK_2._get_rect().collidepoint(x, y):
            self.ROOK_BLACK_2.select()
        elif self.KNIGHT_WHITE_1._get_rect().collidepoint(x, y):
            self.KNIGHT_WHITE_1.select()
        elif self.KNIGHT_WHITE_2._get_rect().collidepoint(x, y):
            self.KNIGHT_WHITE_2.select()
        elif self.KNIGHT_BLACK_1._get_rect().collidepoint(x, y):
            self.KNIGHT_BLACK_1.select()
        elif self.KNIGHT_BLACK_2._get_rect().collidepoint(x, y):
            self.KNIGHT_BLACK_2.select()
        elif self.BISHOP_WHITE_1._get_rect().collidepoint(x, y):
            self.BISHOP_WHITE_1.select()
        elif self.BISHOP_WHITE_2._get_rect().collidepoint(x, y):
            self.BISHOP_WHITE_2.select()
        elif self.BISHOP_BLACK_1._get_rect().collidepoint(x, y):
            self.BISHOP_BLACK_1.select()
        elif self.BISHOP_BLACK_2._get_rect().collidepoint(x, y):
            self.BISHOP_BLACK_2.select()
        else:
            counter = 0
            check = False
            for data_white, data_black in zip(self.PAWN_WHITE, self.PAWN_BLACK):
                if data_white._get_rect().collidepoint(x, y):
                    self.PAWN_WHITE[counter].select()
                    check = True
                    break
                elif data_black._get_rect().collidepoint(x, y):
                    self.PAWN_BLACK[counter].select()
                    check = True
                    break
                else:
                    pass
                counter = counter + 1
            if check is False:
                move = False
        if move is True:
            self.piece_selected = True
        self.moving = move

    def put_pieces(self, x, y):
        move = True

        if self.QUEEN_WHITE.is_selected() is True:
            self.check_eating(x, y)
            self.QUEEN_WHITE.unselect(x, y)
        elif self.QUEEN_BLACK.is_selected() is True:
            self.check_eating(x, y)
            self.QUEEN_BLACK.unselect(x, y)
        elif self.KING_WHITE.is_selected() is True:
            self.check_eating(x, y)
            self.KING_WHITE.unselect(x, y)
        elif self.KING_BLACK.is_selected() is True:
            self.check_eating(x, y)
            self.KING_BLACK.unselect(x, y)
        elif self.ROOK_WHITE_1.is_selected() is True:
            self.check_eating(x, y)
            self.ROOK_WHITE_1.unselect(x, y)
        elif self.ROOK_WHITE_2.is_selected() is True:
            self.check_eating(x, y)
            self.ROOK_WHITE_2.unselect(x, y)
        elif self.ROOK_BLACK_1.is_selected() is True:
            self.check_eating(x, y)
            self.ROOK_BLACK_1.unselect(x, y)
        elif self.ROOK_BLACK_2.is_selected() is True:
            self.check_eating(x, y)
            self.ROOK_BLACK_2.unselect(x, y)
        elif self.KNIGHT_WHITE_1.is_selected() is True:
            self.check_eating(x, y)
            self.KNIGHT_WHITE_1.unselect(x, y)
        elif self.KNIGHT_WHITE_2.is_selected() is True:
            self.check_eating(x, y)
            self.KNIGHT_WHITE_2.unselect(x, y)
        elif self.KNIGHT_BLACK_1.is_selected() is True:
            self.check_eating(x, y)
            self.KNIGHT_BLACK_1.unselect(x, y)
        elif self.KNIGHT_BLACK_2.is_selected() is True:
            self.check_eating(x, y)
            self.KNIGHT_BLACK_2.unselect(x, y)
        elif self.BISHOP_WHITE_1.is_selected() is True:
            self.check_eating(x, y)
            self.BISHOP_WHITE_1.unselect(x, y)
        elif self.BISHOP_WHITE_2.is_selected() is True:
            self.check_eating(x, y)
            self.BISHOP_WHITE_2.unselect(x, y)
        elif self.BISHOP_BLACK_1.is_selected() is True:
            self.check_eating(x, y)
            self.BISHOP_BLACK_1.unselect(x, y)
        elif self.BISHOP_BLACK_2.is_selected() is True:
            self.check_eating(x, y)
            self.BISHOP_BLACK_2.unselect(x, y)
        else:
            counter = 0
            check = False
            for data_white, data_black in zip(self.PAWN_WHITE, self.PAWN_BLACK):
                if data_white.is_selected() is True:
                    self.check_eating(x, y)
                    data_white.unselect(x, y)
                    check = True
                    break
                elif data_black.is_selected() is True:
                    self.check_eating(x, y)
                    data_black.unselect(x, y)
                    check = True
                    break
                else:
                    pass
                counter = counter + 1
            if check is False:
                move = False
        if move is True:
            self.piece_selected = False
        self.moving = move

    def check_eating(self, x, y):
        if self.QUEEN_BLACK._get_rect().collidepoint(x, y):
            self.QUEEN_BLACK.set_position(1000, 1000)
            self.QUEEN_BLACK._set_rect(1000, 1000)
        elif self.QUEEN_WHITE._get_rect().collidepoint(x, y):
            self.QUEEN_WHITE.set_position(1000, 1000)
            self.QUEEN_WHITE._set_rect(1000, 1000)
        elif self.KING_WHITE._get_rect().collidepoint(x, y):
            self.KING_WHITE.set_position(1000, 1000)
            self.KING_WHITE._set_rect(1000, 1000)
        elif self.KING_BLACK._get_rect().collidepoint(x, y):
            self.KING_BLACK.set_position(1000, 1000)
            self.KING_BLACK._set_rect(1000, 1000)
        elif self.ROOK_WHITE_1._get_rect().collidepoint(x, y):
            self.ROOK_WHITE_1.set_position(1000, 1000)
            self.ROOK_WHITE_1._set_rect(1000, 1000)
        elif self.ROOK_WHITE_2._get_rect().collidepoint(x, y):
            self.ROOK_WHITE_2.set_position(1000, 1000)
            self.ROOK_WHITE_2._set_rect(1000, 1000)
        elif self.ROOK_BLACK_1._get_rect().collidepoint(x, y):
            self.ROOK_BLACK_1.set_position(1000, 1000)
            self.ROOK_BLACK_1._set_rect(1000, 1000)
        elif self.ROOK_BLACK_2._get_rect().collidepoint(x, y):
            self.ROOK_BLACK_2.set_position(1000, 1000)
            self.ROOK_BLACK_2._set_rect(1000, 1000)
        elif self.KNIGHT_WHITE_1._get_rect().collidepoint(x, y):
            self.KNIGHT_WHITE_1.set_position(1000, 1000)
            self.KNIGHT_WHITE_1._set_rect(1000, 1000)
        elif self.KNIGHT_WHITE_2._get_rect().collidepoint(x, y):
            self.KNIGHT_WHITE_2.set_position(1000, 1000)
            self.KNIGHT_WHITE_2._set_rect(1000, 1000)
        elif self.KNIGHT_BLACK_1._get_rect().collidepoint(x, y):
            self.KNIGHT_BLACK_1.set_position(1000, 1000)
            self.KNIGHT_BLACK_1._set_rect(1000, 1000)
        elif self.KNIGHT_BLACK_2._get_rect().collidepoint(x, y):
            self.KNIGHT_BLACK_2.set_position(1000, 1000)
            self.KNIGHT_BLACK_2._set_rect(1000, 1000)
        elif self.BISHOP_WHITE_1._get_rect().collidepoint(x, y):
            self.BISHOP_WHITE_1.set_position(1000, 1000)
            self.BISHOP_WHITE_1._set_rect(1000, 1000)
        elif self.BISHOP_WHITE_2._get_rect().collidepoint(x, y):
            self.BISHOP_WHITE_2.set_position(1000, 1000)
            self.BISHOP_WHITE_2._set_rect(1000, 1000)
        elif self.BISHOP_BLACK_1._get_rect().collidepoint(x, y):
            self.BISHOP_BLACK_1.set_position(1000, 1000)
            self.BISHOP_BLACK_1._set_rect(1000, 1000)
        elif self.BISHOP_BLACK_2._get_rect().collidepoint(x, y):
            self.BISHOP_BLACK_2.set_position(1000, 1000)
            self.BISHOP_BLACK_2._set_rect(1000, 1000)
        else:
            counter = 0
            for data_white, data_black in zip(self.PAWN_WHITE, self.PAWN_BLACK):
                if data_white._get_rect().collidepoint(x, y):
                    self.PAWN_WHITE[counter].set_position(1000, 1000)
                    self.PAWN_WHITE[counter]._set_rect(1000, 1000)
                    break
                elif data_black._get_rect().collidepoint(x, y):
                    self.PAWN_BLACK[counter].set_position(1000, 1000)
                    self.PAWN_BLACK[counter]._set_rect(1000, 1000)
                    break
                else:
                    pass
                counter = counter + 1


    # def move_pieces(self, event):
    #     QUEEN_WHITE_RECT, QUEEN_BLACK_RECT = self.QUEEN_WHITE._get_rect(), self.QUEEN_BLACK._get_rect()
    #     KING_WHITE_RECT, KING_BLACK_RECT = self.KING_WHITE._get_rect(), self.KING_BLACK._get_rect()
    #     ROOK1_WHITE_RECT, ROOK2_WHITE_RECT, ROOK1_BLACK_RECT, ROOK2_BLACK_RECT = self.ROOK_WHITE_1._get_rect(), \
    #                 self.ROOK_WHITE_2._get_rect(), self.ROOK_BLACK_1._get_rect(), self.ROOK_BLACK_2._get_rect()
    #     KNIGHT1_WHITE_RECT, KNIGHT2_WHITE_RECT, KNIGHT1_BLACK_RECT, KNIGHT2_BLACK_RECT = self.KNIGHT_WHITE_1._get_rect(), \
    #                 self.KNIGHT_WHITE_2._get_rect(), self.KNIGHT_BLACK_1._get_rect(), self.KNIGHT_BLACK_2._get_rect()
    #     BISHOP1_WHITE_RECT, BISHOP2_WHITE_RECT, BISHOP1_BLACK_RECT, BISHOP2_BLACK_RECT = self.BISHOP_WHITE_1._get_rect(), \
    #                 self.BISHOP_WHITE_2._get_rect(), self.BISHOP_BLACK_1._get_rect(), self.BISHOP_BLACK_2._get_rect()
    #     test = self.QUEEN_WHITE.get_image()
    #     if self.QUEEN_WHITE.is_selected() is True:
    #         test.get_rect().move_ip(event.rel)
    #     elif self.QUEEN_BLACK.is_selected() is True:
    #         QUEEN_BLACK_RECT.move_ip(event.rel)
    #     elif self.KING_WHITE.is_selected() is True:
    #         KING_WHITE_RECT.move_ip(event.rel)
    #     elif self.KING_BLACK.is_selected() is True:
    #         KING_BLACK_RECT.move_ip(event.rel)
    #     # elif self.ROOK_WHITE_1.is_selected() is True:
    #     #     self.ROOK_WHITE_1.unselect(x, y)
    #     # elif self.ROOK_WHITE_2.is_selected() is True:
    #     #     self.ROOK_WHITE_2.unselect(x, y)
    #     # elif self.ROOK_BLACK_1.is_selected() is True:
    #     #     self.ROOK_BLACK_1.unselect(x, y)
    #     # elif self.ROOK_BLACK_2.is_selected() is True:
    #     #     self.ROOK_BLACK_2.unselect(x, y)
    #     # elif self.KNIGHT_WHITE_1.is_selected() is True:
    #     #     self.KNIGHT_WHITE_1.unselect(x, y)
    #     # elif self.KNIGHT_WHITE_2.is_selected() is True:
    #     #     self.KNIGHT_WHITE_2.unselect(x, y)
    #     # elif self.KNIGHT_BLACK_1.is_selected() is True:
    #     #     self.KNIGHT_BLACK_1.unselect(x, y)
    #     # elif self.KNIGHT_BLACK_2.is_selected() is True:
    #     #     self.KNIGHT_BLACK_2.unselect(x, y)
    #     # elif self.BISHOP_WHITE_1.is_selected() is True:
    #     #     self.BISHOP_WHITE_1.unselect(x, y)
    #     # elif self.BISHOP_WHITE_2.is_selected() is True:
    #     #     self.BISHOP_WHITE_2.unselect(x, y)
    #     # elif self.BISHOP_BLACK_1.is_selected() is True:
    #     #     self.BISHOP_BLACK_1.unselect(x, y)
    #     # elif self.BISHOP_BLACK_2.is_selected() is True:
    #     #     self.BISHOP_BLACK_2.unselect(x, y)
    #     else:
    #         pass

    def display_pieces(self):
        # Display pieces
        self.gameDisplay.blit(self.QUEEN_BLACK.get_image(), self.QUEEN_BLACK.get_position())
        self.gameDisplay.blit(self.QUEEN_WHITE.get_image(), self.QUEEN_WHITE.get_position())
        self.gameDisplay.blit(self.KING_BLACK.get_image(), self.KING_BLACK.get_position())
        self.gameDisplay.blit(self.KING_WHITE.get_image(), self.KING_WHITE.get_position())

        self.gameDisplay.blit(self.ROOK_BLACK_1.get_image(), self.ROOK_BLACK_1.get_position())
        self.gameDisplay.blit(self.ROOK_BLACK_2.get_image(), self.ROOK_BLACK_2.get_position())
        self.gameDisplay.blit(self.ROOK_WHITE_1.get_image(), self.ROOK_WHITE_1.get_position())
        self.gameDisplay.blit(self.ROOK_WHITE_2.get_image(), self.ROOK_WHITE_2.get_position())

        self.gameDisplay.blit(self.KNIGHT_BLACK_1.get_image(), self.KNIGHT_BLACK_1.get_position())
        self.gameDisplay.blit(self.KNIGHT_BLACK_2.get_image(), self.KNIGHT_BLACK_2.get_position())
        self.gameDisplay.blit(self.KNIGHT_WHITE_1.get_image(), self.KNIGHT_WHITE_1.get_position())
        self.gameDisplay.blit(self.KNIGHT_WHITE_2.get_image(), self.KNIGHT_WHITE_2.get_position())

        self.gameDisplay.blit(self.BISHOP_BLACK_1.get_image(), self.BISHOP_BLACK_1.get_position())
        self.gameDisplay.blit(self.BISHOP_BLACK_2.get_image(), self.BISHOP_BLACK_2.get_position())
        self.gameDisplay.blit(self.BISHOP_WHITE_1.get_image(), self.BISHOP_WHITE_1.get_position())
        self.gameDisplay.blit(self.BISHOP_WHITE_2.get_image(), self.BISHOP_WHITE_2.get_position())

        for i in range(8):
            self.gameDisplay.blit(self.PAWN_BLACK[i].get_image(), self.PAWN_BLACK[i].get_position())
            self.gameDisplay.blit(self.PAWN_WHITE[i].get_image(), self.PAWN_WHITE[i].get_position())

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
                    x, y = event.pos
                    self.catch_pieces(x, y)
                    # print(self.QUEEN_WHITE.is_selected())
                    # print(self.piece_selected)
                elif event.type == pg.MOUSEBUTTONDOWN and self.piece_selected is True:
                    x, y = event.pos
                    self.put_pieces(x, y)
                # elif event.type == pg.MOUSEMOTION and self.moving:
                #     self.move_pieces(event)
                else:
                    pass

            self.gameDisplay.fill((60, 70, 90))
            self.gameDisplay.blit(background, (0, 0))

            self.display_pieces()

            pg.display.update()
            clock.tick(60)

        pg.quit()
        quit()


def main():
    my_chess = ChessGame()
    my_chess.print_board()


if __name__ == '__main__':
    main()
