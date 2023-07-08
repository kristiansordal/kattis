main :: IO ()
main = do
  str <- getLine
  let x = take (length str) (cycle "PER")
      x' = filter (uncurry (/=)) (zip x str)
  print (length x')
