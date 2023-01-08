from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ewdwvi = Factor("ewdwvi", ["bvzbbc", "hlv"])
jnz = Factor("jnz", ["nmdg", "mook"])
pdu = Factor("pdu", ["bvzbbc", "hlv"])
zieg = Factor("zieg", ["nmdg", "mook"])
pqogoq = Factor("pqogoq", ["jhn", "kym"])
jck = Factor("jck", ["dghcps", "sfxk"])
def oyty (zieg, jnz):
    return zieg == jnz
def wnszvu (zieg, jnz):
    return not oyty(zieg, jnz)
sni = Factor("sni", [DerivedLevel("lqrzx", WithinTrial(oyty, [zieg, jnz])), DerivedLevel("kcz", WithinTrial(wnszvu, [zieg, jnz]))])
def zwhy (pdu, ewdwvi):
    return pdu == ewdwvi
def szs (pdu, ewdwvi):
    return not zwhy(pdu, ewdwvi)
fodyo = Factor("fodyo", [DerivedLevel("glom", WithinTrial(zwhy, [pdu, ewdwvi])), DerivedLevel("tnxby", WithinTrial(szs, [pdu, ewdwvi]))])
design=[sni,fodyo,ewdwvi,jnz,pdu,zieg,pqogoq,jck]
constraints=[]
crossing=[jck,fodyo]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_0_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
