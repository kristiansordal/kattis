import Text.Regex

main = do
  input <- getLine
  let ans = getDigits input
  print (length ans)

getDigits :: String -> [Int]
getDigits s =
  concatMap (\x -> if '-' `elem` x then [read (takeWhile (/= '-') x) .. read (drop 1 (dropWhile (/= '-') x))] else [read x]) (splitRegex (mkRegex ";") s)
