from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jmhfj = Factor("jmhfj", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
insqbc = Factor("insqbc", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
rrf = Factor("rrf", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
def ftmayx(jmhfj, rrf, insqbc):
     return jmhfj == rrf
def oofkb(jmhfj, rrf, insqbc):
     return rrf != jmhfj and jmhfj == insqbc
def ixmvkr(jmhfj, rrf, insqbc):
     return (jmhfj != rrf) and (jmhfj != insqbc)
qwefo = DerivedLevel("pltfpx", WithinTrial(ftmayx, [jmhfj, insqbc, rrf]))
fnv = DerivedLevel("mkb", WithinTrial(oofkb, [jmhfj, insqbc, rrf]))
pampmw = DerivedLevel("ppugl", WithinTrial(ixmvkr, [jmhfj, insqbc, rrf]))
azoirk = Factor("awwa", [qwefo, fnv, pampmw])

### EXPERIMENT
design=[jmhfj,insqbc,rrf,azoirk]
crossing=[azoirk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END