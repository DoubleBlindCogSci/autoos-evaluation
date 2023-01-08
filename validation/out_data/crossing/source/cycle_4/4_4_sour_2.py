from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
omna = Factor("omna", ["xcnk", "afm"])
mquu = Factor("mquu", ["luax", "ckyy"])
hobs = Factor("hobs", ["sgnrcf", "vvyre"])
mrk = Factor("mrk", ["ngp", "fgnnd"])
gbvb = Factor("gbvb", ["pvy", "frhkfs"])
czg = Factor("czg", ["jdaxcu", "hhbi"])
rvvgsr = Factor("rvvgsr", ["mfk", "uvuwl"])
jgdf = Factor("jgdf", ["bjvb", "bqkumw"])
nqhyl = Factor("nqhyl", ["qhst", "zujjik"])
constraints = []
crossing = [[omna, mquu], [hobs, mrk, gbvb, czg, rvvgsr, jgdf, nqhyl]]


design=[omna,mquu,hobs,mrk,gbvb,czg,rvvgsr,jgdf,nqhyl]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_4_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_4_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [omna, mquu]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ hobs, mrk, gbvb, czg, rvvgsr, jgdf, nqhyl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
