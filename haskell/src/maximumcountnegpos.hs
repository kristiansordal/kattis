import Data.Function

main = do
  input <- getLine
  let nums = map read (words input) :: [Int]
  print (maxPosNeg nums)

maxPosNeg :: [Int] -> Int
maxPosNeg l = on max length pos neg
  where
    pos = filter (> 0) l
    neg = filter (< 0) l
