import Control.Monad

main = do
  num <- getLine
  instr <- replicateM (read num) getLine
  print (volume instr 7)

volume :: [String] -> Int -> Int
volume [] n = n
volume (x : xs) n
  | x == "Skru op!" && n < 10 = volume xs (n + 1)
  | x == "Skru ned!" && n > 0 = volume xs (n - 1)
  | otherwise = volume xs n
