from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jbbsq= Factor("jbbsq", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
xrdnu= Factor("xrdnu", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
hyvj= Factor("hyvj", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
def is_wdd_xvgc(jbbsq, xrdnu):
    return jbbsq == xrdnu
def is_wdd_yfck(jbbsq, xrdnu, hyvj):
    return jbbsq == hyvj and jbbsq != xrdnu
def is_wdd_djnv(jbbsq, xrdnu, hyvj):
    return jbbsq != xrdnu and jbbsq != hyvj
wdd= Factor("wdd", [DerivedLevel("xvgc", WithinTrial(is_wdd_xvgc, [jbbsq, xrdnu])), DerivedLevel("yfck", WithinTrial(is_wdd_yfck, [jbbsq, xrdnu, hyvj])), DerivedLevel("djnv", WithinTrial(is_wdd_djnv, [jbbsq, xrdnu, hyvj]))])

design=[jbbsq,xrdnu,hyvj,wdd]
crossing=[wdd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
