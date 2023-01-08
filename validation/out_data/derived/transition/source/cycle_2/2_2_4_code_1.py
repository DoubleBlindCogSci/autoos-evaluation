from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ldg = Factor("ldg", ["lpt","gmev","iwrb","rrh","dreekw"])
kjsz = Factor("kjsz", ["lpt","gmev","iwrb","rrh","dreekw"])
anepf = Factor("anepf", ["lpt","gmev","iwrb","rrh","dreekw"])
def dkzi(ldg, anepf, kjsz):
    return ldg[0] != anepf[-1] and ldg[-1] == kjsz[0]
def epachq(ldg, anepf, kjsz):
    return ldg[0] == anepf[-1] or ldg[-1] != kjsz[0]
zbyru = DerivedLevel("qzcn", Transition(dkzi, [ldg, kjsz, anepf]))
jyxav = DerivedLevel("bboag", Transition(epachq, [ldg, kjsz, anepf]))
vjs = Factor("ofltsk", [zbyru, jyxav])

### EXPERIMENT
design=[ldg,kjsz,anepf,vjs]
crossing=[vjs]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END