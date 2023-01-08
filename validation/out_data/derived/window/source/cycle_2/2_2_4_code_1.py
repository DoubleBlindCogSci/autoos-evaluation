from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
udcne = Factor("udcne", ["hhv","iyh","rncyt","xwfsc","auw","xdiee"])
ayqf = Factor("ayqf", ["sej","avz","dzzaj","rgqja","wqec","byccpl","gnfim"])
def rmjgfq(udcne, ayqf):
    return udcne[-1] == "rncyt" and ayqf[-3] != "rgqja"
def xtloa(udcne,ayqf):
    return not rmjgfq(udcne, ayqf)
xsz = Factor("qdcu", [DerivedLevel("ougyxb", Window(rmjgfq, [udcne, ayqf],4,1)), DerivedLevel("okdoat", Window(xtloa, [udcne, ayqf],4,1))])
### EXPERIMENT
design=[udcne,ayqf,xsz]
crossing=[xsz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END