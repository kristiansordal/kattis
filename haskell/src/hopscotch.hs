import Control.Monad
import Data.Map (Map)
import qualified Data.Map as Map
import Util

main = do
  input <- parseTwoDigs <$> getLine
  s <- map parseList <$> replicateM (fst input) getLine
  let m = Map.fromList (concat (createMap s 0))
  print input
  print s
  print m

-- move :: Map (Integer, Integer) Integer -> (Integer, Integer) -> Integer -> Integer
-- move m d =

createMap :: [[Integer]] -> Integer -> [[((Integer, Integer), Integer)]]
createMap [] _ = []
createMap (x : xs) y = zip coords x : createMap xs (y + 1)
  where
    coords = zip [0 ..] [y, y ..]

-- manhattans :: [(Integer, Integer)] -> [(Integer, Integer)] -> Integer
-- manhattans s h = minimum $ map (\x -> minimum (map (manhattan x) h)) s

manhattans :: (Integer, Integer) -> [(Integer, Integer)] -> (Integer, (Integer, Integer))
manhattans p m = minimum $ map (`manhattan` p) m
