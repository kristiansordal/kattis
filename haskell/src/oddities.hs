import Control.Monad

main :: IO ()
main = do
  n <- getLine
  ns <- replicateM (read n) getLine
  let ns' = f $ map (read :: String -> Int) ns
  mapM_ putStrLn ns'

f :: [Int] -> [String]
f [] = []
f (x : xs)
  | even x = (show x ++ " is even") : f xs
  | otherwise = (show x ++ " is odd") : f xs
