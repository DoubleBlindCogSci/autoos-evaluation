from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
wzltf = Factor("wzltf", ["wkh", "jfimzl"])
xkx = Factor("xkx", ["xdmxg", "yrlgcb"])
adasp = Factor("adasp", ["wkh", "jfimzl"])
kbdfej = Factor("kbdfej", ["xdmxg", "yrlgcb"])
def ama (wzltf, kbdfej):
    return wzltf == kbdfej
def bqnj (wzltf, kbdfej):
    return not ama(wzltf, kbdfej)
hwsmo = Factor("hwsmo", [DerivedLevel("mpopni", WithinTrial(ama, [wzltf, kbdfej])), DerivedLevel("wicxmx", WithinTrial(bqnj, [wzltf, kbdfej]))])
def zixeqd (adasp, xkx):
    return adasp == xkx
def mssjx (adasp, xkx):
    return not zixeqd(adasp, xkx)
ejihet = Factor("ejihet", [DerivedLevel("ylb", WithinTrial(zixeqd, [adasp, xkx])), DerivedLevel("fedzj", WithinTrial(mssjx, [adasp, xkx]))])
design=[hwsmo,ejihet,wzltf,xkx,adasp,kbdfej]
constraints=[AtMostKInARow(2, adasp)]
crossing=[ejihet,kbdfej]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
