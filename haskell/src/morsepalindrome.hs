{-# OPTIONS_GHC -Wno-type-defaults #-}

import Data.Char
import qualified Data.Map as Map

main = do
  input <- getLine
  let morse = filter (/= ' ') (encodeMorse (map toLower input))
  if morse == reverse morse && not (null morse) then print 1 else print 0

encodeMorse :: String -> String
encodeMorse [] = []
encodeMorse (x : xs) = case Map.lookup x morseCode of
  (Just n) -> n ++ encodeMorse xs
  Nothing -> encodeMorse xs
  where
    morseCode =
      Map.fromList
        [ ('a', ".-"),
          ('b', "-..."),
          ('c', "-.-."),
          ('d', "-.."),
          ('e', "."),
          ('f', "..-."),
          ('g', "--."),
          ('h', "...."),
          ('i', ".."),
          ('j', ".---"),
          ('k', "-.-"),
          ('l', ".-.."),
          ('m', "--"),
          ('n', "-."),
          ('o', "---"),
          ('p', ".--."),
          ('q', "--.-"),
          ('r', ".-."),
          ('s', "..."),
          ('t', "-"),
          ('u', "..-"),
          ('v', "...-"),
          ('w', ".--"),
          ('x', "-..-"),
          ('y', "-.--"),
          ('z', "--.."),
          -- ('=', "-...-"),
          -- ('?', "..--.."),
          -- ('/', "-..-."),
          -- (',', "--..--"),
          -- ('.', ".-.-.-"),
          -- (':', "---..."),
          -- ('\'', ".----."),
          -- ('-', "-....-"),
          -- ('(', "-.--."),
          -- (')', "-.--.-"),
          ('0', "-----"),
          ('1', ".----"),
          ('2', "..---"),
          ('3', "...--"),
          ('4', "....-"),
          ('5', "....."),
          ('6', "-...."),
          ('7', "--..."),
          ('8', "---.."),
          ('9', "----.")
          -- ('@', ".--.-.")
        ]
