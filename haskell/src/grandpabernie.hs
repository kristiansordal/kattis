import Control.Monad
import Data.List
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map
import qualified Data.Vector as V

main :: IO ()
main = do
  k <- getLine
  trips <- replicateM (read k) (words <$> getLine)
  q <- getLine
  visits <- replicateM (read q) (words <$> getLine)
  let trips' = Map.fromList (groupTuples (map (\x -> (head x, (read :: String -> Int) (last x))) trips))
      visits' = map (\x -> (head x, (read :: String -> Int) (last x))) visits
      visitOrder = getKthVisit trips' visits'
  mapM_ print visitOrder

getKthVisit :: Map String (V.Vector Int) -> [(String, Int)] -> [Int]
getKthVisit _ [] = []
getKthVisit m (x : xs) = case Map.lookup (fst x) m of
  (Just yrs) -> (yrs V.! (snd x - 1)) : getKthVisit m xs
  Nothing -> []

groupTuples :: (Ord a1, Foldable t, Eq a2) => t (a2, a1) -> [(a2, V.Vector a1)]
groupTuples l =
  let l' = foldr addToGroup [] l
   in map (\(x, y) -> (x, V.fromList (sort y))) l'
  where
    addToGroup (x, y) [] = [(x, [y])]
    addToGroup (x, y) ((x', ys) : xs)
      | x == x' = (x', y : ys) : xs
      | otherwise = (x', ys) : addToGroup (x, y) xs
