import Control.Monad

main = do
  num <- getLine
  input <- replicateM (head $ map read (words num)) getLine
  let ans = cocktail (map read input) [] (map read (words num))
  putStrLn ans

cocktail :: [Int] -> [Int] -> [Int] -> String
cocktail [] c i
  | 0 `elem` c = "NO"
  | otherwise = "YES"
cocktail (x : xs) c i = cocktail xs (map (\x' -> x' - last i) c ++ [x]) i
