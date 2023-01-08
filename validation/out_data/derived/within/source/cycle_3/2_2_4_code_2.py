from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
efg = Factor("efg", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
ytlne = Factor("ytlne", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
behovz = Factor("behovz", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
def is_qqqtvu_dzas(efg, ytlne, behovz):
    return efg != behovz
def is_qqqtvu_iufvh(efg, ytlne, behovz):
    return not is_qqqtvu_dzas(efg, ytlne, behovz)
qqqtvu= Factor("qqqtvu", [DerivedLevel("dzas", WithinTrial(is_qqqtvu_dzas, [efg, ytlne, behovz])), DerivedLevel("iufvh", WithinTrial(is_qqqtvu_iufvh, [efg, ytlne, behovz]))])

design=[efg,ytlne,behovz,qqqtvu]
crossing=[qqqtvu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
