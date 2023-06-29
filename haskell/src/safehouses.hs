import Control.Monad
import Data.List

main = do
  num <- getLine
  input <- replicateM (read num) getLine
  let spiesAndHouses = findSandH input 0
      spies = map snd $ filter ((== 'S') . fst) spiesAndHouses
      houses = map snd $ filter ((== 'H') . fst) spiesAndHouses
  print (manhattans spies houses)

manhattans :: [(Int, Int)] -> [(Int, Int)] -> Int
manhattans s h = maximum $ map (\x -> minimum (map (manhattan x) h)) s

manhattan :: (Int, Int) -> (Int, Int) -> Int
manhattan (x1, y1) (x2, y2) = abs (x1 - x2) + abs (y1 - y2)

findSandH :: [String] -> Int -> [(Char, (Int, Int))]
findSandH [] _ = []
findSandH (x : xs) y = case l of
  (Just l') -> l' ++ findSandH xs (y + 1)
  Nothing -> findSandH xs (y + 1)
  where
    line s y'
      | null spies && null houses = Nothing
      | otherwise = Just (spies ++ houses)
      where
        spies = map (\x' -> ('S', (x', y'))) (elemIndices 'S' s)
        houses = map (\x' -> ('H', (x', y'))) (elemIndices 'H' s)
    l = line x y
