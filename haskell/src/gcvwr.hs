main :: IO ()
main = do
  interact solve

solve :: String -> String
solve input =
  let
    ((x:y:z) : xs : _ ) = map (map read . words) $ lines input :: [[Double]]
    result = ((x - y) * 0.9) - sum xs
  in
    show (round result)
