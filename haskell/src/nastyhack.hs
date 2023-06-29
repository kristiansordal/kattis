import Control.Monad

main = do
  input <- getLine
  intList <- replicateM (read input) (map (read :: String -> Int) . words <$> getLine)
  mapM_ (putStrLn . advertise) intList

advertise :: [Int] -> String
advertise l
  | head (init l) - (l !! 1 - last l) > 0 = "do not advertise"
  | head (init l) - (l !! 1 - last l) < 0 = "advertise"
  | otherwise = "does not matter"
