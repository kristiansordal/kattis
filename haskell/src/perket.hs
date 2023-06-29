import Control.Monad

main = do
  input <- getLine
  let num = read input :: Int
  nums <- replicateM num getLine
  let sour = map (read . head . words) nums :: [Int]
  let bitter = map (read . last . words) nums :: [Int]
  print (abs (sum bitter - product sour))
