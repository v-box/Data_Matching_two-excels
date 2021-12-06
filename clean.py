#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:16:06 2020

@author: kiran
"""
import re

def getUnits(text):
    ress = re.findall(r'([.\d]+)\s*?(:mg|GM|ml|L|q.s.|MG|ML|SOLUTION|INJECTION|OIL|IU|G)', text)
    try:
        returnObj = " "
        for r in ress:
            rs = (' '.join(r))
            returnObj = returnObj +rs +","
        returnObj = returnObj.rstrip(",")
    except:
        pass
    return returnObj
   #%% 
def getmaxNum(text):
    #text = "20 50 AQUADOL SPAS"
    ress = re.findall(r'([.\d]+)', text)
    ress.sort()
    notin = []
    for i in text.split(","):
        try:
            if ress[-1] in i:
                pass
            else:
                notin.append(i)
                text = text.replace(i,"").replace(",","")
        except:
            pass
    ress = re.findall(r'([.\d]+)', text)
    ress.sort(reverse=True)
    try:
        x = ress[0]
        ress = re.findall(r'([.\D]+)', text)
        for i in ress:
            r = ' '.join(ress)
        r = r.replace(".","")
        r = r.replace(",","") 
        r = r.replace("  "," ")    
        y = r.rstrip().lstrip()
        text = x +" "+ y
        text = text.replace("  "," ")
        text = text.replace(" GM "," ")
        text = text.replace(" MG "," ")    
        text = text.replace(" G "," ")
        text = text.replace(" L "," ")
    except:
        text
    #print(text)
    return text

#%%

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

def master_cleaner(one_tabs,sm_tabs):    
    one_tabs["SM"] = one_tabs["SM"].apply(lambda x: str(x).replace("-",""))
    one_tabs["SM"] = one_tabs["SM"].apply(lambda x: str(x).replace(" /"," "))
    one_tabs["SM"] = one_tabs["SM"].apply(lambda x: str(x).replace("/"," "))
    try:
        one_tabs["UK"] = one_tabs["SM"].apply(lambda x: str(x).replace("OIL",""))
    except:
        pass
    print(one_tabs.columns, sm_tabs.columns)
    sm_tabs["SM"] = sm_tabs["SM"].apply(lambda x: str(x).replace("-",""))
    sm_tabs["SM"] = sm_tabs["SM"].apply(lambda x: str(x).replace(" /"," "))
    sm_tabs["SM"] = sm_tabs["SM"].apply(lambda x: str(x).replace("/"," "))
    sm_tabs["UK"] = sm_tabs["SM"].apply(lambda x: str(x).replace("OIL",""))
    
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))

    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("TABLETS",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("TABLET",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TABS",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
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
    print("25 percent completed")
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
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TAB.ER",""))    
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.TAB.MR",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.TAB.",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM.C.",""))    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM C.TABS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("UNCOATED",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DISPERS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FIL.C.BILAYE",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("F.C.OPS",""))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TABS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ENT.F.C.TAB",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("F.C.",""))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("COATED",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("FILM C.S",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TABS.CR",""))    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("TABS.SR",""))    
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
    print("50 percent completed")
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INJECTIONS",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INJECTION",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INJ",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("VIAL",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip()) 
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJECTIONS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJECTION",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INJ",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("(1 VIAL)",""))
    
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
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub('[/]', ' ', x))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('[/]', ' ', x))
    print("75 percent completed")
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("CREAMS",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("CREAM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CREAMS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("CREAM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'\bIU\b','',str(x)))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'\bG\b','',str(x)))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("LIQUID",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("LIQUID",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("LIQUID",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("LIQUID",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("DROPS",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("DROP",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    print("85 percent completed")
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DROPS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("DROP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SYRUP",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SYP",""))
    print("86 percent completed")
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SYRUP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SYP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSUSPENSION",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSPENSION",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    print("87 percent completed")
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSPENSION",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("MG",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))    
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SHAMPOO",""))    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SHAMPOO",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("POWDER",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("POWDER",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SPRAY",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SPRAY",""))
    print("90 percent completed")
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SYRUP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SYRUP",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SUSUSPENSION",""))    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSPENSION",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SHAMPOO",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SHAMPOO",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("POWDER",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("POWDER",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SPRAY","")) 
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SPRAY","")) 
    print("95 percent completed")
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("OINTMENT",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("OINTMENT",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("OINT",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("ML",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("GM",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("%",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOLUTION",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("OINT",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SUSP",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHALE",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHAL",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("INHAL.",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INAHLE",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INHAL",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("INHAL.",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOAPS",""))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("SOAP",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOAPS",""))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("SOAP",""))
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub('IU', '', x))        
    sm_tabs['UK'] = sm_tabs['UK'].apply(lambda x: re.sub(r'\bIU\b','',str(x)))    
    one_tabs['UK'] = one_tabs['UK'].apply(lambda x: re.sub(r'\bIU\b','',str(x)))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("(DCA)N"," "))
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: str(x).replace("DCA"," "))    
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: str(x).replace("  "," "))
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.rstrip())
    sm_tabs["UK"] = sm_tabs["UK"].apply(lambda x: x.lstrip())
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.rstrip())
    one_tabs["UK"] = one_tabs["UK"].apply(lambda x: x.lstrip())
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
    
    return sm_tabs,one_tabs
