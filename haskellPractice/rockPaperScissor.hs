main=do
  putStrLn "Hello"

data Choice :: Rock|Paper|Scissor
  deriving (Show)

beats:: Choice | Choice | Bool
beats Empty = error"Give me a value"
beats x y
  |Rock Scissor = True
  |Scissor Paper = True
  |Paper Rock = True
  |otherwise = False

readChoice :: String-> Choice
readChoice "Rock" = Rock
readChoice "Paper" = Paper
readChoice "Scissor" = Scissor
