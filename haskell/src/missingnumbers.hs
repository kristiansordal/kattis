import Control.Monad

main = do
  num <- getLine
  nums <- map read <$> replicateM (read num) getLine
  let ans = missingNumbers nums [1 ..] []
  case ans of
    Left s -> putStrLn s
    Right n -> mapM_ print n

missingNumbers :: [Int] -> [Int] -> [Int] -> Either String [Int]
missingNumbers [] _ [] = Left "good job"
missingNumbers [] _ m = Right m
missingNumbers (x : xs) (y : ys) m
  | x == y = missingNumbers xs ys m
  | otherwise = missingNumbers (x : xs) ys (m ++ [y])
