from sweetpea import *
import os
_dir=os.path.dirname(__file__)
omna = Factor("omna", ["xcnk", "afm"])
mquu = Factor("mquu", ["luax", "ckyy"])
hobs = Factor("hobs", ["sgnrcf", "vvyre"])
mrk = Factor("mrk", ["ngp", "fgnnd"])
gbvb = Factor("gbvb", ["pvy", "frhkfs"])
czg = Factor("czg", ["jdaxcu", "hhbi"])
rvvgsr = Factor("rvvgsr", ["mfk", "uvuwl"])
jgdf = Factor("jgdf", ["bjvb", "bqkumw"])
nqhyl = Factor("nqhyl", ["qhst", "zujjik"])
constraints = []
crossing = [[omna, mquu], [hobs, mrk, gbvb, czg, rvvgsr, jgdf, nqhyl]]


design=[omna,mquu,hobs,mrk,gbvb,czg,rvvgsr,jgdf,nqhyl]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_4"))

### END