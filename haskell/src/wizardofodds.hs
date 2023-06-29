main = do
  input <- getLine
  let [n, k] = map read (words input) :: [Integer]
  if n <= k ^ 2
    then putStrLn "Your wish is granted!"
    else putStrLn "You will become a flying monkey!"
