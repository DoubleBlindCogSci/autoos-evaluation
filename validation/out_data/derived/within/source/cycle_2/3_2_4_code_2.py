from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oizuh= Factor("oizuh", ["tyyvj","pwv","jjxmu","ayr","mbeusd","qscz"])
phqwn= Factor("phqwn", ["yyn","tkv","atjtz","uvhn","gjbkxc","oan","ktvo","prma"])
def is_wwxb_wqrobh(oizuh, phqwn):
    return oizuh == "ayr"
def is_wwxb_fozlre(oizuh, phqwn):
    return oizuh != "ayr" and phqwn == "atjtz"
def is_wwxb_tqmxnq(oizuh, phqwn):
    return not (is_wwxb_wqrobh(oizuh, phqwn) or is_wwxb_fozlre(oizuh, phqwn))
wwxb= Factor("wwxb", [DerivedLevel("wqrobh", WithinTrial(is_wwxb_wqrobh, [oizuh, phqwn])), DerivedLevel("fozlre", WithinTrial(is_wwxb_fozlre, [oizuh, phqwn])), DerivedLevel("tqmxnq", WithinTrial(is_wwxb_tqmxnq, [oizuh, phqwn]))])

design=[oizuh,phqwn, wwxb]
crossing=[wwxb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
