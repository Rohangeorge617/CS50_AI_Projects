"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
  Xcount = board[0].count(X) + board[1].count(X) + board[2].count(X)
  Ocount = board[0].count(O) + board[1].count(O) + board[2].count(O)
  
  if Xcount == Ocount:
     return X
  elif Xcount > Ocount:
     return O
    
  """
  Returns player who has the next turn on a board.
  """
  raise NotImplementedError


def actions(board):
  if terminal(board) == True:
     return None
  set_actions = set()
  for i in range(3):
    for j in range(3):
      if board[i][j] == EMPTY:
        set_actions.add((i,j))
  return set_actions

    

  """
  Returns set of all possible actions (i, j) available on the board.
  """
  raise NotImplementedError



def result(board, action):

  """
  Returns the board that results from making move (i, j) on the board.
  """
  
  if action not in actions(board):
     raise Exception("This action is not possible")
  i,j = action
  duplicate = copy.deepcopy(board)
  duplicate[i][j] = player(board)
  return duplicate
  
   
def Rows(board, player):
   for i in range(3):
      if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] == player:
         return True
   return False

def Columns(board, player):
   for j in range(3):
      if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[2][j] == player:
         return True
   return False

def Diagonals(board, player):
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == player:
     return True
  if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == player:
     return True
  return False


   
def winner(board):
    
    if Rows(board, X) or Columns(board, X) or Diagonals(board, X):
       return X
    elif Rows(board, O) or Columns(board, O) or Diagonals(board, O):
       return O
    else:
       return None
    
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    if winner(board) != None:
       return True
    for i in range(3):
       for j in range(3):
          if board[i][j] == EMPTY:
             return False
    return True
     
    """       
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    if winner(board) == X:
       return 1
    elif winner(board) == O:
       return -1
    elif winner(board) == None:
       return 0
    
       

    """
    Returns 1 if O has won the game, -1 if X has won, 0 otherwise.
    """
    raise NotImplementedError


def maximize(board, alpha, beta):
   score = -math.inf
   if terminal(board) == True:
      return utility(board)
   for action in actions(board):
      score = max(score, minimize(result(board, action), alpha, beta))
      alpha = max(alpha, score)
      if alpha >= beta:
         break
   return score

def minimize(board, alpha, beta):
   score = math.inf
   if terminal(board) == True:
      return utility(board)
   for action in actions(board):
      score = min(score, maximize(result(board, action), alpha, beta))
      beta = min(beta, score)
      if alpha >= beta:
         break
   return score

def minimax(board):
  if terminal(board) == True:
     return None
  elif player(board) == X:
     score = -math.inf
     best_action = None
     for action in actions(board):
       new_score = minimize(result(board, action), -math.inf, math.inf)
       if new_score > score:
            score = new_score
            best_action = action
     return best_action
  
  elif player(board) == O:
     score = math.inf
     best_action = None
     for action in actions(board):
       new_score = maximize(result(board, action), -math.inf, math.inf)
       if new_score < score:
          score = new_score
          best_action = action
     return best_action

  """
  Returns the optimal action for the current player on the board.
  """
  raise NotImplementedError


         