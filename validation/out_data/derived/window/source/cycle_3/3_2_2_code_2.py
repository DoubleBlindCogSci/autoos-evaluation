from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
inm = Factor("inm", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
qcbti = Factor("qcbti", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
rmwf = Factor("rmwf", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
def is_reyloi_ovxpz(inm, qcbti, rmwf):
    return rmwf[-1] == inm[0] and inm[-1] != qcbti[0]
def is_reyloi_ojx(inm, qcbti, rmwf):
    return rmwf[-1] != inm[0] and qcbti[0] == inm[-1]
def is_reyloi_akwq(inm, qcbti, rmwf):
    return not (is_reyloi_ovxpz(inm, qcbti, rmwf) or is_reyloi_ojx(inm, qcbti, rmwf))
reyloi= Factor("reyloi", [DerivedLevel("ovxpz", Window(is_reyloi_ovxpz, [inm, qcbti, rmwf], 2, 1)), DerivedLevel("ojx", Window(is_reyloi_ojx, [inm, qcbti, rmwf], 2, 1)), DerivedLevel("akwq", Window(is_reyloi_akwq, [inm, qcbti, rmwf], 2, 1))])

design=[inm,qcbti,rmwf,reyloi]
crossing=[reyloi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
