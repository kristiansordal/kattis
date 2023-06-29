main = do
  input <- getLine
  mapM_ putStrLn (parseFinal (parseArr input ""))

parseFinal :: [String] -> [String]
parseFinal [] = []
parseFinal [x] = x : parseFinal []
parseFinal (x : y : ys)
  | elem '}' x && elem ',' y = (x ++ ",") : parseFinal ys
  | otherwise = x : parseFinal (y : ys)

parseArr :: String -> String -> [String]
parseArr [] _ = []
parseArr s i
  | head s == '{' = (i ++ [head s]) : parseArr (tail s) (i ++ "  ")
  | head s == '}' = (drop 2 i ++ [head s]) : parseArr (tail s) (drop 2 i)
  | otherwise = (i ++ get s) : parseArr (drop (length (get s)) s) i
  where
    get str = if length s' < length s'' then s' ++ "," else s''
      where
        s' = takeWhile (/= ',') str
        s'' = takeWhile (/= '}') str
