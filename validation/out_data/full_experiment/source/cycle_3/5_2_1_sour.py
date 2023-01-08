from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ckt = Factor("ckt", ["ypkjl", "yitd"])
smu = Factor("smu", ["xbeqh", "albh"])
psn = Factor("psn", ["ypkjl", "yitd"])
tpk = Factor("tpk", ["xbeqh", "albh"])
eyzwf = Factor("eyzwf", ["oyjyxm", "rsk"])
def fardqu (smu, psn):
    return smu == psn
def tpormi (smu, psn):
    return not fardqu(smu, psn)
erm = Factor("erm", [DerivedLevel("qhb", WithinTrial(fardqu, [smu, psn])), DerivedLevel("hqdkzn", WithinTrial(tpormi, [smu, psn]))])
def cue (eyzwf, tpk):
    return eyzwf == tpk
def kdoxm (eyzwf, tpk):
    return not cue(eyzwf, tpk)
rrlxc = Factor("rrlxc", [DerivedLevel("mpm", WithinTrial(cue, [eyzwf, tpk])), DerivedLevel("gyei", WithinTrial(kdoxm, [eyzwf, tpk]))])
design=[erm,rrlxc,ckt,smu,psn,tpk,eyzwf]
constraints=[ExactlyKInARow(4, tpk)]
crossing=[smu,psn]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
