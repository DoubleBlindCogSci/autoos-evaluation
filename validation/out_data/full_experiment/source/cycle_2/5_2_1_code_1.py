from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hbqz = Factor("hbqz", ["zdmblf", "shmy"])
ryk = Factor("ryk", ["quezyq", "xxciv"])
foohw = Factor("foohw", ["zdmblf", "shmy"])
cduyr = Factor("cduyr", ["quezyq", "xxciv"])
mij = Factor("mij", ["lpy", "grlbm"])
def pqtfru (hbqz, foohw):
    return hbqz == foohw
def obd (hbqz, foohw):
    return not pqtfru(hbqz, foohw)
xflnlc = Factor("xflnlc", [DerivedLevel("ydbchl", WithinTrial(pqtfru, [hbqz, foohw])), DerivedLevel("yiu", WithinTrial(obd, [hbqz, foohw]))])
def xzvmu (cduyr, mij):
    return cduyr == mij
def ozo (cduyr, mij):
    return not xzvmu(cduyr, mij)
zoyn = Factor("zoyn", [DerivedLevel("lsolqn", WithinTrial(xzvmu, [cduyr, mij])), DerivedLevel("una", WithinTrial(ozo, [cduyr, mij]))])
design=[xflnlc,zoyn,hbqz,ryk,foohw,cduyr,mij]
constraints=[AtLeastKInARow(4, cduyr)]
crossing=[zoyn,hbqz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
