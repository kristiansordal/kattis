import Control.Monad
import System.Random

main = do
  num <- getLine
  let num' = read num :: Int
  dishes <- replicateM num' getLine
  rand <- randomRIO (0, num' - 1)
  mapM_ putStrLn (words $ dishes !! rand)
