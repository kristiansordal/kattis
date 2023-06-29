import Data.List

main = do
  input <- getLine
  if nub input == input then print 1 else print 0
