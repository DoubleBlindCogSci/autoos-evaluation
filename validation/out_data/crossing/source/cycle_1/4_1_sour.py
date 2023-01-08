from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
kxma = Factor("kxma", ["nozq", "adiacv"])
uhy = Factor("uhy", ["dafua", "nwvyg"])
gsvtjw = Factor("gsvtjw", ["ifvlbq", "aoyhnl"])
prkinm = Factor("prkinm", ["wvby", "rixgcr"])
rzqvop = Factor("rzqvop", ["ownoyx", "jeammm"])
wfrq = Factor("wfrq", ["qwdiz", "kfsmw"])
htgxg = Factor("htgxg", ["jwiv", "edvpcb"])
ktkj = Factor("ktkj", ["lyc", "afc"])
pmtqn = Factor("pmtqn", ["hkjjoz", "abgrj"])
buriha = Factor("buriha", ["engbyt", "xbhzun"])
rdsfc = Factor("rdsfc", ["dgt", "pof"])

### EXPERIMENT
design=[kxma,uhy,gsvtjw,prkinm,rzqvop,wfrq,htgxg,ktkj,pmtqn,buriha,rdsfc]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_0.csv"))
nr_crossings=4
nr_factors=11
p_code_1 = 0
p_code_2 = 0
crossing = [kxma,uhy,gsvtjw,prkinm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rzqvop]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [wfrq,htgxg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ktkj,pmtqn,buriha,rdsfc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
