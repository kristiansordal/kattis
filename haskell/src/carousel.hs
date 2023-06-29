{-# OPTIONS_GHC -Wno-missing-signatures #-}
import Control.Monad
main = do
  input <- getLine
  let n = map (read :: String -> Int) (words input)
  print n
  offers <- replicateM (head n) getLine
  let offers' = map words offers
  print offers'

