from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eogjc = Factor("eogjc", ["jgzfq","sbohcz","uzjcr","bytwvi","tflo","ttrmbh","dizicq"])
def is_qyyis_jcndf(eogjc):
    return eogjc[-1] == "tflo" and eogjc[0] != "tflo"
def is_qyyis_chjln(eogjc):
    return eogjc[-1] != "tflo" and eogjc[0] == "dizicq"
def is_qyyis_the(eogjc):
    return not (is_qyyis_jcndf(eogjc) or is_qyyis_chjln(eogjc))
qyyis = Factor("qyyis", [DerivedLevel("jcndf", Window(is_qyyis_jcndf, [eogjc], 2, 1)), DerivedLevel("chjln", Window(is_qyyis_chjln, [eogjc], 2, 1)), DerivedLevel("the", Window(is_qyyis_the, [eogjc], 2, 1))])

design=[eogjc,qyyis]
crossing=[qyyis]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END