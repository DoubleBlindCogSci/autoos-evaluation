from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iiyrcc = Factor("iiyrcc", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
tevaa = Factor("tevaa", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
uabdyq = Factor("uabdyq", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
def is_ibv_ivi(iiyrcc, tevaa, uabdyq):
    return tevaa == iiyrcc
def is_ibv_cbi(iiyrcc, tevaa, uabdyq):
    return tevaa != iiyrcc and uabdyq == iiyrcc
def is_ibv_nncbtr(iiyrcc, tevaa, uabdyq):
    return not (is_ibv_ivi(iiyrcc, tevaa, uabdyq) or is_ibv_cbi(iiyrcc, tevaa, uabdyq))
ibv= Factor("ibv", [DerivedLevel("ivi", WithinTrial(is_ibv_ivi, [iiyrcc, tevaa, uabdyq])), DerivedLevel("cbi", WithinTrial(is_ibv_cbi, [iiyrcc, tevaa, uabdyq])), DerivedLevel("nncbtr", WithinTrial(is_ibv_nncbtr, [iiyrcc, tevaa, uabdyq]))])

design=[iiyrcc,tevaa,uabdyq,ibv]
crossing=[ibv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
