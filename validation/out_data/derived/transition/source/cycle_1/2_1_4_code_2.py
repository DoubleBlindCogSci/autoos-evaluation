from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
szaa= Factor("szaa", ["gcjifk","bhghwo","mqa","ziyrmo","wsnxr","wea"])
def is_npswlj_tmgjgv(szaa):
    return szaa[0] == "wea" and szaa[-1] == "ziyrmo"
def is_npswlj_ttx(szaa):
    return not is_npswlj_tmgjgv(szaa)
npswlj= Factor("npswlj", [DerivedLevel("tmgjgv", Transition(is_npswlj_tmgjgv, [szaa])), DerivedLevel("ttx", Transition(is_npswlj_ttx, [szaa]))])

design=[szaa,npswlj]
crossing=[npswlj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
