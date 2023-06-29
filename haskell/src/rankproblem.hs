import Control.Monad
import Data.Char
import Data.List
import Data.Maybe

main = do
  input <- map (read :: String -> Int) . words <$> getLine
  matches <- replicateM (last input) (map (digitToInt . last) . words <$> getLine)
  let teams = [1 .. (head input)]
  putStrLn (unwords $ map ((\c n -> c : show n) 'T') (finalList teams matches))

finalList :: [Int] -> [[Int]] -> [Int]
finalList = foldl updateList

updateList :: [Int] -> [Int] -> [Int]
updateList rank match
  | posW < posL = rank
  | otherwise =
      let split = splitAt posL rank
          removeL = fst split ++ drop 1 (snd split)
          split' = splitAt posW removeL
          newList = fst split' ++ (l : snd split')
       in newList
  where
    (w, posW) = (head match, fromMaybe 0 (elemIndex (head match) rank))
    (l, posL) = (last match, fromMaybe 0 (elemIndex (last match) rank))
