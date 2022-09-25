board =['_' for i in range(9)]

def makeMove(m,p):
    if m<1 or m>10  or board[m-1]!='_': 
        print("invalid")
        return False
    board[m-1]=p
    return True

def movesLeft(board):
    if '_' in board:
        return True
    return False

def checkWinner(board):
    k=0
    for i in range(3):
        if board[0+i]==board[3+i]==board[6+i]:
            if board[0+i]=='x':
                return 1 
            elif board[0+i]=='o': return 2

        if board[k]==board[k+1]==board[k+2]:
            if board[k]=='x':
                return 1 
            elif board[k]=='o': return 2
        k+=3
    if board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
        if board[4]=='x':
            return 1 
        elif board[4]=='o': return 2
    return None

def printBoard():
    k=0
    for i in range(3):
        for j in range(3):
            print(board[k],end="")
            k+=1
        print()


def aiMove():
  bestScore=float('-inf')
  move=None 
  for idx,i in enumerate(board):
    if i =='_':
      board[idx]='o'
      score=minimax(board,False)
      board[idx]='_'
      if score>bestScore:
        bestScore=score
        move=idx+1
  
  print("idx,move",idx,move)
  return move

def minimax(board,isMaximizing):
  result = checkWinner(board) 
  if result != None or not movesLeft(board):
    scores={
        1:-1,
        2:1,
        None:0
    }
    return scores[result]

  if isMaximizing:
    bestScore=float('-inf')
    for idx,i in enumerate(board):
      if i =='_':
        board[idx]='o'
        score=minimax(board,False)
        board[idx]='_'
        bestScore=max(score,bestScore)
    return bestScore
  else:
    bestScore=float('inf')
    for idx,i in enumerate(board):
      if i =='_':
        board[idx]='x'
        score=minimax(board,True)
        board[idx]='_'
        bestScore=min(score,bestScore)
    return bestScore

#driver code
p1=True
while(checkWinner(board)==None and movesLeft(board)):
    if p1:
        print("player 1 turn")
        p=int(input())
        if makeMove(p,'x'):
            p1=False
    else:
        print("player 2 turn")
        p=aiMove()
        if makeMove(p,'o'):
            p1=True
    printBoard()


if checkWinner(board)==1:
    print("Player 1 wins")
elif checkWinner(board)==2:
    print("Player 2 wins")
else: 
    print("draw")

