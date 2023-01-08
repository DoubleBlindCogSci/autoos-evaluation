from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ldg= Factor("ldg", ["lpt","gmev","iwrb","rrh","dreekw"])
kjsz= Factor("kjsz", ["lpt","gmev","iwrb","rrh","dreekw"])
anepf= Factor("anepf", ["lpt","gmev","iwrb","rrh","dreekw"])
def is_ofltsk_qzcn(ldg, kjsz, anepf):
    return ldg[0] != anepf[-1] and ldg[-1] == kjsz[0]
def is_ofltsk_bboag(ldg, kjsz, anepf):
    return not is_ofltsk_qzcn(ldg, kjsz, anepf)
ofltsk= Factor("ofltsk", [DerivedLevel("qzcn", Transition(is_ofltsk_qzcn, [ldg, kjsz, anepf])), DerivedLevel("bboag", Transition(is_ofltsk_bboag, [ldg, kjsz, anepf]))])

design=[ldg,kjsz,anepf,ofltsk]
crossing=[ofltsk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
