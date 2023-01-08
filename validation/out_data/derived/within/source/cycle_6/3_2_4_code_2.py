from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jmhfj = Factor("jmhfj", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
insqbc = Factor("insqbc", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
rrf = Factor("rrf", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
def is_awwa_pltfpx(jmhfj, insqbc, rrf):
    return jmhfj == rrf
def is_awwa_mkb(jmhfj, insqbc, rrf):
    return jmhfj != rrf and jmhfj == insqbc
def is_awwa_ppugl(jmhfj, insqbc, rrf):
    return not (is_awwa_pltfpx(jmhfj, insqbc, rrf) or is_awwa_mkb(jmhfj, insqbc, rrf))
awwa = Factor("awwa", [DerivedLevel("pltfpx", WithinTrial(is_awwa_pltfpx, [jmhfj, insqbc, rrf])), DerivedLevel("mkb", WithinTrial(is_awwa_mkb, [jmhfj, insqbc, rrf])), DerivedLevel("ppugl", WithinTrial(is_awwa_ppugl, [jmhfj, insqbc, rrf]))])

design=[jmhfj,insqbc,rrf,awwa]
crossing=[awwa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END