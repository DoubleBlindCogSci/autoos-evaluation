from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
lvylg = Factor("lvylg", ["atheg", "irduf"])
qlzbh = Factor("qlzbh", ["jstxk", "tlmmco"])
dcoqy = Factor("dcoqy", ["atheg", "irduf"])
zvfx = Factor("zvfx", ["jstxk", "tlmmco"])
vord = Factor("vord", ["qomtek", "lniqwx"])
lnvgik = Factor("lnvgik", ["cbal", "itukx"])
design=[lvylg,qlzbh,dcoqy,zvfx,vord,lnvgik]
constraints=[AtLeastKInARow(3, lvylg)]
crossing=[dcoqy,lvylg]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_0_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_0_1_0.csv"))
nr_regular=6
nr_derived=0
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
