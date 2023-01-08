from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
efg = Factor("efg", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
ytlne = Factor("ytlne", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
behovz = Factor("behovz", ["gjgx","aolb","fkixrn","gzqzlq","vhgp"])
def kaaae(efg, behovz, ytlne):
    return efg != behovz
def nflo(efg, behovz, ytlne):
    return efg == behovz
udn = Factor("qqqtvu", [DerivedLevel("dzas", WithinTrial(kaaae, [efg, ytlne, behovz])), DerivedLevel("iufvh", WithinTrial(nflo, [efg, ytlne, behovz]))])
### EXPERIMENT
design=[efg,ytlne,behovz,udn]
crossing=[udn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END