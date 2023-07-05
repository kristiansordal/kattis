main :: IO ()
main = do
  num <- getLine
  let x = read num :: Integer
      ans = (2 ^ x + 1) * (2 ^ x + 1)
  print ans
