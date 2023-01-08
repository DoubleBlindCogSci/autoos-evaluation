from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
geo = Factor("geo", ["nifi", "dwc"])
jms = Factor("jms", ["krfi", "cwkx"])
mqhf = Factor("mqhf", ["nifi", "dwc"])
rqqs = Factor("rqqs", ["krfi", "cwkx"])
xocanv = Factor("xocanv", ["poqlbg", "gcr"])
def fubc (mqhf, xocanv):
    return mqhf == xocanv
def aud (mqhf, xocanv):
    return not fubc(mqhf, xocanv)
cvfre = Factor("cvfre", [DerivedLevel("tktwoa", WithinTrial(fubc, [mqhf, xocanv])), DerivedLevel("ljnw", WithinTrial(aud, [mqhf, xocanv]))])
def ahhql (jms, geo):
    return jms == geo
def gkv (jms, geo):
    return not ahhql(jms, geo)
nkd = Factor("nkd", [DerivedLevel("gzzjd", WithinTrial(ahhql, [jms, geo])), DerivedLevel("yan", WithinTrial(gkv, [jms, geo]))])
design=[cvfre,nkd,geo,jms,mqhf,rqqs,xocanv]
constraints=[AtMostKInARow(2, jms),MinimumTrials(25)]
crossing=[mqhf,xocanv]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_2_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
