from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jbbsq = Factor("jbbsq", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
xrdnu = Factor("xrdnu", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
hyvj = Factor("hyvj", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
def sdempl(jbbsq, xrdnu, hyvj):
     return jbbsq == xrdnu
def ovfyo(jbbsq, xrdnu, hyvj):
     return xrdnu != jbbsq and jbbsq == hyvj
def zkzjmn(jbbsq, xrdnu, hyvj):
     return (not jbbsq == xrdnu) and (not jbbsq == hyvj)
kpayf = Factor("wdd", [DerivedLevel("xvgc", WithinTrial(sdempl, [jbbsq, xrdnu, hyvj])), DerivedLevel("yfck", WithinTrial(ovfyo, [jbbsq, xrdnu, hyvj])),DerivedLevel("djnv", WithinTrial(zkzjmn, [jbbsq, xrdnu, hyvj]))])
### EXPERIMENT
design=[jbbsq,xrdnu,hyvj,kpayf]
crossing=[kpayf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END