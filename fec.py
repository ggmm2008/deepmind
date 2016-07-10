import pandas as pd
import numpy as np 

def loadData():
    fec=pd.read_csv('/home/linjun/Downloads/P00000001-ALL.csv')
    return fec

def loadParties():
    parites=pd.read_csv('/home/linjun/deepmind/parties.csv',sep='-',index_col=0,header=None).to_dict()
    return parites[1]


def main():
    fec=loadData()
    parties=loadParties()
    fec['parties']=fec.cand_nm.map(parties)
    fec=fec[fec.contb_receipt_amt>0]
    print (fec.contb_receipt_amt>0).value_counts()
    fec_mrbo=fec[fec.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]

    
def editData():
    occ_mapping={}
