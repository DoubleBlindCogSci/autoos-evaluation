from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_MJoBcljx = Factor(":MJoBcljx", ["xuqvUI!QNWD", "A1 apR:KOeUU", "BqBe;Uhi0%EyX", "pKeu*C(Hrn", "IG%qtiaBZ", "fBA}urKu", ";chV"])
WTwbv = Factor("WTwbv", ["uECHZECESk", "TCQg", "Z%Lb#6BOZbiQU", "%CWqrBAS*Uhu", "bTDHI", "oirf6Q", "rcSbkSrtNbBB", "Wgqi4{kIhJV1)"])
fj____xg = Factor("fj%}(&xg", [Level("AFgnPVcxla>w", 1), Level("h6JuFbxP<R", 1), Level("qwMx", 1), Level("Kr)XjtrZQhsF>P", 1), Level("v%!So2AT F", 1), Level("BEk ro", 1), Level("^X81XESyrf:bf", 4)])


design=[_MJoBcljx,WTwbv,fj____xg]
crossing=[_MJoBcljx,WTwbv,fj____xg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_0"))

### END
