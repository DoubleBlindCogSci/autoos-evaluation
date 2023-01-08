from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rdt = Factor("rdt", ["umt","dycmaw","eck","jgpw","ekax"])
ilf = Factor("ilf", ["kpc","dgvk","yzyqgn","szym","qhas","nbb","wxky"])
def rjar(rdt, ilf):
    return rdt[-1] != "jgpw" or ilf[-2] != "qhas"
def fndguy(rdt,ilf):
    return not rjar(rdt, ilf)
fra = DerivedLevel("lpvlp", Window(rjar, [rdt, ilf],3,1))
husir = DerivedLevel("uiqx", Window(fndguy, [rdt, ilf],3,1))
ctgwb = Factor("rqjuv", [fra, husir])

### EXPERIMENT
design=[rdt,ilf,ctgwb]
crossing=[ctgwb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END