from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cqM = Factor("cqM", [Level("WZpwSCHq", 1), Level("ImrE]lduw{Qksl", 1), Level("$e&Q", 1), Level("PNeqBHUqsIG", 1), Level("Q<o", 1), Level("cW{Ilk~y~POT", 1), Level("lH;EzXs", 1), Level("nnIiGKcue", 3), Level("vXOuPJKKz", 1)])
cyANfIZJpQOgh_ = Factor("cyANfIZJpQOgh$", [Level("?VIecNgjZ!>", 2), Level("DRD", 1), Level("epr@z:NXTgrVVw", 3), Level("iZiVT", 1), Level("6#mpkRrIqrf", 1), Level("i<vBBQxdFIr", 1), Level("UnCC>jMoA", 1), Level("OqnmMYNff>U", 1), Level("eQ1|T{I^", 1)])
Dkk_DvU_ = Factor("Dkk{DvU^", [Level("JHWoN", 1), Level("rFMlkftlF", 1), Level("wG YzNeGxuJvE", 1), Level("ID?se7vmMz", 1), Level("SVJgykI", 1), Level("5PrE?z jT", 1), Level("Oh<DPIgw", 1), Level("JBGdUQ8LX", 1)])

design=[cqM,cyANfIZJpQOgh_,Dkk_DvU_]
crossing=[cqM,cyANfIZJpQOgh_,Dkk_DvU_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_1"))

### END
