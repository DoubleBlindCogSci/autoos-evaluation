from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ljajs= Factor("ljajs", ["igja","pmshy","mmqrcq","njjjc","qhhlhv","kgzz","mgg"])
duebpi= Factor("duebpi", ["xvic","dpbx","nxfgd","sgo","gqrrqf","dph","yjo"])
def is_pnlg_vpbr(ljajs, duebpi):
    return ljajs[-1] == "mgg" and duebpi[0] != "dpbx"
def is_pnlg_kwcroh(ljajs, duebpi):
    return ljajs[-1] != "mgg" and duebpi[0] == "dpbx"
def is_pnlg_gtkpx(ljajs, duebpi):
    return ljajs[-1] != "mgg" and duebpi[0] != "dpbx"
pnlg= Factor("pnlg", [DerivedLevel("vpbr", Transition(is_pnlg_vpbr, [ljajs, duebpi])), DerivedLevel("kwcroh", Transition(is_pnlg_kwcroh, [ljajs, duebpi])), DerivedLevel("gtkpx", Transition(is_pnlg_gtkpx, [ljajs, duebpi]))])

design=[ljajs,duebpi,pnlg]
crossing=[pnlg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
