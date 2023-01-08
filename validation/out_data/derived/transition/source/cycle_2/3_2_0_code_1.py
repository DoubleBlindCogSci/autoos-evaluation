from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ljajs = Factor("ljajs", ["igja","pmshy","mmqrcq","njjjc","qhhlhv","kgzz","mgg"])
duebpi = Factor("duebpi", ["xvic","dpbx","nxfgd","sgo","gqrrqf","dph","yjo"])
def lsn(ljajs, duebpi):
     return ljajs[-1] == "mgg" and duebpi[0] != "dpbx"
def rvpsbb(ljajs, duebpi):
     return ljajs[-1] != "mgg" and duebpi[0] == "dpbx"
def qgnnap(ljajs, duebpi):
     return (not lsn(ljajs, duebpi)) and (not rvpsbb(ljajs, duebpi))
tbn = Factor("pnlg", [DerivedLevel("vpbr", Transition(lsn, [ljajs, duebpi])), DerivedLevel("kwcroh", Transition(rvpsbb, [ljajs, duebpi])),DerivedLevel("gtkpx", Transition(qgnnap, [ljajs, duebpi]))])
### EXPERIMENT
design=[ljajs,duebpi,tbn]
crossing=[tbn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END