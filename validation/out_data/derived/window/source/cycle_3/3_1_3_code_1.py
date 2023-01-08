from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
myriv = Factor("myriv", ["rix","czbk","ryyilj","lmmecb","rungn","iex"])
def yuu(myriv):
     return "rix" == myriv[-2] and not myriv[0] == "rix"
def tby(myriv):
     return not "rix" == myriv[-2] and  myriv[0] == "czbk"
def igrk(myriv):
     return (myriv[-2] != "rix") and (not myriv[0] == "czbk")
igqfk = DerivedLevel("tkiu", Window(yuu, [myriv],3,1))
sgx = DerivedLevel("nxmsiz", Window(tby, [myriv],3,1))
etjki = DerivedLevel("nandlu", Window(igrk, [myriv],3,1))
nefg = Factor("jpu", [igqfk, sgx, etjki])

### EXPERIMENT
design=[myriv,nefg]
crossing=[nefg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END