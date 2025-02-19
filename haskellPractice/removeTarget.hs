main = do
  putStrLn "hey"
data List a = Empty | Entry a (List a)
  deriving (Show)
removeF:: Eq a =>a ->[a] -> [a]
removeF _[] = error"Target not found"
removeF target (x:xs)
    |x == target = xs
    |otherwise   = x:(removeF target xs)
