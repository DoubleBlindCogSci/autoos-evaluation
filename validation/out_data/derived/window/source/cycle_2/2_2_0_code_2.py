from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rdt= Factor("rdt", ["umt","dycmaw","eck","jgpw","ekax"])
ilf= Factor("ilf", ["kpc","dgvk","yzyqgn","szym","qhas","nbb","wxky"])
def is_rqjuv_lpvlp(rdt, ilf):
    return rdt[0] != "jgpw" or ilf[0] != "qhas"
def is_rqjuv_uiqx(rdt, ilf):
    return not is_rqjuv_lpvlp(rdt, ilf)
rqjuv= Factor("rqjuv", [DerivedLevel("lpvlp", Window(is_rqjuv_lpvlp, [rdt, ilf], 3, 1)), DerivedLevel("uiqx", Window(is_rqjuv_uiqx, [rdt, ilf], 3, 1))])

design=[rdt,ilf, rqjuv]
crossing=[rqjuv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
