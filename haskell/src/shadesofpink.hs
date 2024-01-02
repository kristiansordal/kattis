import Control.Monad
import Data.Char
import Data.List

main = do
  input <- getLine
  str <- replicateM (read input) getLine
  let ans = findShades str
  if ans == 0 then putStrLn "I must watch Star Wars with my daughter" else print ans

findShades :: [String] -> Int
findShades l = length $ filter (not . null) (map (filter (\x -> x == "rose" || x == "pink")) (filter (\x -> length x >= 4) (map (map (map toLower . take 4) . tails) l)))
