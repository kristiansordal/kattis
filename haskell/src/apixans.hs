import Data.List

main = do
  getLine >>= putStrLn . concatMap nub . group
