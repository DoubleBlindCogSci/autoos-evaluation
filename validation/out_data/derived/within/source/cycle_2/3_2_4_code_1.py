from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oizuh = Factor("oizuh", ["tyyvj","pwv","jjxmu","ayr","mbeusd","qscz"])
phqwn = Factor("phqwn", ["yyn","tkv","atjtz","uvhn","gjbkxc","oan","ktvo","prma"])
def mfi(oizuh, phqwn):
     return oizuh == "ayr"
def wfk(oizuh, phqwn):
     return oizuh != "ayr" and  phqwn == "atjtz"
def kdrnwg(oizuh, phqwn):
     return (not mfi(oizuh, phqwn)) and (not wfk(oizuh, phqwn))
xlitka = DerivedLevel("wqrobh", WithinTrial(mfi, [oizuh, phqwn]))
elguk = DerivedLevel("fozlre", WithinTrial(wfk, [oizuh, phqwn]))
vzdduv = DerivedLevel("tqmxnq", WithinTrial(kdrnwg, [oizuh, phqwn]))
fbdq = Factor("wwxb", [xlitka, elguk, vzdduv])

### EXPERIMENT
design=[oizuh,phqwn,fbdq]
crossing=[fbdq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END