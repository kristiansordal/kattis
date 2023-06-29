import Control.Monad
import Data.Fixed
import Data.List

main = do
  num <- getLine
  input <- replicateM (read num) getLine
  let nums = map (map read . tail . words) input :: [[Double]]
      avgs = map overAvg nums

  mapM_ putStrLn avgs

avg :: (Real a, Fractional b) => [a] -> b
avg l = realToFrac (sum l) / genericLength l

overAvg :: [Double] -> String
overAvg l = show (round3dp perc) ++ "%"
  where
    -- overAvg l = if perc `mod'` 10 == 0 then show perc ++ "00%" else show (round3dp perc) ++ "%"
    av = avg l :: Double
    len = genericLength $ filter (> av) l
    perc = len / genericLength l * 100

round3dp :: Double -> Double
round3dp x = fromIntegral (round $ x * 1e3) / 1e3
