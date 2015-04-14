# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment



###How I do my stuff:

### One hash for Pseudocode

### Two for comments

### three for anything else

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetPieceName(Rank, File, Board):
  
  ### print("[DEBUG]", Rank, File, '"'+Board[Rank][File]+'"')
  
  ShortHandColour = Board[File][Rank][0]
  EnglishColours = {"B":"Black", "W":"White", " ":""}
  FullColour = EnglishColours[ShortHandColour]

  PieceNames = {"S":"Sarrum", "E":"Eltu", "R":"Redum", "M":"Marzaz pani", "G":"Gisigir", "N":"Nabu", " ":"Empty"}
  ShortHandName = Board[File][Rank][1]
  FullName = PieceNames[ShortHandName]

  return FullColour, FullName

def GetTypeOfGame():
  choice = ''
  while choice not in ['yes', 'no', 'y', 'n']:
    choice = input("Do you want to play the sample game (enter Y for Yes)? ").lower()
    if choice not in ['yes', 'no', 'y', 'n']:
      print("That's not a valid input, you've got to try again")

  ## the first character of the choice will be what the program is expecting, and from what I can make out it is also in uppercase.
  TypeOfGame = choice[0].upper()
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")
 
def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  
  ## this function will go and check if there is a sarrum in the space
  ## that is going to be moved into
  
  if Board[FinishRank][FinishFile][1] == "S": ## if the peice at the finishing position is a sarrum
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("    +--+--+--+--+--+--+--+--+")
    print("R{0}".format(RankNo), end="  ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("│" + Board[RankNo][FileNo], end="")
    print("│")
  print("    +--+--+--+--+--+--+--+--+")
  #print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  
  CheckRedumMoveIsLegal = False
  
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
        
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True

      
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  
  CheckSarrumMoveIsLegal = False
  
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1: ## this means the sarrum doesn' have to move
    CheckSarrumMoveIsLegal = True
    
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  
  if RankDifference == 0:
    ## rank difference of zero means horizontal movement
    ## if the peice is moving to the left
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      ## check that there are no peices in between first and final places.
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    ## if the peice is moving to the right
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      ## check that there are no peices in between
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
          
  elif FileDifference == 0:
    ## file difference of zero means vertical
    ## if the peice is moving up
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      ## check that all the spaces between it and it's final space
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    ## if the object is moving down
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      ## check that all the spaces in between it and it's final destination are empty
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  ## return the bool, true if legal, false if illegal
  return GisgigirMoveIsLegal #bool

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  ## check that the nabu moves only one space diagonally
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal #bool

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  ## can move either vertically or horizontally
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  ## can move exactly 2 in any direction
  ## does not take into account the fact it cannot jump spaces
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

 def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True

  
  ##if there is no movement then the move is not valid
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  ##movement helps in making the move valid
  ##If the player tries to move off of the board
  elif not(0 < FinishFile < 9) or not( 0 < FinishRank < 9):
    ## then it move is illegal.
    MoveIsLegal = False

    
  else:

    ## get the piece data from the arraay of the target peices
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    ## check whose turn it is
    
    if WhoseTurn == "W":
      ## the white's turn cannot move the other team's players
      if PieceColour != "W":
        MoveIsLegal = False
      ## white pieces cannot move on top of other white peices
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else: ## in other words "if WhoseTurn == "B""
      
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def CheckWithRedum(Board, FinishRank, FinishFile, WhoseTurn):
    WhiteTurn = WhoseTurn == "W"
    InCheck = False
    if Board[(FinishRank+1)%len(Board)][(FinishFile+1)%len(Board)] == "WS" and not WhiteTurn:
        InCheck = True
    elif Board[FinishRank+1][FinishFile-1] == "WS" and not WhiteTurn:
        InCheck = True
    elif Board[(FinishRank+1)%len(Board)][(FinishFile+1)%len(Board)] == "BS" and WhiteTurn:
        InCheck = True
    elif Board[FinishRank+1][FinishFile-1] == "BS" and WhiteTurn:
        InCheck = True
    return InCheck

def CheckWithNabu(Board, FinishRank, FinishFile, WhoseTurn):
    WhiteTurn = WhoseTurn == "W"
    if not WhiteTurn:
        opponent = "W"
    else:
        opponent = "B"

    InCheck = False

    if Board[FinishRank+1][FinishFile+1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank+1][FinishFile-1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank-1][FinishFile+1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank-1][FinishFile+1] == opponent+"S":
        InCheck = True

    return InCheck
    

def CheckWithMarzazPani(Board, FinishRank, FinishFile, WhoseTurn):
    WhiteTurn = WhoseTurn == "W"
    if not WhiteTurn:
        opponent = "W"
    else:
        opponent = "B"

    InCheck = False

    if Board[FinishRank][FinishFile+1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank][FinishFile-1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank+1][FinishFile] == opponent+"S":
        InCheck = True
    elif Board[FinishRank-1][FinishFile] == opponent+"S":
        InCheck = True

    return InCheck

def CheckWithEltu(Board, FinishRank, FinishFile, WhoseTurn):
    WhiteTurn = WhoseTurn == "W"
    if not WhiteTurn:
        opponent = "W"
    else:
        opponent = "B"

    InCheck = False

    if Board[FinishRank+2][FinishFile] == opponent+"S":
        InCheck = True
    elif Board[FinishRank-2][FinishFile] == opponent+"S":
        InCheck = True
    elif Board[FinishRank][FinishFile+2] == opponent+"S":
        InCheck = True
    elif Board[FinishRank][FinishFile-2] == opponent+"S":
        InCheck = True

    return InCheck

def CheckWithGisgigir(Board, FinishRank, FinishFile, WhoseTurn):
    WhiteTurn = WhoseTurn == "W"
    if not WhiteTurn:
        opponent = "W"
    else:
        opponent = "B"
    ## loop through each direction, stopping when a peice is found
    ## then check if that piece is an enemy sarrum

    InCheck = False

    ##in x axis, from the piece's position to the right hand side
    for FileCount in range(FinishFile+1, 9): ##the range function is not inclusive
        if Board[FinishRank][FileCount] == "  ":
            continue
        elif Board[FinishRank][FileCount] == opponent+"S":
            InCheck = True
            break
        else:
            break
    ## in x axis, from left to right.
    for FileCount in range(FinishFile-1, 0, -1): ##the range function is not inclusive
        if Board[FinishRank][FileCount] == "  ":
            continue
        elif Board[FinishRank][FileCount] == opponent+"S":
            InCheck = True
            return InCheck
        elif Board[FinishRank][FileCount][0] == WhoseTurn:
          break
    ## in the y axis, from up to down
    for RankCount in range(FinishRank+1, 9): ##the range function is not inclusive
        if Board[RankCount][FinishFile] == "  ":
            continue
        elif Board[RankCount][FinishFile] == opponent+"S":
            InCheck = True
            break
        else:
            break
    ##in y axis, from the other way
    for RankCount in range(FinishRank-1, 0, -1): ##the range function is not inclusive
        if Board[RankCount][FileCount] == "  ":
            continue
        elif Board[FinishRank][FileCount] == opponent+"S":
            InCheck = True
            break
        else:
            break
    
    return InCheck

def CheckSarrumInCheck(Board, FinishRank, FinishFile, WhoseTurn):
    BOARDDIMENTION = 8
    WhiteTurn = WhoseTurn == "W"
    if not WhiteTurn:
        opponent = "W"
    else:
        opponent = "B"

    IsInCheck = False
        
    ## Linear search the heck out of the board, evaluate the moves of the other pieces
    for Rank in range(1, BOARDDIMENTION + 1):
        for File in range(1, BOARDDIMENTION + 1):
            if Board[Rank][File] != "  " and Board[Rank][File][0] != opponent and not IsInCheck:
                ThisPiece = Board[Rank][File]
                if ThisPiece[1] == "R":
                    IsInCheck = CheckWithRedum(Board, Rank, File, WhoseTurn)
                    break
                elif ThisPiece[1] == "N":
                    IsInCheck = CheckWithNabu(Board, Rank, File, WhoseTurn)
                    break
                elif ThisPiece[1] == "E":
                    IsInCheck = CheckWithEltu(Board, Rank, File, WhoseTurn)
                    break
                elif ThisPiece[1] == "G":
                    IsInCheck = CheckWithGisgigir(Board, Rank, File, WhoseTurn)
                    break
                elif ThisPiece[1] == "M":
                    IsInCheck = CheckWithMarzazPani(Board, Rank, File, WhoseTurn)
    return IsInCheck

def CheckMessage(WhoseTurn):
    if WhoseTurn == "B":
        print("The White Sarrum is in Check")
    else:
        print("The Black Sarrum is in Check")
    


def GetValidBoardPosition(rank, file):
    ## invalid board position? I'm not entirely sure what the question asks
    if not(0 < rank < 9) and not(0 < file < 9):
        return False
    else:
        return True

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    ## create an empty board
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    ## now add all the peices for the demo game
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    ##this bit sets up the board for a normal game, with all the peices in
    ##their proper place.
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
          
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
          
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
            
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
            
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
            
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
            
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
            
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
            
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
            
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  ## this is going to need validating isn't it?
  Valid = False
  while not Valid:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if not (10 < StartSquare < 89):
        print("Please enter both the rank and file")
      else:
        Valid = True
    except ValueError:
      print("Please enter some valid data")
  Valid = False
  while not Valid:
    try:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if not (10 < FinishSquare < 89):
        print("Please enter a valid input")
      else:
        Valid = True
    except ValueError:
      print("Please enter some valid data")
      
  return StartSquare, FinishSquare

def ConfirmMove(StartSquare, FinishSquare, board): ## Boolean function
  StartCoords = (StartSquare//10, StartSquare%10)
  EndCoords = (FinishSquare//10, FinishSquare%10)
  #PieceAtTheStart = board[StartCoords[0]][StartCoords[1]]
  PieceAtTheStartColour, PieceAtTheStartName = GetPieceName(StartCoords[0], StartCoords[1], board)
  PieceAtTheFinishColour, PieceAtTheFinishName = GetPieceName(EndCoords[0], EndCoords[1], board)
  
  
  print("Are you sure you want to move the {1} in {0} to the {2} in {3}".format(StartCoords, PieceAtTheStartColour+" "+PieceAtTheStartName,
                                                                                PieceAtTheFinishColour+" "+PieceAtTheFinishName, EndCoords))
  ## String Formatting:
  ##    0: Startcoords
  ##    1: The type and colour of the piece in that square
  ##    2: Endcoords
  ##    3: The type and colour of the piece in that square (If applicable)

  Response = input("Enter Y or N").lower()
  while Response not in ["yes", "y", "n", "no"]:
    Response= input("Please enter something valid").lower()

  if Response == "y":
    print("Move confirmed")
    return True
  else:
    print("Move cancelled")
    return False
        

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    ## White Redum becomes a Marzaz Pani
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White Redum Promoted")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    ## Black Redum becomes a Marzaz Pani
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black Redum Promoted")
  else:
    ###DisplayBoard(Board)
    ##Enrty point for the code to inform the user what piece they've just taken
    PieceColour, PieceType = GetPieceName(FinishRank, FinishFile, Board)
    ###print("[DEBUG]", '"'+Board[FinishRank][FinishFile]+'"')
    #if Board[FinishFile][FinishRank] != "  ":
    print("You've just taken a {0} {1}".format(PieceColour, PieceType))
    ## This code swaps the pieces around
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

    

    
if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    ## Do you want to play a game?
    WhoseTurn = "W"
    GameOver = False
    ## uses my nicely validated function
    SampleGame = GetTypeOfGame()
    ## rather than doing `IF SampleGame == "y"`etc, they have decided to do something stupid
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    ## just why? it doesn't do anything actually uesful, it's just bad
    
    ## get this party started
    InitialiseBoard(Board, SampleGame)

    ## keep going until the fat lady sings
    while not(GameOver):
      ## NB: This is effectively the start of the turn, this is where I should impliment the `check` function
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):

        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        ## okay, so rather than dealing with strings, they have chosen to work out which
        ## character is which mathematically
        ## again, not a logical choice? Anyone could just put in any number and break it
        
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")

      
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      isCheck = CheckSarrumInCheck(Board, FinishRank, FinishFile, WhoseTurn)
      MoveConfirm = ConfirmMove(StartSquare, FinishSquare, Board)
      if MoveConfirm:
        MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if isCheck:
        CheckMessage(WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)

      ## swap it's now the other player's turn
      if WhoseTurn == "W" and MoveConfirm:
        WhoseTurn = "B"
      elif WhoseTurn != "W" and MoveConfirm:
        WhoseTurn = "W"
      ##else (if MoveConfirm is false)
        ## Allow the player to continue their turn

      ## this could be done really easily if the turn was kept track of using a bool - the statement could be `WhoseTurn = (not WhoseTurn)`
      
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
