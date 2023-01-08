from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
rtbca = Factor("rtbca", ["wdcnuv","weees","tevmvl","loe","csskmf","ibf","tgddbk"])
zxtt = Factor("zxtt", ["wcaqjk","lln","yjdv","zltbig","wlran","kdtqcf","djyl","pub"])
def hkc(rtbca, zxtt):
     return "ibf" == rtbca[-1] and zxtt[0] != "wlran"
def eobbr(rtbca, zxtt):
     return "ibf" != rtbca[-1] and zxtt[0] == "wlran"
def zacjqf(rtbca, zxtt):
     return (not rtbca[-1] == "ibf") and (not eobbr(rtbca, zxtt))
bxhxol = DerivedLevel("hbbs", Transition(hkc, [rtbca, zxtt]))
ehngjl = DerivedLevel("slsizl", Transition(eobbr, [rtbca, zxtt]))
zio = DerivedLevel("swgha", Transition(zacjqf, [rtbca, zxtt]))
cyh = Factor("edud", [bxhxol, ehngjl, zio])

### EXPERIMENT
design=[rtbca,zxtt,cyh]
crossing=[cyh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)