from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
e_c = Factor("e1c", ["GDJDoHTiO<", "BmBERcRytWF", "TR~OmrjLEscjK", "K@7N_q", "<Pf", "(TJ$KJ9cCjF", "sGLswZAxy", Level("qlKxBtKj", 2)])
DKsJ = Factor("DKsJ", [Level("kWqbHkKZ[!F", 7), "^xRG", Level("~M5i", 1), "Cwa", Level("f DVVjHcThY2hs", 10), Level("2jatR0pLGxmg", 4), "&qp"])
qKX = Factor("qKX", [Level("5gO", 4), "lSmc", Level("0yf8d", 9), "J8W4", Level("rqKuLWd", 8), Level("I<!jFcLxZ", 6)])

design=[e_c,DKsJ,qKX]
crossing=[e_c,DKsJ,qKX]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_1"))

### END
