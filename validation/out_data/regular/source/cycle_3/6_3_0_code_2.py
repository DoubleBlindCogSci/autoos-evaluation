from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zmlMNmIsOxRD = Factor("zmlMNmIsOxRD", [Level("o&hqnoGLqDytjX", 1), Level("OdH", 1), Level("VOfxC3Omb%A", 1), Level("jJAN18N", 1), Level("mkG", 1), Level("CwpAf4rQGNA", 1), Level("ZRjSb*9E:n>", 7)])
MSpw_dWsfrsZw = Factor("MSpw(dWsfrsZw", [Level("SSaaahFktKaKIS", 1), Level("MDrEK<QAy", 4), Level("zZH", 1), Level("gWGsXcb", 1), Level("OqxH", 1), Level("db sNZuZI)MwCx", 1)])
_J_b_ = Factor("3J:b[", [Level("qc^7(t^Ulc", 1), Level("TPPZfRaEXs4u", 1), Level("~JZESduWvLrpV3", 8), Level("@gU(mw$tim", 1), Level("4ORsMW", 1), Level("oPDRL", 4)])

design=[zmlMNmIsOxRD,MSpw_dWsfrsZw,_J_b_]
crossing=[zmlMNmIsOxRD,MSpw_dWsfrsZw,_J_b_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_0"))

### END
