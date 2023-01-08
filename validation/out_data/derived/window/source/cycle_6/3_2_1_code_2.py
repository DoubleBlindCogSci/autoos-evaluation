from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mfrme = Factor("mfrme", ["joqydt","mobtn","kzjju","mevtp","crjhjs","wii"])
tnwi = Factor("tnwi", ["bvvwd","rqnix","courr","xwwdvb","kste","idonp"])
def is_xlyjlo_ztgo(mfrme, tnwi):
    return mfrme[0] == "wii" and tnwi[-2] != "kste"
def is_xlyjlo_rqcz(mfrme, tnwi):
    return mfrme[0] != "wii" and tnwi[-2] == "kste"
def is_xlyjlo_qfujr(mfrme, tnwi):
    return not (is_xlyjlo_ztgo(mfrme, tnwi) or is_xlyjlo_rqcz(mfrme, tnwi))
xlyjlo = Factor("xlyjlo", [DerivedLevel("ztgo", Window(is_xlyjlo_ztgo, [mfrme, tnwi], 3, 1)), DerivedLevel("rqcz", Window(is_xlyjlo_rqcz, [mfrme, tnwi], 3, 1)), DerivedLevel("qfujr", Window(is_xlyjlo_qfujr, [mfrme, tnwi], 3, 1))])

design=[mfrme,tnwi,xlyjlo]
crossing=[xlyjlo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END