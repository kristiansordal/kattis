main = do
  input <- getLine
  let n = read input :: Double
  let n' = (read :: String -> Int) input
  print (probability n n')

probability n n' = 1 - ((n - 1) / n) ^ (n' - 1)

p n = (n - 1) / n
