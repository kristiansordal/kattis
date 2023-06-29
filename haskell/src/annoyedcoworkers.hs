import Control.Monad

main = do
  ch <- getLine
  cw <- map (map (\x -> (st x, y)) . (read :: String -> Int) . words) <$> replicateM (read $ head $ words ch) getLine

  print cw
