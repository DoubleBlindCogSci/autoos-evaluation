from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
udcne= Factor("udcne", ["hhv","iyh","rncyt","xwfsc","auw","xdiee"])
ayqf= Factor("ayqf", ["sej","avz","dzzaj","rgqja","wqec","byccpl","gnfim"])
def is_qdcu_ougyxb(udcne, ayqf):
    return udcne[-1] == "rncyt" and ayqf[-3] != "rgqja"
def is_qdcu_okdoat(udcne, ayqf):
    return not is_qdcu_ougyxb(udcne, ayqf)
qdcu= Factor("qdcu", [DerivedLevel("ougyxb", Window(is_qdcu_ougyxb, [udcne, ayqf], 4, 1)), DerivedLevel("okdoat", Window(is_qdcu_okdoat, [udcne, ayqf], 4, 1))])

design=[udcne,ayqf,qdcu]
crossing=[qdcu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
