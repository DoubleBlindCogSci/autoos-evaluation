from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Nu_hsR__QRVyT = Factor("Nu9hsR7)QRVyT", [Level("XKlO:PTn", 1), Level("iI)Jf2", 1), Level("XALFi~H%HMIkby", 1), Level("HVrd6cQVJP", 1), Level("ZxrHgV", 1), Level("ndXyv", 1), Level("?ZBCNvSe", 6), Level("APKM#d", 1), Level("e8PrYt{v%JH *D", 1)])
W_cIisM_FtnMmD = Factor("W!cIisM8FtnMmD", [Level("~BBHICUcD", 7), Level("kScn0s", 1), Level("KypU", 1), Level("<VVbyuZ4or", 6), Level("BAfAY@ct)KUy", 1), Level("ckxe3", 3), Level("BfZFF", 1), Level("ZKiVYkip", 1)])

design=[Nu_hsR__QRVyT,W_cIisM_FtnMmD]
crossing=[Nu_hsR__QRVyT,W_cIisM_FtnMmD]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_1"))

### END
