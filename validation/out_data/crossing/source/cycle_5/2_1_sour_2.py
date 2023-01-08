from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
sxud = Factor("sxud", ["jnd", "ifwp"])
mew = Factor("mew", ["esidn", "lrz"])
zamss = Factor("zamss", ["uskak", "avemq"])
badrp = Factor("badrp", ["ulhdwc", "bieqn"])
bnuavc = Factor("bnuavc", ["wcw", "xocwd"])
constraints = []
crossing = [[sxud, mew], [zamss, badrp, bnuavc]]


design=[sxud,mew,zamss,badrp,bnuavc]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [sxud, mew]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ zamss, badrp, bnuavc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
