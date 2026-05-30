import pygame as p
import ChessEngine as CE

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
IMAGES = {}

def load_images():
    pieces = ["wp","wR","wN","wB","wQ","wK","bp","bR","bN","bB","bK","bQ"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")


def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill("white")

    gs = CE.GameState()
    valid_moves = gs.get_all_moves()
    move_made = False
    load_images()

    sq_selected = ()
    player_clicks = []
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            #MOUSE HANDLERS
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sq_selected == (row,col):
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2:
                    move = CE.Move(player_clicks[0],player_clicks[1],gs.board)
                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                    player_clicks = []
                    sq_selected = ()
            #KEY HANDLERS
            elif event.type == p.KEYDOWN:
                    if event.key == p.K_z:
                        try:
                            gs.undo_move()
                            move_made = True
                        except IndexError as e:
                            print(e)
                        sq_selected = ()
                        player_clicks = []
        if move_made:
            valid_moves = gs.get_all_moves()
            move_made = False

        drawGameState(screen,gs)
        p.display.flip()
        clock.tick(30)

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

def drawBoard(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (r+c)%2 == 0:
                color = "white"
            else:
                color = "gray"
            p.draw.rect(screen,color,p.Rect( c*SQ_SIZE, r*SQ_SIZE ,SQ_SIZE,SQ_SIZE))


def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect( c*SQ_SIZE, r*SQ_SIZE ,SQ_SIZE,SQ_SIZE))



main()