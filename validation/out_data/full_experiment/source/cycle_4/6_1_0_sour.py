from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
nnoqy = Factor("nnoqy", ["xmqn", "tkhwvj"])
bac = Factor("bac", ["isxjfn", "gmpgkr"])
iopjv = Factor("iopjv", ["xmqn", "tkhwvj"])
lnnq = Factor("lnnq", ["isxjfn", "gmpgkr"])
svbto = Factor("svbto", ["wlmdyb", "adjimh"])
mtro = Factor("mtro", ["hgcxa", "frzn"])
def nhlkq (bac, lnnq):
    return bac == lnnq
def wiqa (bac, lnnq):
    return not nhlkq(bac, lnnq)
ggzo = Factor("ggzo", [DerivedLevel("kzir", WithinTrial(nhlkq, [bac, lnnq])), DerivedLevel("wddk", WithinTrial(wiqa, [bac, lnnq]))])
design=[ggzo,nnoqy,bac,iopjv,lnnq,svbto,mtro]
constraints=[]
crossing=[iopjv,svbto]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
