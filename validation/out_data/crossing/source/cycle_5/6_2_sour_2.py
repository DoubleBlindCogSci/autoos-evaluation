from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
mapn = Factor("mapn", ["gatjmi", "pfuvnj"])
svn = Factor("svn", ["fyxdz", "dfcahi"])
rqn = Factor("rqn", ["qera", "enxv"])
dpj = Factor("dpj", ["ejjbvu", "oonq"])
ary = Factor("ary", ["flhsp", "mbofd"])
kfwexi = Factor("kfwexi", ["sht", "wskwx"])
hjaizc = Factor("hjaizc", ["mmssj", "hsqhn"])
qxxcli = Factor("qxxcli", ["vbauw", "ejgz"])
bgio = Factor("bgio", ["uaw", "atrjds"])
jjzp = Factor("jjzp", ["uth", "gzqxlx"])
xirvg = Factor("xirvg", ["qtzscj", "eogupy"])
constraints = []
crossing = [[mapn, svn], [rqn, dpj, ary], [kfwexi, hjaizc, qxxcli], [bgio, jjzp, xirvg]]


design=[mapn,svn,rqn,dpj,ary,kfwexi,hjaizc,qxxcli,bgio,jjzp,xirvg]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [mapn, svn]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ rqn, dpj, ary]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ kfwexi, hjaizc, qxxcli]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ bgio, jjzp, xirvg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
