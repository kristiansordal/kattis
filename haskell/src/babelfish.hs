import System.IO

main = do
  input <- readLines
  print input

readLines :: IO [String]
readLines = do
  eof <- isEOF
  if eof
    then return []
    else do
      line <- getLine
      rest <- readLines
      return (line : rest)
