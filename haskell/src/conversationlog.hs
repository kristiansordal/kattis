import Control.Monad
import Data.Function
import Data.List.Extra
import Data.Maybe

main = do
  msgCount <- getLine
  m <- replicateM (read msgCount) getLine
  let w = nub $ getWords m
  print w

getWords :: [String] -> [String]
getWords = concatMap (tail . splitOn " ")
