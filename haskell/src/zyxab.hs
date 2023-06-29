import Control.Monad
import Data.Function
import Data.List
import Data.Maybe

main = do
  input <- getLine
  names <- replicateM (read input) getLine
  let potNames = sortBy (compare `on` length) $ filter (\x -> length x >= 5 && nub x == x) names
      shortNames = filter (\x -> length x == length (head potNames)) potNames
      name = sortBy compareTup (zip shortNames (map strToInt shortNames))
  if null potNames then putStrLn "neibb!" else putStrLn (fst $ head name)

strToInt = sum . mapMaybe (\x -> lookup x (zip ['a' .. 'z'] [1 .. 26]))

compareTup (a1, b1) (a2, b2) = compare b2 b1
