main = do
  getLine >>= print . sum . map read . words
