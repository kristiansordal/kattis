import Control.Monad
import Data.List

main = do
  l <- replicateM 3 (map (read :: String -> Int) . words <$> getLine)
  print (head $ (l !! 1) \\ (l !! 2))
