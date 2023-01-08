from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
hbqz = Factor("hbqz", ["zdmblf", "shmy"])
ryk = Factor("ryk", ["quezyq", "xxciv"])
foohw = Factor("foohw", ["zdmblf", "shmy"])
cduyr = Factor("cduyr", ["quezyq", "xxciv"])
mij = Factor("mij", ["lpy", "grlbm"])
def is_xflnlc_ydbchl(hbqz, foohw):
    return hbqz == foohw
def is_xflnlc_yiu(hbqz, foohw):
    return not is_xflnlc_ydbchl(hbqz, foohw)
xflnlc= Factor("xflnlc", [DerivedLevel("ydbchl", WithinTrial(is_xflnlc_ydbchl, [hbqz, foohw])), DerivedLevel("yiu", WithinTrial(is_xflnlc_yiu, [hbqz, foohw]))])
def is_zoyn_lsolqn(cduyr, mij):
    return cduyr == mij
def is_zoyn_una(cduyr, mij):
    return not is_zoyn_lsolqn(cduyr, mij)
zoyn= Factor("zoyn", [DerivedLevel("lsolqn", WithinTrial(is_zoyn_lsolqn, [cduyr, mij])), DerivedLevel("una", WithinTrial(is_zoyn_una, [cduyr, mij]))])
constraints = [AtLeastKInARow(4, (xflnlc, "ydbchl"))]
crossing = [zoyn, hbqz]

design=[hbqz,ryk,foohw,cduyr,mij,xflnlc,zoyn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))
