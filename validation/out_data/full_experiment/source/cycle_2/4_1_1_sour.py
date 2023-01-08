from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
bwiy = Factor("bwiy", ["nkk", "wpgc"])
duutsq = Factor("duutsq", ["kwt", "aovg"])
gjhyl = Factor("gjhyl", ["nkk", "wpgc"])
gkp = Factor("gkp", ["kwt", "aovg"])
def cff (gjhyl, duutsq):
    return gjhyl == duutsq
def xdfkpc (gjhyl, duutsq):
    return not cff(gjhyl, duutsq)
ulbw = Factor("ulbw", [DerivedLevel("ygc", WithinTrial(cff, [gjhyl, duutsq])), DerivedLevel("kuut", WithinTrial(xdfkpc, [gjhyl, duutsq]))])
design=[ulbw,bwiy,duutsq,gjhyl,gkp]
constraints=[AtMostKInARow(4, bwiy)]
crossing=[ulbw,gkp]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_1_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
