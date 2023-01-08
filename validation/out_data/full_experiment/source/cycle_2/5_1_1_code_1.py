from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hcwl = Factor("hcwl", ["yuf", "mso"])
mdvxwl = Factor("mdvxwl", ["ywadjh", "fskl"])
sql = Factor("sql", ["yuf", "mso"])
mjwrx = Factor("mjwrx", ["ywadjh", "fskl"])
iaa = Factor("iaa", ["uqbw", "gwzp"])
def nhjaa (sql, mdvxwl):
    return sql == mdvxwl
def egzf (sql, mdvxwl):
    return not nhjaa(sql, mdvxwl)
uid = Factor("uid", [DerivedLevel("nfp", WithinTrial(nhjaa, [sql, mdvxwl])), DerivedLevel("waj", WithinTrial(egzf, [sql, mdvxwl]))])
design=[uid,hcwl,mdvxwl,sql,mjwrx,iaa]
constraints=[ExactlyKInARow(2, mjwrx)]
crossing=[uid,hcwl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
