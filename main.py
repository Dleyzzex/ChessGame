import itertools
import pygame as pg
import pieces


def print_board():
    pg.init()

    display_width = 608
    display_height = 608
    image_size = 50

    brown = (149, 69, 53)
    beige = (254, 243, 206)
    gameDisplay = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption('Chess Game')

    colors = itertools.cycle((beige, brown))
    tile_size = 76
    width, height = 8 * tile_size, 8 * tile_size
    background = pg.Surface((width, height))

    QUEEN_BLACK = pieces.Queen("black", ((display_width / 8) * 3 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    QUEEN_WHITE = pieces.Queen("white", ((display_width / 8) * 3 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))
    KING_BLACK = pieces.King("black", ((display_width / 8) * 4 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    KING_WHITE = pieces.King("white", ((display_width / 8) * 4 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))

    ROOK_BLACK_1 = pieces.Rook("black", ((tile_size - image_size) / 2), (tile_size - image_size) / 2)
    ROOK_WHITE_1 = pieces.Rook("white", ((tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))
    ROOK_BLACK_2 = pieces.Rook("black", ((display_width / 8) * 7 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    ROOK_WHITE_2 = pieces.Rook("white", ((display_width / 8) * 7 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))

    KNIGHT_BLACK_1 = pieces.Knight("black", ((display_width / 8) + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    KNIGHT_WHITE_1 = pieces.Knight("white", ((display_width / 8) + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))
    KNIGHT_BLACK_2 = pieces.Knight("black", ((display_width / 8) * 6 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    KNIGHT_WHITE_2 = pieces.Knight("white", ((display_width / 8) * 6 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))

    BISHOP_BLACK_1 = pieces.Bishop("black", ((display_width / 8) * 2 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    BISHOP_WHITE_1 = pieces.Bishop("white", ((display_width / 8) * 2 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))
    BISHOP_BLACK_2 = pieces.Bishop("black", ((display_width / 8) * 5 + (tile_size - image_size) / 2), (tile_size - image_size) / 2)
    BISHOP_WHITE_2 = pieces.Bishop("white", ((display_width / 8) * 5 + (tile_size - image_size) / 2), ((display_height / 8) * 7 + (tile_size-50) / 2))

    PAWN_BLACK, PAWN_WHITE = [], []
    for i in range(8):
        PAWN_BLACK.append(pieces.Pawn("black", ((display_width / 8) * i + (tile_size - image_size) / 2), (display_height / 8) + (tile_size - image_size) / 2))
        PAWN_WHITE.append(pieces.Pawn("white", ((display_width / 8) * i + (tile_size - image_size) / 2), (display_height / 8) * 6 + (tile_size-50) / 2))

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            rect = (x, y, tile_size, tile_size)
            pg.draw.rect(background, next(colors), rect)
        next(colors)

    clock = pg.time.Clock()
    crashed = False

    while not crashed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True
            if event.type == pg.MOUSEBUTTONDOWN and QUEEN_WHITE.is_selected() is False:
                x, y = event.pos
                if QUEEN_WHITE_RECT[0] < x < QUEEN_WHITE_RECT[2] and QUEEN_WHITE_RECT[1] < y < QUEEN_WHITE_RECT[3]:
                    QUEEN_WHITE.select()
            elif event.type == pg.MOUSEBUTTONDOWN and QUEEN_WHITE.is_selected() is True:
                x, y = event.pos
                QUEEN_WHITE.set_position(x-15, y-15)
                QUEEN_WHITE.unselect()
            else:
                pass

        gameDisplay.fill((60, 70, 90))
        gameDisplay.blit(background, (0, 0))

        # Display pieces
        gameDisplay.blit(QUEEN_BLACK.get_image(), QUEEN_BLACK.get_position())
        gameDisplay.blit(QUEEN_WHITE.get_image(), QUEEN_WHITE.get_position())
        gameDisplay.blit(KING_BLACK.get_image(), KING_BLACK.get_position())
        gameDisplay.blit(KING_WHITE.get_image(), KING_WHITE.get_position())

        gameDisplay.blit(ROOK_BLACK_1.get_image(), ROOK_BLACK_1.get_position())
        gameDisplay.blit(ROOK_BLACK_2.get_image(), ROOK_BLACK_2.get_position())
        gameDisplay.blit(ROOK_WHITE_1.get_image(), ROOK_WHITE_1.get_position())
        gameDisplay.blit(ROOK_WHITE_2.get_image(), ROOK_WHITE_2.get_position())

        gameDisplay.blit(KNIGHT_BLACK_1.get_image(), KNIGHT_BLACK_1.get_position())
        gameDisplay.blit(KNIGHT_BLACK_2.get_image(), KNIGHT_BLACK_2.get_position())
        gameDisplay.blit(KNIGHT_WHITE_1.get_image(), KNIGHT_WHITE_1.get_position())
        gameDisplay.blit(KNIGHT_WHITE_2.get_image(), KNIGHT_WHITE_2.get_position())

        gameDisplay.blit(BISHOP_BLACK_1.get_image(), BISHOP_BLACK_1.get_position())
        gameDisplay.blit(BISHOP_BLACK_2.get_image(), BISHOP_BLACK_2.get_position())
        gameDisplay.blit(BISHOP_WHITE_1.get_image(), BISHOP_WHITE_1.get_position())
        gameDisplay.blit(BISHOP_WHITE_2.get_image(), BISHOP_WHITE_2.get_position())

        for i in range(8):
            gameDisplay.blit(PAWN_BLACK[i].get_image(), PAWN_BLACK[i].get_position())
            gameDisplay.blit(PAWN_WHITE[i].get_image(), PAWN_WHITE[i].get_position())

        QUEEN_WHITE_RECT = QUEEN_WHITE._get_rect()

        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()


if __name__ == '__main__':
    print_board()
