//Example 1

main =do
  putStrLn "Hello"
lastdigit :: [a] -> a
lastdigit [] = error "Empty"
lastdigit [x] = x
lastdigit (x:xs) = lastdigit xs

//Maximum of a list
main =do
  putStrLn "Hello"
maximum' :: Ord a =>[a] -> a
maximum' [] = error "Empty"
maximum' [x] = x
maximum' (x:xs) 
  |x> tailmax (xs) = x
  |otherwise =  tailmax
  where tailmax = maximum' (xs)

  //reverse
main =do
putStrLn "Hello"
reverseIt :: [a] -> [a]
reverseIt [] = []
reverseIt (x:xs) = (reverseIt xs) ++[x]

//otherone
main =do
putStrLn "Hello"
reverseIt :: [a] -> [a]
reverseIt xs = helper xs []
    where
    helper [] reversed = reversed
    helper (x:xs) reversedSoFar = helper xs (x:reversedSoFar)

//romove all

removeAll :: Eq a =>[a] -> [a]
removeAll target (x:xs)
    |x == target = removeAll target xs
    |otherwise = x:(removeAll target xs)
//
main = do
putStrLn "hey"
removeAll :: Eq a =>a ->[a] -> [a]
removeAll _[] = []
removeAll target (x:xs)
    |x == target = removeAll target xs
    |otherwise   = x:(removeAll target xs)

    
removeF:: Eq a =>a ->[a] -> [a]
removeF _[] = error"Target not found"
removeF target (x:xs)
    |x == target = xs
    |otherwise   = x:(removeF target xs)

main = do
  putStrLn "hey"
data List a = Empty | Entry a (List a)
  deriving (Show)
removeF:: Eq a =>a ->[a] -> [a]
removeF _[] = error"Target not found"
removeF target (x:xs)
    |x == target = xs
    |otherwise   = x:(removeF target xs)


