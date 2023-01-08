from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IIAvEBEBnZqhA= Factor("IIAvEBEBnZqhA", ["yNQKZrsUXCMb4h", '<MS9A", "bu5}iwBG)mu"])
dCU__hdNP_W__x= Factor("dCU%3hdNP>W?#x", ["HK4LftZdK", '@BZZomKQ', 'CDAjJy|veKYfMF'])
oeAtWT= Factor("oeAtWT", [Level("ntz", 10), Level("Ptbb", 8), Level("8Ml", 1)])

design=[IIAvEBEBnZqhA,dCU__hdNP_W__x,oeAtWT]
crossing=[IIAvEBEBnZqhA,dCU__hdNP_W__x,oeAtWT]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_3_0"))

### END
