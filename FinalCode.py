from datetime import datetime
now = datetime.now()
import warnings 
warnings.filterwarnings('ignore')
# -*- coding: utf-8 -*-
from clean import *
import re
import pandas as pd
def shuffle(x):
    x = x.split()
    x.sort()
    r = ' '.join(x)
    return r

#%%
print("Loading files")
SM = (pd.read_csv('SM.csv',encoding='latin1'))
SM = SM.drop_duplicates()#drops all duplicates from SM
OneMg = (pd.read_csv('OneMg.csv',encoding="latin1"))
OneMg = OneMg.drop_duplicates() #drops all duplicates from OneMg
#%%

# =============================================================================
# SYRUP vs. SYP in SM
# INJECTION  vs. INJ in SM
# CAPSULE vs. CAPS in SM
# SUSPENSION vs. SUSP in SM
# INHALER vs. INHAL in SM
# LIQUID same
# GEL SAME
# CREAM same
# SOAP same
# solution same
# DROPS
# TABLETS vs. C. TABS or C.TABS
# MG

# =============================================================================
#%%

SM["Cat"] = ""
for i in range(0,len(SM)):
    if (len(re.findall(r'\bdrops\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bdrop\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "DROPS"
    elif "cream" in str(SM["SM"].iloc[i]).lower():
        SM["Cat"].iloc[i] = "CREAM"
    elif (len(re.findall(r'\bgel\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "GEL"
    elif (len(re.findall(r'\btablets\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btablet\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btab\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btabs\b',str(SM["SM"].iloc[i]).lower()))!=0) or ("enter.c." in str(SM["SM"].iloc[i]).lower()) or ("enter c." in str(SM["SM"].iloc[i]).lower()) or ("uncoa." in str(SM["SM"].iloc[i]).lower()) or ("f.c.ops" in str(SM["SM"].iloc[i]).lower()) or ("fil.c.bilaye" in str(SM["SM"].iloc[i]).lower()) or  ("ent.f.c.tabs" in str(SM["SM"].iloc[i]).lower()) or ("c. tabs" in str(SM["SM"].iloc[i]).lower()) or ("c.tabs" in str(SM["SM"].iloc[i]).lower()) or ("tab" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "TABLETS"        
    elif ("soap" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "SOAP"
    elif ("inhal" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "INHALER"
    elif ("susp" in str(SM["SM"].iloc[i]).lower()) or (len(re.findall(r'\bsuspension\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "SUSUSPENSION"
    elif (len(re.findall(r'\binj\b',str(SM["SM"].iloc[i]).lower()))!=0) or ("prefill.syr." in str(SM["SM"].iloc[i]).lower()) or (len(re.findall(r'\bINJ\b',str(SM["SM"].iloc[i]).lower()))!=0) or ("vial" in str(SM["SM"].iloc[i]).lower()) or ("inj lyo vial" in str(SM["SM"].iloc[i]).lower()) or ("infus vial" in str(SM["SM"].iloc[i]).lower()) or ("vial" in str(SM["SM"].iloc[i]).lower()) or ("vial dry+sol" in str(SM["SM"].iloc[i]).lower()) or ("inj dry vial" in str(SM["SM"].iloc[i]).lower()) or ("injectable" in str(SM["SM"].iloc[i]).lower()) or ("inject." in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "INJECTION"
    elif ("liquid" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "LIQUID"
    elif (len(re.findall(r'\bcaps\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bcap\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "CAPSULES"
    elif ("syr." in str(SM["SM"].iloc[i]).lower()) or ("syp" in str(SM["SM"].iloc[i]).lower()) or ("syrup" in str(SM["SM"].iloc[i]).lower()) or (len(re.findall(r'\bsyr\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "SYRUP"
    elif ("infus" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "INFUSION"
    elif ("lotion" in str(SM["SM"].iloc[i]).lower()) or ("lot." in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "LOTION"
    elif ("shampoo" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "SHAMPOO"
    elif ("powder" in str(SM["SM"].iloc[i]).lower()) or ("powd." in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "POWDER"
    elif (len(re.findall(r'\bsolut\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bsolution\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "SOLUTION"
    elif ("spray" in str(SM["SM"].iloc[i]).lower()):
        SM["Cat"].iloc[i] = "SPRAY"
    elif (len(re.findall(r'\boil\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "OIL"
    elif (len(re.findall(r'\bointment\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "OINTMENT"
    elif (len(re.findall(r'\bsachet\b',str(SM["SM"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bsachets\b',str(SM["SM"].iloc[i]).lower()))!=0):
        SM["Cat"].iloc[i] = "SACHETS"
    else:
        SM["Cat"].iloc[i] = "EMPTY"
        
    #print(i)
SM["Cat"].value_counts().reset_index()

SM.to_csv('Cat_SM.csv')
        
print("Categorising SM items completed")     
#%%

print("Categorising OneMg items ### started")
OneMg["Cat"] = ""
for i in range(0,len(OneMg)):
    if ("drops" in str(OneMg["OneMg"].iloc[i]).lower()) or ("drop" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "DROPS"
    elif "cream" in str(OneMg["OneMg"].iloc[i]).lower():
        OneMg["Cat"].iloc[i] = "CREAM"
    elif (len(re.findall(r'\bgel\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0):
        OneMg["Cat"].iloc[i] = "GEL"
    elif (len(re.findall(r'\btablet\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btablets\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btabs\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\btab\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or ("tablet" in str(OneMg["OneMg"].iloc[i]).lower()) or ("tablet." in str(OneMg["OneMg"].iloc[i]).lower()) or ("tablets" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "TABLETS"        
    elif ("soap" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "SOAP"
    elif ("inhal" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "INHALER"
    elif ("susp" in str(OneMg["OneMg"].iloc[i]).lower()) or (len(re.findall(r'\bsuspension\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0):
        OneMg["Cat"].iloc[i] = "SUSUSPENSION"
    elif ("inj" in str(OneMg["OneMg"].iloc[i]).lower()) or ("vial" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "INJECTION"
    elif ("liquid" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "LIQUID"
    elif (len(re.findall(r'\bcaps\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bcap\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0):
        OneMg["Cat"].iloc[i] = "CAPSULES"
    elif (len(re.findall(r'\bsyr\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or  (len(re.findall(r'\bsyp\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or ("syrup" in str(OneMg["OneMg"].iloc[i]).lower()) or ("syr." in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "SYRUP"
    elif ("infus" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "INFUSION"
    elif ("lotion" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "LOTION"
    elif ("shampoo" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "SHAMPOO"
    elif ("powder" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "POWDER"
    elif (len(re.findall(r'\bsolut\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bsolution\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0):
        OneMg["Cat"].iloc[i] = "SOLUTION"
    elif ("spray" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "SPRAY"
    elif ("oil" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "OIL"
    elif ("ointment" in str(OneMg["OneMg"].iloc[i]).lower()):
        OneMg["Cat"].iloc[i] = "OINTMENT"
    elif (len(re.findall(r'\bsachet\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0) or (len(re.findall(r'\bsachets\b',str(OneMg["OneMg"].iloc[i]).lower()))!=0):
        OneMg["Cat"].iloc[i] = "SACHETS"
    else:
        OneMg["Cat"].iloc[i] = "EMPTY"
        
        
    #print(i)
OneMg["Cat"].value_counts().reset_index()

OneMg.to_csv('Cat_OneMg.csv')

print("Categorising OneMg items ## completed")
#%%
# =============================================================================
# #MAIN functions to merge Capsules and Tablets
# =============================================================================
import pandas as pd
import re

print("Replacing garbage text from items")
tab1= "DOLO 650 MG"
tab1.split()
tab2 = "650 MG DOLO"

def shuffle(x):
    x = x.split()
    x.sort()
    r = ' '.join(x)
    return r


df = pd.read_csv("Cat_OneMg.csv",encoding='latin1')

sm_df = pd.read_csv("Cat_SM.csv",encoding='latin1')



one_tab = df[df.Cat=="TABLETS"]
one_capsu = df[df.Cat=="CAPSULES"]
one_capsu["Cat"] = "TABLETS"
one_tabs = pd.concat([one_tab,one_capsu])

sm_tab = sm_df[sm_df.Cat=="TABLETS"]
sm_capsu = sm_df[sm_df.Cat=="CAPSULES"]
sm_capsu["Cat"] = "TABLETS"
sm_tabs = pd.concat([sm_tab,sm_capsu])


#one_tabs = df[df.Cat=="TABLETS"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)
one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("TABLETS",""))

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("COMBIPACK",""))
sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("COMBIPACK",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("TABLET",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TABS",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("FILM C.TABS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("UNCOATED",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DISPERS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.BILAYE",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("F.C.OPS",""))

sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TABS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TAB",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("F.C.",""))

sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("COATED",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM C.S",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TAB.ER",""))    
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM C.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("   "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SR",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TAB UNCOATED",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub('[/]', ' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub('[/]', ' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub('TABS', '', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TAB",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("UNCOA.FT",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("UNCOA.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENTER C.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENTER.C.",""))



sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CAPLETS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CAPS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CAPSULES",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CAPSULE",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("BILAYER",""))


sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace(" )",""))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('[/]', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('TABS', '', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('UNCOATED', '', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('COATED', '', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('DT', '', x))

one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('TAB', '', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('SR', '', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("CAPSULES",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("CAPSULE",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("FIL.C..OD",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C..OD",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C..DS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("C. FIL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENT.C.TAB",""))

sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C..MR",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C..ER",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.TAB.MR",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.TAB.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM.C.",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("(DCA)N",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("(DCA)",""))

for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bAMP\b','',str(sm_tabs['UK'].iloc[r]))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip()) 


def removeTrash(x):
    x = x.split()
    try:
        x.remove("Y")
        y = ' '.join(x)
    except:
        x = x.split()
        y = ' '.join(x)
    try:
        x.remove("G")
        y = ' '.join(x)
    except:
        x = x.split()
        y = ' '.join(x)        
    return y


def removeEtc(x):
    x = x.split()
    try:
        x.remove("XR")
        y = ' '.join(x)
    except:
        x = x.split()
        y = ' '.join(x)
    return y
    
for r in range (0, len(sm_tabs['UK'])):
    try:
        sm_tabs['UK'].iloc[r] = removeTrash(sm_tabs['UK'].iloc[r])
        print("y")
    except:
        pass
    try:
        sm_tabs['UK'].iloc[r] = removeEtc(sm_tabs['UK'].iloc[r])
        print("==")
    except:
        pass

sm_tabs["UKm"]  = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    
    merge_tablets = pd.merge(one_tabs, sm_tabs,on="UKm",how="left")
    merge_tablets['SKU'].count()
except:
    merge_tablets = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})

#%%
print("Category wise removal of garbage")
#INjection Mapping
import re
one_tabs = df[df.Cat=="INJECTION"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)
one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("INJECTIONS",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INJECTION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INJ",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("VIAL",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))



one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("(DCA)N",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("(DCA)",""))

sm_tabs = sm_df[sm_df.Cat=="INJECTION"]
sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("INJECTIONS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJECTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJ",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("(1 VIAL)",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("COMB PCK",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("COMBIPACK",""))



sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJ DRY VIAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("VIAL DRY+SOL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJ VIAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INFUS VIAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJ LYO VIAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJECTABLE",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJECT.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("VIAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MCG",""))


one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_caps = pd.merge(one_tabs, sm_tabs,on="UKm",how="left")
    merge_caps.to_csv("inj_mapped.csv")
    merge_caps['SKU'].count()
except:
    merge_caps = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})


#%%
## creams mapping
one_tabs = df[df.Cat=="CREAM"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)
sm_tabs = sm_df[sm_df.Cat=="CREAM"]


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("CREAMS",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("CREAM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("CREAMS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CREAM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


def shuffle(x):
    try:
        x = x.split()
        x.sort()
        r = ' '.join(x)
        return r        
    except:
        pass

def removeGm(x):
    x = x.split()
    try:
        x.remove("GM")
        y = ' '.join(x)
    except:
        x = x.split()
        y = ' '.join(x)
def removeGms(x):
    x = x.split()
    try:
        x.remove("GM")
        y = ' '.join(x)
    except:
        x = x.split()
        y = ' '.join(x)        
    return y
for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))

for r in range (0, len(sm_tabs['UK'])):
    try:
        sm_tabs['UK'].iloc[r] = removeGm(sm_tabs['UK'].iloc[r])
        sm_tabs['UK'].iloc[r] = removeGms(sm_tabs['UK'].iloc[r])        
        print("y")
    except:
        pass
sm_tabs["UKm"] = ""    
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_cream = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_cream['SKU'].count()
except:
    merge_cream = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
#liquid and solutions mapping
one_tab = df[df.Cat=="LIQUID"]
one_capsu = df[df.Cat=="SOLUTION"]
one_capsu["Cat"] = "LIQUID"
one_tabs = pd.concat([one_tab,one_capsu])
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="LIQUID"]
sm_capsu = sm_df[sm_df.Cat=="SOLUTION"]
sm_capsu["Cat"] = "LIQUID"
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("LIQUID",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("LIQUID",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))

sm_tabs["UKm"]  = ""
one_tabs["UKm"]  = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_liquid = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_liquid['SKU'].count()
except:
    merge_liquid = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})

#%%
# GEL mapping
one_tabs = df[df.Cat=="GEL"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="GEL"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("LIQUID",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("LIQUID",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))

sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_gel = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_gel['SKU'].count()
except:
    merge_gel = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
# DROPS mappnig
one_tabs = df[df.Cat=="DROPS"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="DROPS"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("DROPS",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("DROP",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("DROPS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DROP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_drops = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_drops['SKU'].count()
except:
    merge_drops = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
#syrups
one_tabs = df[df.Cat=="SYRUP"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="SYRUP"]


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SYRUP",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SYP",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SYRUP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SYP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("PREFILL.SYR.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("PREFILL.SYR",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("PREFILL",""))


sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))

sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())

sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_syrup = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_syrup['SKU'].count()
except:
    merge_syrup = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
#SUSUSPENSION
one_tabs = df[df.Cat=="SUSUSPENSION"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="SUSUSPENSION"]


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SUSUSPENSION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSPENSION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("DRY",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SUSPENSION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DRY",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))

one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_susp = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_susp['SKU'].count()
except:
    merge_susp = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
#SHAMPOO
one_tabs = df[df.Cat=="SHAMPOO"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="SHAMPOO"]

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SHAMPOO",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SHAMPOO",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())

sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_shampoo = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_shampoo['SKU'].count()    
except:
    merge_shampoo = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
#%%
#POWDER
one_tabs = df[df.Cat=="POWDER"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="POWDER"]


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("POWDER",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("POWDER",""))
sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("POWD.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_powder = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_powder['SKU'].count()
except:   
    merge_powder = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})

#%%
#SPRAY
one_tabs = df[df.Cat=="SPRAY"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="SPRAY"]


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SPRAY",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SPRAY",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_SPRAY = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_SPRAY['SKU'].count()
except:
    merge_SPRAY = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})

#%%
#OIl
one_tabs = df[df.Cat=="OIL"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tabs = sm_df[sm_df.Cat=="OIL"]
one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("OIL",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("OIL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_OIL = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_OIL['SKU'].count()
except:
    merge_OIL = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass

#%%
#ointment
one_tabs = df[df.Cat=="OINTMENT"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="OINTMENT"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("OINTMENT",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("OINT",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("OINTMENT",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("OINT",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_OINT = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_OINT['SKU'].count()
except:
    merge_OINT = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass

#%%
#sachet
one_tabs = df[df.Cat=="SACHET"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="SACHET"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SACHETS",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SACHET",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

for r in range (0, len(one_tabs['UK'])):
    one_tabs['UK'].iloc[r]  = re.sub(r'\bGM\b','',str(one_tabs['UK'].iloc[r]))
    one_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(one_tabs['UK'].iloc[r]))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SACHETS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SACHET",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bGM\b','',str(sm_tabs['UK'].iloc[r]))
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_SACHET = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_SACHET['SKU'].count()
except:
    merge_SACHET = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass
#%%
#INHALER
one_tabs = df[df.Cat=="INHALER"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="INHALER"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("INHALER",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHALE",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHAL",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHAL.",""))

one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("INHALER",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INAHLE",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INHAL",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INHAL.",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_INHAL = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_INHAL['SKU'].count()
except:
    merge_INHAL = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass

#%%
#soap
#INHALER
one_tabs = df[df.Cat=="SOAP"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)

sm_tab = sm_df[sm_df.Cat=="SOAP"]
sm_tabs = pd.concat([sm_tab,sm_capsu])

one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("SOAPS",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOAP",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("SOAPS",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOAP",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())


for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_soap = pd.merge(one_tabs,sm_tabs,on="UKm",how="left")
    merge_soap['SKU'].count()
except:
    merge_soap = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass

#%%%
#INHALER
one_tabs["Cat"] = one_tabs["Cat"].apply(lambda x:x if str(x)!="nan" else "EMPTY")

one_tabs = df[df.Cat=="EMPTY"]
one_tabs.rename(columns={'OneMg':"SM"},inplace=True)
sm_tab["Cat"] = sm_tab["Cat"].apply(lambda x:x if str(x)!="nan" else "EMPTY")
sm_tab = sm_df[sm_df.Cat=="EMPTY"]
sm_tabs = pd.concat([sm_tab,sm_capsu])


one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("ML",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).lstrip())

sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("%",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).lstrip())

one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[()]",' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub("[/-]",' ', x))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("/",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("]",""))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("[",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'(/^\s+|\s+$|\s+(?=\s))', ' ', x))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())

sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
for r in range (0, len(sm_tabs['UK'])):
    sm_tabs['UK'].iloc[r]  = re.sub(r'\bG\b','',str(sm_tabs['UK'].iloc[r]))
sm_tabs["UKm"] = ""
one_tabs["UKm"] = ""
try:
    sm_tabs["UKm"] = sm_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    one_tabs["UKm"] = one_tabs.apply(lambda row: shuffle(row['UK']),axis=1)
    merge_empty = pd.merge(one_tabs,sm_tabs,on="UKm",how="inner")
    merge_empty['SKU'].count()
except:
    merge_empty = pd.DataFrame({"SM":[], "SKU":[], "Cat":[], "UK":[], "UKm":[]})
    pass

#%%
print("Category wise dataframe joining")
# =============================================================================
# Grand Concat
# =============================================================================
frames = [merge_caps,merge_cream,merge_drops,merge_gel,merge_INHAL,merge_liquid,merge_OIL,merge_OINT,merge_powder,merge_shampoo,merge_soap,merge_SPRAY,merge_susp,merge_syrup,merge_tablets,merge_SACHET,merge_empty]
#%%
main = pd.concat(frames)
main = main.drop_duplicates()
main.to_csv("Checkpoint.csv")
new_main = main.rename(columns={'SM_x':"OneMg",'SM_y':"SM"})
new_main["SKU"].count()
new_main["Units"] = ""
select = ['OneMg', 'Cat_x','UKm','SM', 'SKU', 'Cat_y']
new_main = new_main[select]
new_main.to_csv("final_merged_raw.csv", encoding='latin1')


#new_main = pd.read_csv("final_merged_raw.csv",encoding='latin1')

#%%

# =============================================================================
# 90% matchig starts here 
# =============================================================================
#this entire cell will  check matched SKUs and removes matched items from SM and OneMg dataframes
import re
SM = pd.read_csv('Cat_SM.csv', encoding='latin1')
sm_ref = SM["SKU"]
SM["Note"] = ""
lookup = (list(new_main[new_main.SKU!="nan"]["SKU"]))
for i in range (0, len(sm_ref)):
    val = str(SM["SKU"].iloc[i])
    if val in lookup:
        SM["Note"].iloc[i] = "Full"
#SM is now is like sm_tabs

one_tabs = new_main.copy()
one_tabs["Note"] = ""
one_tabs["Note"] = one_tabs["SKU"].apply(lambda x: "Full" if str(x)!="nan" else "")
#one_tabs = one_tabs[one_tabs.SKU==""]

# =============================================================================
# cleaning UP other text to match 90 %
# =============================================================================
SM["Note"].value_counts()
import time 
start = time.localtime()
from clean import *
sm_filt = SM[SM.Note!="Full"]
one_filt = one_tabs[one_tabs.Note!="Full"]
print(one_filt.columns)

one_filt = one_filt[['OneMg', 'Cat_x', 'UKm',"SKU","Note"]]
one_filt.rename(columns={"OneMg":"SM"},inplace=True)



#%%
print("Starting master cleaner #### started")
one,sm = master_cleaner(sm_filt,one_filt)
end = time.localtime()
print(start.tm_sec-end.tm_sec)
print("Starting master cleaner #### completed")
#%%
#%%


#%%
sm["UKm"] = ""
sm["UKm"] = sm.apply(lambda row: shuffle(row['UK']),axis=1)  

import copy
s = sm.copy()
o = one.copy()
#%%
one.rename(columns={"SM":"OneMg"},inplace=True)
sm["Units"] = ""
one["Units"] = ""
sm["Units"] = sm.apply(lambda row: getUnits(row['SM']),axis=1)

#%%

print("Dosage extraction SM #### started")
for i in range(0,len(sm["SM"])):
    if len(sm["Units"].iloc[i])==2:
        fr = sm["Units"].iloc[i].split(",")
        try:
            delNum = re.findall(r'([.\d]+)',fr[1])
            sm["UKm"].iloc[i] = sm["UKm"].iloc[i].replace(delNum[0],"")
        except:
            pass
    elif len(sm["Units"].iloc[i])==2:
        try:
            delNum1 = re.findall(r'([.\d]+)',fr[1])
            sm["UKm"].iloc[i] = sm["UK"].iloc[i].replace(delNum1[0],"")
            delNum2 = re.findall(r'([.\d]+)',fr[2])
            sm["UKm"].iloc[i] = sm["UK"].iloc[i].replace(delNum2[0],"")
        except:
            pass
print("Dosage extraction SM #### completed")
#%%
print("Dosage extraction OneMg #### started")
one["Units"] = one.apply(lambda row: getUnits(row['OneMg']),axis=1)

for i in range(0,len(one["OneMg"])):
    print("working",i)
    try:
        fr = one["Units"].iloc[i].split(",")
    except:
        pass
    if len(fr)==1:
        try:
            print("first ###########")
            delNum = re.findall(r'([.\d]+)',fr[1])
            one["UKm"].iloc[i] = one["UKm"].iloc[i].replace(delNum[0],"")
        except:
            pass
    elif len(fr)==2:
        try:
            print("second-------------")
            delNum1 = re.findall(r'([.\d]+)',fr[1])
            one["UK"].iloc[i] = one["UKm"].iloc[i].replace(delNum1[0],"").lstrip().rstrip()
            delNum2 = re.findall(r'([.\d]+)',fr[2])
            one["UK"].iloc[i] = one["UKm"].iloc[i].replace(delNum2[0],"").lstrip().rstrip()
        except:
            pass

#sm.to_csv("OneMg_Final.csv")

print("Dosage extraction OneMg #### completed")
#%%            

one["UKm"] = one["UKm"].apply(lambda x: x.replace("C. FILM",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("C.  FILM",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("C.FILM",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("FILM",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("DRY+SOL",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("DRY",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("1G",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("CAPS",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("CAP",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("FIL.C..ER",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("FIL.C..DS",""))

one["UKm"] = one["UKm"].apply(lambda x: x.replace(".C.",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("C.",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("SOLUT.",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("GEL",""))

one["UKm"] = one["UKm"].apply(lambda x: x.replace("IV.",""))
one["UKm"] = one["UKm"].apply(lambda x: x.replace("  "," "))
one["UKm"] = one["UKm"].apply(lambda x: x.rstrip())
one["UKm"] = one["UKm"].apply(lambda x: x.lstrip())
sm["UKm"] = sm["UKm"].astype(str)
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.  FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("DRY+SOL",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("DRY",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("1G",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("CAPS",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("CAP",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FIL.C..ER",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FIL.C..DS",""))

sm["UKm"] = sm["UKm"].apply(lambda x: x.replace(".C.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("SOLUT.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("GEL",""))

sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("IV.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("  "," "))
sm["UKm"] = sm["UKm"].apply(lambda x: x.rstrip())
sm["UKm"] = sm["UKm"].apply(lambda x: x.lstrip())
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C. FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.  FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FILM",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("DRY+SOL",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("DRY",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("1G",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("CAPS",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("CAP",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FIL.C..ER",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("FIL.C..DS",""))

sm["UKm"] = sm["UKm"].apply(lambda x: x.replace(".C.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("C.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("SOLUT.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("GEL",""))

sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("IV.",""))
sm["UKm"] = sm["UKm"].apply(lambda x: x.replace("  "," "))
sm["UKm"] = sm["UKm"].apply(lambda x: x.rstrip())
sm["UKm"] = sm["UKm"].apply(lambda x: x.lstrip())

        #%%

sm.to_csv("OneMg_Final.csv")
one.to_csv("SM_Final.csv")

#%%


#trial

#%%

# =============================================================================
# 90 percent merging step
# =============================================================================
sm = pd.read_csv('SM_Final.csv',encoding='latin1')
one = pd.read_csv('OneMg_Final.csv',encoding='latin1')
merged_95= pd.merge(one,sm,on="UKm",how="inner")
print(len(merged_95))
merged_95.to_csv("95%match.csv",encoding='latin1')
#%%
import pandas as pd
import re
import copy
#%%
#merged_95 = pd.read_csv('95%match.csv')
merged_95Copy = merged_95.copy() 
merged_95["SKU_y"] = merged_95["SKU_x"].astype(str)
merged_95.rename(columns={"SKU_x":'SKU'},inplace=True)
merged_95["SKU"] = merged_95["SKU"].astype(str)
merged_95 = merged_95[merged_95.SKU!="nan"]
merged_95["Note"] =""
merged_95["Note"] = "95_percent"
merged_95.to_csv("95%match.csv", encoding='latin1')
#%%    
# =============================================================================
# To remove matched items from SM and One mg with reference to merged95 95_percent Notes
# =============================================================================
sm = pd.read_csv('SM_Final.csv',encoding='latin1')
one = pd.read_csv('OneMg_Final.csv',encoding='latin1')
#this entire cell will  check matched SKUs and removes matched items from SM and OneMg dataframes
import re
SM = pd.read_csv('Cat_SM.csv', encoding='latin1')
sm_ref = SM["SKU"]

merged_95['SKU']=merged_95['SKU'].astype(str)

SM["Note"] = ""
lookup = (list(merged_95[merged_95.SKU!="nan"]["SKU"]))
for i in range (0, len(sm_ref)):
    val = str(SM["SKU"].iloc[i])
    try:
        if val in lookup:
            SM["Note"].iloc[i] = "95_percent"
    except:
        pass
#SM is now is like sm_tabsmerged_95
#%%
merged_95 = pd.read_csv("95%match.csv", encoding='latin1')
merged_95 = merged_95[["OneMg","Note","SKU","Units_x","UKm","SM"]]
#%%
new_main['SKU'] = new_main['SKU'].astype(str)
new_main = new_main[new_main.SKU!="nan"]
new_main["Note"] = ""
new_main["Note"] = "100_percent"
new_main["Units_x"] = ""
    
new_main["Units_x"] = new_main.apply(lambda row: getUnits(row['OneMg']),axis=1)
    
new_main.rename(columns={"SM":"SM_y"},inplace=True)
new_main = new_main[["OneMg","Note","SKU","Units_x","UKm","SM_y"]]
try:
    master_merged = new_main.append([merged_95])
except:
    master_merged  = new_main

master_merged.to_csv("matched_master.csv", encoding='latin1')
#%%
SM_resi = pd.read_csv('SM.csv',encoding='latin1')
OneMg_resi = pd.read_csv('OneMg.csv',encoding="latin1")

#%%
import time 
start = time.localtime()
resi_OneMg = []
setb = list(OneMg_resi["OneMg"])
seta = list(master_merged.OneMg)
import numpy as np
main_list_OneMg = np.setdiff1d(setb,seta)
print(len(main_list_OneMg))
end = time.localtime()
print(start.tm_sec-end.tm_sec)     
#%%

#filter code


#%%
smSeta = list(master_merged.SM_y)
smSetb = list(SM_resi["SM"])
main_list_SM = np.setdiff1d(smSetb,smSeta)
print(len(main_list_SM))
#%%
fuzzy_O = pd.DataFrame({"OneMg":main_list_OneMg})
fuzzy_O.rename(columns={"OneMg":"SM"},inplace=True)
fuzzy_S = pd.DataFrame({"SM":main_list_SM})
fuzzy_O.to_csv("fuzzy_OneMg.csv")
fuzzy_S.to_csv("fuzzy_SM.csv")
#%%
import os
savecurrent = os.getcwd()

oneONEfina,oneSMFinal = master_cleaner(fuzzy_O, fuzzy_S)
#%%
import os 
#uncommment below after run
os.system("mkdir last")

os.chdir("last")
os.system("mkdir ONEMG")
os.system("mkdir SM")


#%%

oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("C.TABS",""))
oneSMFinal["UK"] =oneSMFinal["UK"].apply(lambda x: str(x).replace("SYRUP",""))
oneSMFinal["UK"] =oneSMFinal["UK"].apply(lambda x: str(x).replace("GEL","")) 
oneSMFinal["UK"] =oneSMFinal["UK"].apply(lambda x: str(x).replace("SUSPENSION","")) 
oneSMFinal["UK"] =oneSMFinal["UK"].apply(lambda x: str(x).replace("INHALER","")) 
oneSMFinal["UK"] =oneSMFinal["UK"].apply(lambda x: str(x).replace("INHA","")) 

oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("C.TABS",""))
oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("SYRUP",""))
oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("GEL","")) 
oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("SUSPENSION","")) 
oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("INHALER","")) 
oneONEfina["UK"] =oneONEfina["UK"].apply(lambda x: str(x).replace("INHA","")) 
oneONEfina.to_csv("oneSMFinal.csv")
oneSMFinal.to_csv("oneONEfina.csv")
#os.chdir("..")
#%%
os.chdir(savecurrent)



#%% 

# =============================================================================
# Fuzzy 95
# =============================================================================
#fuzzy run
import difflib 

def fuzzy_merge(df1, df2, left_on, right_on, how='inner', cutoff=0.80):
    df_other= df2.copy()
    df_other[left_on] = [get_closest_match(x, df1[left_on], cutoff) 
                         for x in df_other[right_on]]
    return df1.merge(df_other, on=left_on, how=how)

def get_closest_match(x, other, cutoff):
    matches = difflib.get_close_matches(x, other, cutoff=cutoff)
    return matches[0] if matches else x

#res = fuzzy_merge(oneONEfina, oneSMFinal, left_on='UK', right_on='UK')

    

#Fuzzy Run
def split_csv(source_filepath, dest_folder, split_file_prefix,
                records_per_file):
    import csv
    import os
    """
    Split a source csv into multiple csvs of equal numbers of records,
    except the last file.

    Includes the initial header row in each split file.

    Split files follow a zero-index sequential naming convention like so:

        `{split_file_prefix}_0.csv`
    """
    if records_per_file <= 0:
        raise Exception('records_per_file must be > 0')

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_idx = 0
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f'{split_file_prefix}_{file_idx}.csv'
            target_filepath = os.path.join(dest_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < records_per_file:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_idx += 1
#%%Fuzzy Run

split_csv("last/oneSMFinal.csv","last/SM","SM__Mg",3000) #26
import glob
count = 0
for k in glob.glob("last/SM/*.csv"):
    count+=1
#%%
#above 10000K to lakhs
newNumber = len(pd.read_csv("last/oneONEfina.csv"))/count
split_csv("last/oneONEfina.csv","last/ONEMG","ONEMGBATCH__Mg",newNumber)
#%%



for i in range(0,count):
    print(i)
    sample1 = pd.read_csv("last/ONEMG/ONEMGBATCH__Mg_{}.csv".format(i))
    sample2 = pd.read_csv("last/SM/SM__Mg_{}.csv".format(i))
    res1 = fuzzy_merge(sample1, sample2, left_on='UK', right_on='UK')
    res1.to_csv("fuzzyMatched_{}.csv".format(i))
itemsall= []
for g in glob.glob("fuzzyMatched_*.csv"):
    itemsall.append(g)
combined_csv = pd.concat([pd.read_csv(f) for f in itemsall])
combined_csv.rename(columns={"SM_x":"SM", "SM_y":"OneMg"},inplace=True)

one = combined_csv
one["Units"] = ""
one["Notes"] = ""
one["Notes"] ="Fuzzy_95"

one.to_csv( "combined95_fuzzy.csv", index=False, encoding='utf-8-sig')
#%%


# =============================================================================
# Cross check type of item in fuzzy 95 data and eliminating wrongly matched data  #start
# =============================================================================
crosscheck = pd.read_csv("combined95_fuzzy.csv")
crosscheck.rename(columns={"SM":"OneMg", "OneMg":"SM"},inplace="True")
SM = pd.read_csv('Cat_SM.csv', encoding='latin1')
OneMg = pd.read_csv('Cat_OneMg.csv', encoding='latin1')
#%%
crosscheck["Cat_SM"] = ""
crosscheck["Cat_OneMg"] = ""

for i in range(0, len(crosscheck)):
    if crosscheck["OneMg"].iloc[i] in list(OneMg["OneMg"]):
        if len(OneMg[OneMg.OneMg==crosscheck["OneMg"].iloc[i]])!=0:
            crosscheck["Cat_OneMg"].iloc[i] = (list(OneMg[OneMg.OneMg==crosscheck["OneMg"].iloc[i]]["Cat"])[0])
            
for i in range(0, len(crosscheck)):
    if crosscheck["SM"].iloc[i] in list(SM["SM"]):        
        if len(SM[SM.SM==crosscheck["SM"].iloc[i]])!=0:
            crosscheck["Cat_SM"].iloc[i] = (list(SM[SM.SM==crosscheck["SM"].iloc[i]]["Cat"])[0])
#%%
df = crosscheck
#df = pd.read_csv("90_cat_mapped_to_fuzzy90_test.csv")

for i in range(0,len(df)):
    catsm = df["Cat_SM"].iloc[i]
    catone = df["Cat_OneMg"].iloc[i]
    if str(catsm)!=str(catone):
        df["UK"].iloc[i] = "CHECK_IT_95Fuz"
crosscheck = df

crosscheck = crosscheck[crosscheck.Notes=="Fuzzy_95"]
crosscheck.to_csv('95_cat_mapped_to_fuzzy95.csv')
# ========================================================================================
# # Cross check type of item in fuzzy 95 data and eliminating wrongly matched data  #end
# ========================================================================================

#%%

#Fuzzzy 90

import difflib 

def fuzzy_merge(df1, df2, left_on, right_on, how='inner', cutoff=0.65):
    df_other= df2.copy()
    df_other[left_on] = [get_closest_match(x, df1[left_on], cutoff) 
                         for x in df_other[right_on]]
    return df1.merge(df_other, on=left_on, how=how)

def get_closest_match(x, other, cutoff):
    matches = difflib.get_close_matches(x, other, cutoff=cutoff)
    return matches[0] if matches else x

def split_csv(source_filepath, dest_folder, split_file_prefix,
                records_per_file):
    import csv
    import os
    """
    Split a source csv into multiple csvs of equal numbers of records,
    except the last file.

    Includes the initial header row in each split file.

    Split files follow a zero-index sequential naming convention like so:

        `{split_file_prefix}_0.csv`
    """
    if records_per_file <= 0:
        raise Exception('records_per_file must be > 0')

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_idx = 0
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f'{split_file_prefix}_{file_idx}.csv'
            target_filepath = os.path.join(dest_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < records_per_file:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_idx += 1

#%%
import glob
count = 0
for k in glob.glob("last/ONEMG/*.csv"):
    count+=1

for i in range(0,count):
    print(i)
    sample1 = pd.read_csv("last/ONEMG/ONEMGBATCH__Mg_{}.csv".format(i))
    sample2 = pd.read_csv("last/SM/SM__Mg_{}.csv".format(i))
    res1 = fuzzy_merge(sample1, sample2, left_on='UK', right_on='UK')
    res1.to_csv("fuzzyMatched_{}.csv".format(i))
itemsall= []
for g in glob.glob("fuzzyMatched_*.csv"):
    itemsall.append(g)
combined_csv = pd.concat([pd.read_csv(f) for f in itemsall])
combined_csv.rename(columns={"SM_x":"SM", "SM_y":"OneMg"},inplace=True)

two = combined_csv
two["Units"] = ""
two["Notes"] = ""
two["Notes"] ="Fuzzy_90"

two.to_csv( "combined90_fuzzy.csv", index=False, encoding='utf-8-sig')
#%%
two["Cat_SM"] = ""
two["Cat_OneMg"] = ""
SM = pd.read_csv('Cat_SM.csv', encoding='latin1')
OneMg = pd.read_csv('Cat_OneMg.csv', encoding='latin1')
for i in range(0, len(two)):
    if two["OneMg"].iloc[i] in list(OneMg["OneMg"]):
        if len(OneMg[OneMg.OneMg==two["OneMg"].iloc[i]])!=0:
            two["Cat_OneMg"].iloc[i] = (list(OneMg[OneMg.OneMg==two["OneMg"].iloc[i]]["Cat"])[0])
            
for i in range(0, len(two)):
    if two["SM"].iloc[i] in list(SM["SM"]):        
        if len(SM[SM.SM==two["SM"].iloc[i]])!=0:
            two["Cat_SM"].iloc[i] = (list(SM[SM.SM==two["SM"].iloc[i]]["Cat"])[0])

#%%
two_un = pd.DataFrame()
crosscheck = pd.read_csv("combined95_fuzzy.csv")
checkX = list(crosscheck["SM"])
for i in range(0,len(two["SM"])):
    if two["SM"].iloc[i] not in checkX:
        if len(two["SM"].iloc[i])!=0:
            two_un = two_un.append(two.iloc[i])
#%%
print("funzzy 90 matching dfs")
SM = pd.read_csv('SM.csv',encoding='latin1')
one = pd.read_csv('combined95_fuzzy.csv',encoding='latin1')
one.rename(columns={"SM":"OneMg", "OneMg":"SM"},inplace=True)

finalFuzzy = pd.merge(SM,one, on="SM", how="inner")
finalFuzzy = finalFuzzy[['SM', 'SKU', 'Notes', 'OneMg', 'UK', 'Units']]

two_un.rename(columns={"SM":"OneMg", "OneMg":"SM"},inplace="True")

finalFuzzy1 = pd.merge(SM,two_un, on="SM", how="inner")
try:
    finalFuzzy1 = finalFuzzy1[['SM', 'SKU', 'Notes', 'OneMg', 'UK', 'Units']]
except:
    finalFuzzy1 = pd.DataFrame({'SM':[], 'SKU':[], 'Notes':[], 'OneMg':[], 'UK':[], 'Units':[]})
#%%
final_fuz = finalFuzzy1
#adding category
SM = pd.read_csv('Cat_SM.csv', encoding='latin1')
OneMg = pd.read_csv('Cat_OneMg.csv', encoding='latin1')
final_fuz["Cat_SM"] = ""
final_fuz["Cat_OneMg"] = ""

for i in range(0, len(final_fuz)):
    if final_fuz["OneMg"].iloc[i] in list(OneMg["OneMg"]):
        if len(OneMg[OneMg.OneMg==final_fuz["OneMg"].iloc[i]])!=0:
            final_fuz["Cat_OneMg"].iloc[i] = (list(OneMg[OneMg.OneMg==final_fuz["OneMg"].iloc[i]]["Cat"])[0])
            
for i in range(0, len(final_fuz)):
    if final_fuz["SM"].iloc[i] in list(SM["SM"]):        
        if len(SM[SM.SM==final_fuz["SM"].iloc[i]])!=0:
            final_fuz["Cat_SM"].iloc[i] = (list(SM[SM.SM==final_fuz["SM"].iloc[i]]["Cat"])[0])

#%%

for i in range(0,len(final_fuz)):
    catsm = final_fuz["Cat_SM"].iloc[i]
    catone = final_fuz["Cat_OneMg"].iloc[i]
    if str(catsm)!=str(catone):
        final_fuz["UK"].iloc[i] = "CHECK_IT_90Fuz"
final_fuz = final_fuz

final_fuz = final_fuz[final_fuz.Notes=="Fuzzy_90"]
final_fuz.to_csv('90_cat_mapped_to_fuzzy95.csv')
#%%
final_fuz = pd.concat([finalFuzzy,finalFuzzy1])
#%%
print("at regular 95 match")
merged_95 = pd.read_csv("95%match.csv")
merged_95.rename(columns={"SM_x":"SM"},inplace=True)
merged_95Copy.rename(columns={"SM_x":"SM"},inplace=True)
merged95 = pd.merge(SM,merged_95Copy,on="SM",how="inner")
merged95.rename(columns={"SM_x":"SM","UK_x":"UK","Notes_y":"Notes","Units_y":"Units"},inplace=True)
merged95["Notes"] = "95Match"
merged95 = merged95[['SM', 'SKU', 'Notes', 'OneMg', 'UK', 'Units']]
new_main=new_main[['OneMg', 'Note', 'SKU', 'Units_x', 'UKm','SM_y']]

#%%
try:
    ~new_main.columns.duplicated()
    lk=[True, True, True, True, True, False, True]
    new_main = new_main.loc[:, lk]
except:
    ~new_main.columns.duplicated()
    lk=[True, True, True, True, True,True]
    new_main = new_main.loc[:, lk]

SM3 = pd.merge(SM,final_fuz,on="SM",how="inner")
SM3.to_csv("SM3.csv")
new_main.rename(columns={"Units_y":"Units","Note":"Notes","SM_y":"SM"},inplace=True)


#%%

#%%

SM4 = pd.merge(SM,new_main,on="SM",how="inner")
SM5 = pd.merge(SM,merged95,on="SM",how="inner")

masterF = [SM3,SM4,SM5]
masterconcat = pd.concat(masterF)
masterconcat.rename(columns={"SKU_y":"SKU"},inplace=True)
masterconcat = masterconcat[['SM', 'SKU', 'Notes', 'OneMg', 'UK', 'Units']]
SMmaster = pd.merge(SM, masterconcat,on="SKU", how="left")
SMmaster.rename(columns={"SM_x":"SM"},inplace=True)
SMmaster = SMmaster[['SM', 'SKU', 'Notes', 'OneMg', 'UK', 'Units']]
SMmaster.to_csv("master_mapped.csv")
#%%
print("getting dosage")
sm = SMmaster
sm["Units"] = ""
sm["Units"] = sm.apply(lambda row: getUnits(row['SM']),axis=1)
for i in range(0,len(sm["SM"])):
    if len(sm["Units"].iloc[i])==2:
        fr = (sm["Units"].iloc[i]).split(",")
        try:
            delNum = re.findall(r'([.\d]+)',fr[1])
            sm["UKm"].iloc[i] = sm["UKm"].iloc[i].replace(delNum[0],"")
        except:
            pass
    elif len(sm["Units"].iloc[i])==2:
        try:
            delNum1 = re.findall(r'([.\d]+)',fr[1])
            sm["UK"].iloc[i] = sm["UKm"].iloc[i].replace(delNum1[0],"")
            delNum2 = re.findall(r'([.\d]+)',fr[2])
            sm["UK"].iloc[i] = sm["UKm"].iloc[i].replace(delNum2[0],"")
        except:
            pass
#%%
import copy
tdf = sm.copy()
tdf.drop_duplicates(keep='first', inplace=True, subset="SKU")

#%%
one_df = pd.read_csv("Cat_OneMg.csv",encoding='latin1')
sm_df = pd.read_csv("Cat_SM.csv",encoding='latin1')
sm_df = sm_df[['Cat','SKU']]
one_df = one_df[['OneMg','Cat']] 
sm_df.rename(columns={'Cat':'SM_Category'},inplace=True)
one_df.rename(columns={'Cat':'OneMg_Category'},inplace=True)
res = pd.merge(tdf,sm_df,on='SKU',how='left')
res = pd.merge(res,one_df,on='OneMg',how='left')

#%%
res.to_csv("final_closest_match.csv")
 
# =============================================================================
# Run below code now
# =============================================================================

###


#%%
import pandas as pd
main = pd.read_csv("final_closest_match.csv",encoding="latin1")
a100 = pd.read_csv("matched_master.csv", encoding="latin1")
a95 = pd.read_csv("95%match.csv", encoding="latin1")
f95 = pd.read_csv("95_cat_mapped_to_fuzzy95.csv",encoding="latin1")
f90 = pd.read_csv("combined90_fuzzy.csv",encoding="latin1")

#%%
c = 0
for i in range(0, len(main)):
    tite = main["SKU"].iloc[i]
    if tite in list(a100["SKU"]):
        if len(list(a100[a100.SKU==tite]["OneMg"]))!=0:
            #print(main["SM"].iloc[i], " :: ",list(a100[a100.SKU==tite]["OneMg"])[0])
            main["OneMg"].iloc[i] = list(a100[a100.SKU==tite]["OneMg"])[0]
            main["Notes"].iloc[i] = "100_percent"
            c+=1
            print(c)

main.to_csv("100CheckIt.csv")
#%%
print("working at 95%")
c = 0
for i in range(0, len(main)):
    tite = main["SKU"].iloc[i]
    if tite in list(a95["SKU"]):
        if len(list(a95[a95.SKU==tite]["OneMg"]))!=0:
            #print(main["SM"].iloc[i], " :: ",list(a100[a100.SKU==tite]["OneMg"])[0])
            main["OneMg"].iloc[i] = list(a95[a95.SKU==tite]["OneMg"])[0]
            main["Notes"].iloc[i] = "95Match"
            c+=1
            print(c, "out of "+ str(len(a95[a95.Note=="95_percent"])))
main.to_csv("100_95_CheckIt.csv")

#%%
print("working at Fuzzy 95%")
c = 0
for i in range(0, len(main)):
    tite = main["SM"].iloc[i]
    if (tite in list((main[main.Notes=="100_percent"])["SM"])) or (tite in list((main[main.Notes=="Fuzzy_95"])["SM"])):
        print(i, "a")
        pass
    elif tite in list(f95["SM"]):
        if len(list(f95[f95.SM==tite]["OneMg"]))!=0:
            #print(main["SM"].iloc[i], " :: ",list(a100[a100.SKU==tite]["OneMg"])[0])
            main["OneMg"].iloc[i] = list(f95[f95.SM==tite]["OneMg"])[0]
            main["Notes"].iloc[i] = "Fuzzy_95"
            c+=1
            print(c, "out of "+ str(len(f95[f95.Notes=="Fuzzy_95"])))
    else:
        print(i,"b")
        pass
main = main.drop_duplicates(subset=['SKU'], keep='first')
main.to_csv("Final_Output.csv")

#%%

past = datetime.now()

print(past-now)
