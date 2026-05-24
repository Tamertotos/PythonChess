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
    running = True
    screen.fill("white")
    gs = CE.GameState()
    print(gs.board)
    load_images()
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
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