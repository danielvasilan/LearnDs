
class GomokuGame:

    def __init__(self, gameNo, tblRows, tblCols):
        self.tblRows = tblRows
        self.tblCols = tblCols
        self.gameNo = gameNo
        self.segLength = 3
        self.cells = []
        self.char_1 = "X"
        self.char_2 = "0"
        for p in range(self.tblRows * tblCols):
            self.cells.append(" ")

    def rc2p(self, r, c):
        p = (r - 1) * self.tblCols + c -1
        # print(str(r)+str(c)+str(p))
        return p

    def getAtPos(self, p):
        return self.cells[p]

    def getAtRc(self, r, c):
        p = self.rc2p(r, c)
        return self.getAtPos(p)

    def printTable(self):
        print ('Game ' + str(self.gameNo))
        print ("+ " + ('- ' * self.tblCols) + "+")
        for r in range(self.tblRows):
            rowOutput = ""
            #print("r=" + str(r))
            for c in range(self.tblCols):
                rowOutput += self.getAtRc(r+1, c+1) + " "
                #print("c=" + str(c))
            print ("| " + rowOutput + "|")
        print ("+ " + ('- ' * self.tblCols) + "+")
        #print (self.cells)

    def checkWinner (self):


    def makeMove(self, r, c):
        move_pos = self.rc2p(r, c)
        if self.cells.count(self.char_1) > self.cells.count(self.char_2):
            self.cells[move_pos] = self.char_2
        else:
            self.cells[move_pos] = self.char_1

class GameSimulator:
    def __init(self, nrOfGames)__:
        self.nrOfGames = nrOfGames

    def simulate():
        for g in range(self.nrOfGames):
            game = GomokuGame(g, 3, 4)
            game.makeMove()
game.makeMove(1, 2)
game.makeMove(1, 1)
game.makeMove(2, 2)
            

game = GomokuGame(1, 3, 4)
game.makeMove(1, 2)
game.makeMove(1, 1)
game.makeMove(2, 2)


game.printTable()