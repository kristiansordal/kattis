import Control.Monad
import Data.Set (Set)
import Data.Set qualified as Set

main = do
  num <- getLine
  minions <- replicateM (read num) getLine
  let m = map (map read . words) minions :: [[Int]]
  let sets = map Set.fromList m
  print sets

rooms :: [Set Int] -> [Set Int] -> Int
rooms s u = 1
  where
    union = getUnion s (u, [])
    s' = filter (`elem` s) s

getUnion :: [Set Int] -> (Set Int, [Set Int]) -> (Set Int, [Set Int])
getUnion sets s
  | Set.disjoint curr (fst s) = getUnion (tail sets) s
  | otherwise = getUnion (tail sets) (Set.union (fst s) curr, curr : snd s)
  where
    curr = head sets

-- print (rooms m 0)

-- rooms :: [[Int]] -> Int -> Int
-- rooms [] c = c
-- rooms ls c = rooms ls' (c + 1)
--   where
--     curr = head ls
--     ls' = filter (\[x, y] -> x > last curr) (tail ls)
