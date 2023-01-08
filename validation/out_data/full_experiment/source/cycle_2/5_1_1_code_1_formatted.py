### REGULAR FACTORS
hcwl = Factor("hcwl", ["yuf", "mso"])
mdvxwl = Factor("mdvxwl", ["ywadjh", "fskl"])
sql = Factor("sql", ["yuf", "mso"])
mjwrx = Factor("mjwrx", ["ywadjh", "fskl"])
iaa = Factor("iaa", ["uqbw", "gwzp"])
### DERIVED FACTORS
##
def nhjaa (sql, mdvxwl):
    return sql == mdvxwl
def egzf (sql, mdvxwl):
    return not nhjaa(sql, mdvxwl)
uid = Factor("uid", [DerivedLevel("nfp", WithinTrial(nhjaa, [sql, mdvxwl])), DerivedLevel("waj", WithinTrial(egzf, [sql, mdvxwl]))])
### EXPERIMENT
design=[uid,hcwl,mdvxwl,sql,mjwrx,iaa]
constraints=[ExactlyKInARow(2, mjwrx)]
crossing=[uid,hcwl]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
