import Data.List

main = do
  num <- getLine
  bus <- getLine
  let ans = getShortest (sort (map read (words bus))) ""
  putStrLn ans

getShortest :: [Int] -> String -> String
getShortest [] s = init s
getShortest (x : xs) s
  | length range >= 3 = getShortest (drop (length range - 1) xs) (s ++ show (head range) ++ "-" ++ show (last range) ++ " ")
  | otherwise = getShortest xs ((s ++ show x) ++ " ")
  where
    range = map fst (takeWhile (uncurry (==)) (zip (x : xs) [x ..]))
