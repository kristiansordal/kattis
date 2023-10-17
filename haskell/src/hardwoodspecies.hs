import Data.List.Extra

main :: IO ()
main = do
  let x = [1, 1, 1, 3, 4, 1, 5, 7, 7]
  print (group x)

-- interact solve

solve :: String -> String
solve s = s

-- process :: [String] -> [(String, String)]
-- process s = map (\x -> (head x, read $ intToDouble (length x) / intToDouble $ length s)) (group s)
