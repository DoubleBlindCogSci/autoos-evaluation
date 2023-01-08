from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
bpmr = Factor("bpmr", ["vdza", "zew"])
nyoy = Factor("nyoy", ["emszr", "ntatdb"])
dma = Factor("dma", ["vzx", "kmmaw"])
fdl = Factor("fdl", ["xhisah", "vqejbj"])
constraints = []
crossing = [[bpmr, nyoy], [dma, fdl]]


design=[bpmr,nyoy,dma,fdl]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [bpmr, nyoy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ dma, fdl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
