from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vzweak = Factor("vzweak", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
dsrncz = Factor("dsrncz", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
nwdg = Factor("nwdg", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
def wcmpva(vzweak, dsrncz, nwdg):
     return dsrncz[-1] == vzweak[0] and vzweak[-1] != nwdg[0]
def qgrfup(vzweak, dsrncz, nwdg):
     return dsrncz[-1] != vzweak[0] and vzweak[-1] == nwdg[0]
def dlqf(vzweak, dsrncz, nwdg):
     return (not vzweak[0] == dsrncz[-1]) and (not vzweak[-1] == nwdg[0])
pkptrb = Factor("cij", [DerivedLevel("gkutnp", Transition(wcmpva, [vzweak, dsrncz, nwdg])), DerivedLevel("qpmdhc", Transition(qgrfup, [vzweak, dsrncz, nwdg])),DerivedLevel("ezj", Transition(dlqf, [vzweak, dsrncz, nwdg]))])
### EXPERIMENT
design=[vzweak,dsrncz,nwdg,pkptrb]
crossing=[pkptrb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)