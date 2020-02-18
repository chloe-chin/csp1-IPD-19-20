####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Wolves' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

strategy1_name = 'collude then betray twice'
strategy1_description = 'In this strategy, the player will start off by colluding and then betray for the next two moves. After the two betrays, they will collude again'

def move1(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
  if len(my_history) == 0 or len(my_history) % 3 == 0
    return 'c'
  else:
    return 'b'

strategy2_name = 'return opposite'
strategy2_description = 'If the opponent betrays, then collude next round. If the opponent colludes, then betray the next round. first round is collude.'

def move2(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history) == 0:
      return 'c'
    elif their_history[-1] == 'b':
      return 'c'
    else:
      return 'b'

strategy3_name = 'If collude, then collude. If betray, then betray twice'
strategy3_description = 'One where if the opponent colludes, then this player will collude for the next turn. If the opponent betrays, this player will betray for the next 2 turns. This dependence on the opponent’s turn will be reset at the collude or the 2nd betrayal of this player. Betrayal is first turn'

def move3(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
  '''
  if len(my_history) == 0:
    return 'b'
  elif their_history[-1] == 'c':
    return 'c'
  elif their_history[-1] == 'b' or their_history[-2] == 'b':
    return 'b'
  else:
    return 'c'
