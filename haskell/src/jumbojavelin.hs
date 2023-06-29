import Control.Arrow

main =
  interact $
    lines >>> map (words >>> map read >>> solve >>> show) >>> unlines

solve :: [Integer] -> Integer
-- solve [] = 0
-- solve [x] = 0
solve [a, b] = abs (a - b)
