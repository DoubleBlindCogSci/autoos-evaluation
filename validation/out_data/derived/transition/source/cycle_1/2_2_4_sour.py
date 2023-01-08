from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
rail = Factor("rail", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
hes = Factor("hes", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
kpngck = Factor("kpngck", ["pgvu","ypstjm","sfyvba","aely","oicgle","acjo","swa"])
def kywa(rail, hes, kpngck):
    return rail[0] != hes[-1] or rail[-1] != kpngck[0]
def biofxd(rail, hes, kpngck):
    return not kywa(rail, hes, kpngck)
pghbkq = Factor("nbftir", [DerivedLevel("skb", Transition(kywa, [rail, hes, kpngck])), DerivedLevel("afo", Transition(biofxd, [rail, hes, kpngck]))])
### EXPERIMENT
design=[rail,hes,kpngck,pghbkq]
crossing=[pghbkq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)