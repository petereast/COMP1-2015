# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

import pickle
from datetime import date, timedelta

###How I do my stuff:

### One hash for Pseudocode

### Two for comments

### three for anything else

KashshaptuEnabled = False

BOARDDIMENSION = 8

Scores = []

class Score():
    def __init__(self, Name="", NumberOfTurns = -1, Date = None, Colour = None):
        self.Name = Name
        self.NumberOfTurns = NumberOfTurns
        self.Date = Date
        self.Colour = Colour

def vrange(start, end): ## A function that finds all of the integers between two numbers, regardless of if one is greater than the other
    #print("vrange",start, end)
    if start < end:
        #print("start < end")
        #print(list(range(start, end)))
        return range(start, end+1)
    elif start > end:
        #print("start > end")
        #print(list(range(start, end, -1)))
        return range(start, end, -1)
    else:
        #print("Errornous :(")
        return range(0, -1)


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
  EnglishColours = {"B":"Black", "W":"White", " ":"Empty"}
  FullColour = EnglishColours[ShortHandColour]

  PieceNames = {"S":"Sarrum", "E":"Eltu", "R":"Redum", "M":"Marzaz pani", "G":"Gisigir", "N":"Nabu", " ":"Space", "K":"Kashshaptu"}
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

def DisplayMainMenu():
  print("{0}".format("Main Menu"))
  print()
  print("1. Play New Game")
  print("2. Load Existing Game")
  print("3. Play Sample Game")
  print("4. View High Scores")
  print("5. Settings")
  print("6. Quit Program")

def GetMainMenuSelection():
  ValidSelection = False
  while not ValidSelection:
    try:
      Selection = int(input("Please choose an option: "))
      if not (0 < Selection <= 6):
        ValidSelection = False
      else:
        ValidSelection = True
        break
    except ValueError:
      ValidSelection = False
    print("That's Invalid")
  return Selection

def MakeSelection(UsersSelection, Scores):
  if UsersSelection == 1: ## Play new game
    PlayGame(False, Scores) ## False (Param 1) means 'don't play the sample game'
  elif UsersSelection == 2: ## Load Existing Game
    ## This is where I'll do the stuff to load an existing game
    ## Ideas of how to do this:
    ##    - list the contents of cwd
    ##    - display all files with the extension that I'm going to use
    ##    - offer them as a menu
    ##    = then use pickle.load to get the contents from them
    ##      - their contents will be a record of a board, number of turns and whose turn it currently is
    ##      - this will be passed to the playgame function
    pass
  elif UsersSelection == 3: ## Play Sample Game
    PlayGame(True, Scores)
  elif UsersSelection == 4: ## View high Scores
    for score in Scores:
        print(score.Name, score.NumberOfTurns, score.Date)
    
    pass
  elif UsersSelection == 5: ## Access Settings
    DisplaySettingsMenu()
    choice = GetUserInputForSettings()
    ActOnUserSettingsChoice(choice)
    
    pass
  elif UsersSelection == 6: ## Quit
    ## Quit the game
    return True
  else:
    print("This isn't a valid menu choice, which shouldn't have gotten to this point")
  return False

def DisplayInGameMenu():
  print()
  print("In-Game Menu")
  print("1. Save Game")
  print("2. Save and Quit")
  print("3. Just Quit")
  print("4. Surrender")
  print()

def GetInGameSelection():
  ValidSelection = False
  while not ValidSelection:
    try:
      Selection = int(input("Please choose an option: "))
      if not (0 < Selection <= 4):
        ValidSelection = False
      else:
        ValidSelection = True
        break
    except ValueError:
      ValidSelection = False
    print("That's Invalid")
  return Selection

def MakeInGameSelection(Board, WhoseTurn, NumberOfTurns, Selection):
  if Selection == 1:
    print("Saving the Game")
  elif Selection == 2:
    print("Saving and quitting the game")
    ## call savegame function
  elif Selection == 3:
    print("Quitting the game")
    return True, False
  elif Selection == 4:
    print("Surrendering")
    return False, True
  else:
    print("I don't know how you've satisified this option")
  return False, False

def DisplaySettingsMenu():
    global KashshaptuEnabled
    print()
    print("Settings")
    print()
    word = "Enable"
    if KashshaptuEnabled:
        word = "Disable"
    print("1. {0} Kashshaptu".format(word))
    print("0. Exit")
    print()

def GetUserInputForSettings():
    ValidSelection = False
    while not ValidSelection:
        try:
            choice = int(input("Please enter your choice: "))
            if -1 < choice <= 1:
                ValidSelection = True
            else:
                print("Invalid Selection")
        except ValueError:
            print("Invalid Selection")
    return choice

def ActOnUserSettingsChoice(choice):
    global KashshaptuEnabled
    if choice == 1:
        word = "Enabled"
        if KashshaptuEnabled:
            word = "Disabled"
        KashshaptuEnabled = not KashshaptuEnabled
        print("Kashshaptu {0}".format(word))

def DisplayWinner(WhoseTurn, isSurrender):
  if WhoseTurn == "W" and not isSurrender:
    print("Black's Sarrum has been captured.  White wins!")
  elif WhoseTurn == "W" and isSurrender:
    print("White has surrendered! Black wins!")
  elif WhoseTurn == "B" and isSurrender:
    print("Black has surrendered! White wins!")
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
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
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
    elif FinishRank == StartRank - 2 and StartRank == 7 and FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
        
  elif ColourOfPiece == "B":
    if FinishRank == StartRank + 1:
       if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
            CheckRedumMoveIsLegal = True
       elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
            CheckRedumMoveIsLegal = True
    elif FinishRank == StartRank + 2 and StartRank == 2 and FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
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
  CheckNabuMoveIsLegal = True
  ## check that the nabu moves diagonally
  print(abs(FinishFile - StartFile),  abs(FinishRank - StartRank))
  if not(abs(FinishFile - StartFile) == abs(FinishRank - StartRank)):
    CheckNabuMoveIsLegal = False
    #return CheckNabuMoveIsLegal ##There's no point in continuing with this if it's not even diagonal
  ## Also we need to check if there is anything between the nabu and it's destination
  print(StartFile, FinishFile)
  for CountFile, CountRank in zip(vrange(StartFile, FinishFile), vrange(StartRank, FinishRank)):
      CheckPiece = Board[CountRank][CountFile]
      if CheckPiece != "  " and ((CountFile != StartFile and CountRank != StartRank) and (CountRank != FinishRank and CountFile != FinishFile)):
          #print(CheckPiece != "  ", (CountFile != StartFile and CountRank != StartRank), (CountRank != FinishRank and CountFile != FinishFile))
          CheckNabuMoveIsLegal = False
  return CheckNabuMoveIsLegal #bool

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  ## can move either vertically or horizontally
  #if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1): (old code)

  if (abs(FinishFile - StartFile) == 1) or (abs(FinishRank - StartRank) == 1):

    #basically says that it can move one square in any direction

    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  ## can move exactly 2 in any direction
  ## does not take into account the fact it cannot jump spaces
  ## forget that
  ## can now move in an L shape, `C# vector2(2,1)`
  ## it can also jump over other peices.
  move_two_y = abs(FinishRank - StartRank) == 2
  move_two_x = abs(FinishFile - StartFile) == 2
  move_one_y = abs(FinishRank - StartRank) == 1
  move_one_x = abs(FinishFile - StartFile) == 1
  ## debug code:
  #print("2x, 2y, 1x, 1y")
  #print(move_two_x, move_two_y, move_one_x, move_one_y)
  ## end of debug code


  move_L_up = move_two_y and move_one_x
  move_L_side = move_two_x and move_one_y

  if move_L_up or move_L_side:
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckKashshaptuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
    KisLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, StartRank, FinishRank, WhoseTurn)
    KisLegal += CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    KisLegal += CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    KisLegal += CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    KisLegal += CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    
    return bool(KisLegal)

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
      elif PieceType == "K":
        MoveIsLegal = CheckKashshaptuMoveIsLegal(Board,StartRank,StartFile,FinishRank,FinishFile, PieceColour)
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
    elif Board[FinishRank -1][FinishFile + 1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank -1][FinishFile - 1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank +1][FinishFile -1] == opponent+"S":
        InCheck = True
    elif Board[FinishRank +1][FinishFile + 1] == opponent+"S":
        InCheck=True

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

def CheckSarrumInCheck(Board, WhoseTurn, Enemy = False):
    BOARDDIMENTION = 8
    if not Enemy:
        WhiteTurn = WhoseTurn == "W"
        if not WhiteTurn:
            opponent = "W"
        else:
            opponent = "B"
    else:
      opponent = WhoseTurn

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

def InitializeSampleBoard(Board):
    ## create a blank board, into an existing list.
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
    Board[3][6] = "WN"
    Board[4][5] = "BR"

def InitializeNewBoard(Board):
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
            if RankNo == 1:
                Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
            elif RankNo == 8:
                Board[RankNo][FileNo] += "S"
            
          elif FileNo == 5:
            if RankNo == 1:
                Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
            elif RankNo == 8:
                Board[RankNo][FileNo] += "M"
            
        else:
          Board[RankNo][FileNo] = "  "    

def InitialiseBoard(Board, SampleGame):
  if SampleGame:
    InitializeSampleBoard(Board)
  else:
    InitializeNewBoard(Board)
   
                    
def GetMove(StartSquare, FinishSquare):
  ## this is going to need validating isn't it?
  Valid = False
  while not Valid:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if StartSquare == -1:
        ## Register Menu Request
        Valid = True
        return 0, 0, True
        print("So why isn't this returning it's stuff")
      elif not (10 < StartSquare < 89):
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
      elif FinishSquare == -1:
        ## Register Menu Request
        return 0, 0, True
      else:
        Valid = True
    except ValueError:
      print("Please enter some valid data")
      
  return StartSquare, FinishSquare, False

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

  Response = input("Enter Y or N\n>>> ").lower()
  while Response not in ["yes", "y", "n", "no"]:
    Response= input("Please enter something valid\n(Enter Y or N)\n>>> ").lower()

  if Response == "y":
    print("Move confirmed")
    return True
  else:
    print("Move cancelled")
    return False
        

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  global KashshaptuEnabled
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    ## White Redum becomes a Marzaz Pani
    if KashshaptuEnabled:
        Board[FinishRank][FinishFile] = "WK"
        KashshaptuEnabled = False ##Only happens once per game
    else:
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

def PlayGame(SampleGame, Scores, PresetBoard = []):
  StartSquare = 0 
  FinishSquare = 0
  if len(PresetBoard) == 0:
    Board = CreateBoard()
    InitialiseBoard(Board, SampleGame)
  else:
    Board = PresetBoard
  
  ## Do you want to play a game?
  WhoseTurn = "W"
  GameOver = False

  ## Keep track of thhe number of turns in the game

  NumberOfTurns = 1

  ## keep going until the fat lady sings
  while not(GameOver):
    StartRank, FinishRank, StartFile, FinishFile = 0, 0, 0, 0
    ## NB: This is effectively the start of the turn, this is where I should impliment the `check` function
    ##      This is also where I shall force the user to continue with the turn until the sarrum is out of check
    ## When value of WhoseTurn is the current user's turn, this function will check if the opposite players
    ## sarrum is in check, so in this instance, the players should not be inverted       
    
    DisplayBoard(Board)
    DisplayWhoseTurnItIs(WhoseTurn)
    MoveIsLegal = False
    IsMenuRequest = False
    while not(MoveIsLegal):
      isSurrendering = False
      isQuitting = False

      StartSquare, FinishSquare, isMenuRequest = GetMove(StartSquare, FinishSquare)
      if not isMenuRequest:
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        ## okay, so rather than dealing with strings, they have chosen to work out which
        ## character is which mathematically
        ## again, not a logical choice? Anyone could just put in any number and break it (unless there's substantial validation)
      
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      else: ## If it is a menu request, show the menu the cycle
        DisplayInGameMenu()
        Choice = GetInGameSelection()
        isQuitting, isSurrendering = MakeInGameSelection(Board, WhoseTurn, NumberOfTurns,Choice)
        if isQuitting:
            print()
            return None
        elif isSurrendering:
            GameOver = True
            break
        else:
            continue

    if not isSurrendering:
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
    isCheck = CheckSarrumInCheck(Board, WhoseTurn)

    MoveConfirm = False

    if not isMenuRequest:
      MoveConfirm = ConfirmMove(StartSquare, FinishSquare, Board)      
      
    if MoveConfirm:
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      
    if isCheck:
      CheckMessage(WhoseTurn)
      
    if GameOver or isSurrendering:
      DisplayWinner(WhoseTurn, isSurrendering)

    ## swap it's now the other player's turn
    if WhoseTurn == "W" and MoveConfirm and not GameOver:
      WhoseTurn = "B"
      NumberOfTurns += 1
    elif WhoseTurn != "W" and MoveConfirm and not GameOver:
      WhoseTurn = "W"
      NumberOfTurns += 1
    ##else (if MoveConfirm is false)
      ## Allow the player to continue their turn

      ## this could be done really easily if the turn was kept track of using a bool - the statement could be `WhoseTurn = (not WhoseTurn)`
  print("Do you want to save this score?")
  choice = ""
  while choice not in ["Y", "N", "YES", "NO"]:
      choice = input("Enter wither [Y]es or [N]o: ").upper()
  if choice[0] == "Y":
      print("Please enter your name:")
      name = ''
      while name == '':
          name = input(">>> ")
      #GET NAME
      #GET DATE
      thisDate = date.strftime(date.today(), "%d/%m/%y")
      #CREATE RECORD FOR THE SCORE
      thisScore = Score(name, NumberOfTurns, thisDate, WhoseTurn)
      #STORE THAT RECORD IN A LIST
      Scores.append(thisScore)

    
if __name__ == "__main__":
  ##Display the menu
  Quit = False
  while not Quit:
    DisplayMainMenu()
    Choice = GetMainMenuSelection()
    Quit = MakeSelection(Choice, Scores)
