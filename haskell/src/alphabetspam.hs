import Data.Char
import Data.List
import Numeric

main = do
  input <- getLine
  let upper = genericLength (filter isUpper input) / genericLength input
      lower = genericLength (filter isLower input) / genericLength input
      white = genericLength (filter (== '_') input) / genericLength input
      other = genericLength (filter (\x -> not (isUpper x) && not (isLower x) && x /= '_') input) / genericLength input
  putStrLn (scientificToFloat white)
  putStrLn (scientificToFloat lower)
  putStrLn (scientificToFloat upper)
  putStrLn (scientificToFloat other)

scientificToFloat :: Double -> String
scientificToFloat x = showFFloat Nothing x ""
