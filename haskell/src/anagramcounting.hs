import Combinatorics
import Data.Char
import Data.List

main :: IO ()
main = do
  linesList <- readLines []
  let combos = map getCombos linesList
  mapM_ print combos

getCombos :: String -> Integer
getCombos s = if all isLower s then factorial (fromIntegral $ length s) else fromIntegral $ length $ permutations s

r

eadLines :: [String] -> IO [String]

readLines l = do
  line <- getLine
  if line == ""
    then return l
    else readLines (l ++ [line])
