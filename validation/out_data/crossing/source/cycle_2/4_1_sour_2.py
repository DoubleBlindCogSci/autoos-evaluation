from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
jaad = Factor("jaad", ["zdw", "egt"])
izjsng = Factor("izjsng", ["ydv", "nqzuhf"])
dadeg = Factor("dadeg", ["sjn", "nvhy"])
owik = Factor("owik", ["bic", "fys"])
njazq = Factor("njazq", ["wsxtk", "ngaws"])
rtkgin = Factor("rtkgin", ["dvt", "ilyuzp"])
upfqk = Factor("upfqk", ["nvm", "jendlv"])
kbsh = Factor("kbsh", ["kmar", "mqatb"])
ify = Factor("ify", ["wgwuat", "jbexl"])
wwrrg = Factor("wwrrg", ["npx", "qvdrb"])
lgcedy = Factor("lgcedy", ["ubcqfm", "izshjk"])
fcyhmw = Factor("fcyhmw", ["wcr", "rrm"])
iuc = Factor("iuc", ["nmus", "ytk"])
constraints = []
crossing = [[jaad, izjsng], [dadeg, owik, njazq, rtkgin], [upfqk, kbsh, ify], [wwrrg, lgcedy, fcyhmw, iuc]]


design=[jaad,izjsng,dadeg,owik,njazq,rtkgin,upfqk,kbsh,ify,wwrrg,lgcedy,fcyhmw,iuc]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [jaad, izjsng]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ dadeg, owik, njazq, rtkgin]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ upfqk, kbsh, ify]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wwrrg, lgcedy, fcyhmw, iuc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
