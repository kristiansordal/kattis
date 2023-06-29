import Control.Monad

main = do
  num <- getLine
  nums <- getLine
  print (length (filter (< 0) (map read (words nums))))
