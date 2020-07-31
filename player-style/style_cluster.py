import os
import glob
from pathlib import Path

import json
import csv
import numpy as np
import pandas as pd 
import sklearn as sk 
from sklearn.manifold import TSNE


def tsne_cluster():
    pass


def aggregatedata(df):
    df = df.sum(level = 'player')
    return df

def data_preprocess(df):
    names1  = df["match_id"].astype(str)
    names2  = df["match_id"].astype(str)
    nameidx = df['player'].astype(str)
    name1 = [name.split('-')[-1] for name in names1]
    name2 = [name.split('-')[-2] for name in names2]
    #df['name1'] = name1
    #df['name2'] = name2
    newnameidx = [name1[idx] if player else name2[idx] for (idx,player) in enumerate(nameidx)]
    df['player'] = newnameidx
    #print(df.head())
    return df 

def getmatches(df):
    return df
def getpoints(df):
    return df
def getkeypointreturn(df):
    return df
def getkeypointserve(df):
    return df
def getnetpoints(df):
    df = df[["player",
             "net_pts",
             "pts_won",
             "net_winner",
             "induced_forced",
             "net_unforced",
             "passed_at_net",
             "passing_shot_induced_forced",
             "total_shots"]
            ]
    return df
def getoverview(df):
    df = df[["player",
             "serve_pts",
             "aces",
             "dfs",
             "first_in",
             "first_won",
             "second_in",
             "second_won",
             "bk_pts",
             "bp_saved",
             "return_pts",
             "return_pts_won",
             "winners",
             "winners_fh",
             "winners_bh",
             "unforced",
             "unforced_fh",
             "unforced_bh"]
            ]
    return df

def getrally(df):
    return df
def getreturndepth(df):
    df = df[["player",
             "returnable",
             "shallow",
             "deep",
             "very_deep",
             "unforced",
             "err_net",
             "err_deep",
             "err_wide",
             "err_wide_deep"]
            ]
    return df
def getreturnoutcome(df):
    df = df[["player",
             "pts",
             "pts_won",
             "returnable",
             "returnable_won",
             "in_play",
             "in_play_won",
             "winners",
             "total_shots"]
            ]
    return df
def getservebasics(df):
    df = df[["player",
             "pts_won",
             "aces",
             "unret",
             "forced_err",
             "pts_won_lte_3_shots",
             "wide",
             "body",
             "t"]]
    return df
def getserveDirection(df):
    return df
def getserveinfluence(df):
    return df
def getshotdir(df):
    df = df[["player",
             "crosscourt",
             "down_middle",
             "down_the_line",
             "inside_out",
             "inside_in"]
            ]
    return df

def getshotdirection(df):
    df = df[["player",
             "crosscourt",
             "down_middle",
             "down_the_line",
             "inside_out",
             "inside_in"]
            ]
    return df

def getshotdiroutcomes(df):
    df = df[["player",
             "shots",
             "pt_ending",
             "winners",
             "induced_forced",
             "unforced",
             "shots_in_pts_won",
             "shots_in_pts_lost"]
            ]
    return df

def getshottypes(df):
    df = df[["player",
             "shots",
             "pt_ending",
             "winners",
             "induced_forced",
             "unforced",
             "serve_return",
             "shots_in_pts_won",
             "shots_in_pts_lost"]
            ]
    return df
def getsnv(df):
    df = df[["player",
             "snv_pts",
             "pts_won",
             "aces",
             "unret",
             "return_forced",
             "net_winner",
             "induced_forced",
             "net_unforced",
             "passed_at_net",
             "passing_shot_induced_forced",
             "total_shots"]
            ]
    return df

def getsvbreaksplit(df):
    df = df[["player",
             "first_pts",
             "first_pts_won",
             "first_aces",
             "first_unret",
             "first_forced",
             "first_won_lte_3_shots",
             "second_pts",
             "second_pts_won",
             "second_aces",
             "second_unret",
             "second_forced",
             "second_won_lte_3_shots"]
            ]
    return df

def getsvBreakTotal(df):
    df = df[["player",
             "pts",
             "pts_won",
             "aces",
             "unret",
             "forced_err",
             "pts_won_lte_3_shots",
             "first_in",
             "dfs"]
            ]
    return df

def checksparseness(df):
    sparse = dict()
    sparse["totalrows"] = df.shape[0]

    columns = df.columns.values
    #print("columns: ",columns)
    for column in columns:
        columndata = df[column]
        count = int(columndata.isna().sum())
        sparse[column] = count


    return sparse


def getnumericdata(dflist):
     #[0,2,4,5,8,9,13,16,17,18,20,21,22,23,25,26,29,30,31,32,36]
    dflist[0] = getsvbreaksplit(dflist[0]) # charting-w-stats-SvBreakSplit.csv
    #dflist[1] = getservebasics(dflist[1]) # charting-w-stats-ServeBasics.csv
    dflist[1] = getreturndepth(dflist[1]) # charting-w-stats-ReturnDepth.csv
    #dflist[3] = getserveinfluence(dflist[3]) # charting-w-stats-ServeInfluence.csv
    dflist[2] = getshotdirection(dflist[2])# charting-w-stats-ShotDirection.csv
    dflist[3] = getreturnoutcome(dflist[3])# charting-m-stats-ReturnOutcomes.csv
    #dflist[6] = getserveDirection(dflist[6])# charting-m-stats-ServeDirection.csv
    #dflist[7] = getserveDirection(dflist[7])# charting-w-stats-ServeDirection.csv
    dflist[4] = getshotdir(dflist[4])# charting-m-stats-ShotDir.csv
    dflist[5] = getshotdirection(dflist[5]) #charting-m-stats-ShotDirection.csv
    #dflist[10] = getkeypointserve(dflist[10]) # charting-m-stats-KeyPointsServe.csv
    #dflist[11] = getkeypointreturn(dflist[11]) # charting-m-stats-KeyPointsReturn.csv
    #dflist[12] = getservebasics(dflist[11]) # charting-m-stats-ServeBasics.csv
    dflist[6] = getnetpoints(dflist[6]) # charting-m-stats-NetPoints.csv
    #dflist[14] = getmatches(dflist[13]) # charting-m-matches.csv
    #dflist[15] = getserveinfluence(dflist[14]) # charting-m-stats-ServeInfluence.csv
    dflist[7] = getsvBreakTotal(dflist[7])# charting-w-stats-SvBreakTotal.csv
    dflist[8] = getreturndepth(dflist[8])# charting-m-stats-ReturnDepth.csv
    dflist[9] = getoverview(dflist[9])# charting-w-stats-Overview.csv
    #dflist[19] = getpoints(dflist[18])# charting-w-points.csv
    dflist[10] = getshotdiroutcomes(dflist[10])# charting-m-stats-ShotDirOutcomes.csv
    dflist[11] = getsnv(dflist[11])# charting-w-stats-SnV.csv
    dflist[12] = getsnv(dflist[12])# charting-m-stats-SnV.csv
    dflist[13] = getnetpoints(dflist[13])# charting-w-stats-NetPoints.csv
    #dflist[24] = getmatches(dflist[23])# charting-w-matches.csv
    dflist[14] = getreturnoutcome(dflist[14])# charting-w-stats-ReturnOutcomes.csv
    dflist[15] = getsvbreaksplit(dflist[15])# charting-m-stats-SvBreakSplit.csv
    #dflist[27] = getkeypointserve(dflist[26])# charting-w-stats-KeyPointsServe.csv
    #dflist[28] = getkeypointreturn(dflist[27])# charting-w-stats-KeyPointsReturn.csv
    dflist[16] = getshottypes(dflist[16])# charting-w-stats-ShotTypes.csv
    dflist[17] = getsvBreakTotal(dflist[17])# charting-m-stats-SvBreakTotal.csv
    dflist[18] = getshottypes(dflist[18])# charting-m-stats-ShotTypes.csv
    dflist[19] = getshotdiroutcomes(dflist[19]) # charting-w-stats-ShotDirOutcomes.csv
    #dflist[33] = getrally(dflist[33])# charting-m-stats-Rally.csv
    #dflist[34] = getpoints(dflist[34])# charting-m-points.csv
    #dflist[35] = getrally(dflist[35])# charting-w-stats-Rally.csv
    dflist[20] = getoverview(dflist[20])# charting-m-stats-Overview.csv
    #[0,2,4,5,8,9,13,16,17,18,20,21,22,23,25,26,29,30,31,32,36]
    return dflist

def cyclesparsenessfiles(dflist,filenames):
    resultdict = dict()
    for idx,[df,filename] in enumerate(zip(dflist,filenames)):
        result = checksparseness(df)
        result['idx'] = idx
        resultdict[str(filename)] = result
    
    return resultdict

def read_charting_data(directory):
    dflist = []
    filenames = []
    for filepath in Path(directory).glob('**/*'):
        afile = filepath.absolute()
        #print(afile)
        extension = afile.suffix
        #print(extension)
        if(extension ==".csv"):
            print(afile)
            df = pd.read_csv(afile, engine='python',index_col=False) #,error_bad_lines=False) #, quoting=csv.QUOTE_NONE, encoding='utf-8')
            df.rename( columns={0 :'id'}, inplace=True)
            dflist.append(df)
            filenames.append(os.path.basename(afile))
            #if(filenames[-1] == "charting-m-stats-ReturnOutcomes.csv"): #"charting-m-stats-ReturnOutcomes.csv"):
                #print(df)

    return dflist,filenames


def main():
    dirname = Path("/home/dima/Desktop/datamining/project/files/tennis_MatchChartingProject")
    files = os.listdir(dirname)
    #print(files)
    dflist,filenames = read_charting_data(dirname)
    #print(dflist)

    #result = cyclesparsenessfiles(dflist,filenames)
    #print(result)

    indexes = [0,2,4,5,8,9,13,16,17,18,20,21,22,23,25,26,29,30,31,32,36]
    #print("indexes: ",indexes, indexes.shape)
    newdflist = [dflist[idx] for idx in indexes]
    dflist = newdflist
    #print('test: ',dflist)
    #print(dflist[0].head())

    for idx,_ in enumerate(dflist):
        print('index: ',idx)
        dflist[idx]=data_preprocess(dflist[idx])

    #print(dflist[0].head())
    dflist = getnumericdata(dflist)
    dflist = [df.set_index('player') for df in dflist]
    #print(dflist[0])
    #print(dflist[4].head())
    dflist = [aggregatedata(df) for df in dflist]
    print(dflist[0].head(20))

    dflist = np.array(dflist)
    femaledflist = dflist[[0,1,2,7,9,11,13,14,16,19]]
    maledflist = dflist[[3,4,5,6,8,10,12,15,17,18,20]]

    maledf = pd.concat(maledflist,axis=1).reindex(maledflist[0].index)
    maledf = maledf.fillna(0)
    maledf = maledf.groupby(lambda x:x, axis=1).sum()
   
    femaledf = pd.concat(femaledflist,axis=1).reindex(femaledflist[0].index)
    femaledf = femaledf.fillna(0)
    femaledf = femaledf.groupby(lambda x:x, axis=1).sum()

    aggdf = pd.concat([maledf,femaledf])
    
    #aggdf  = pd.concat(dflist, axis=1).reindex(dflist[0].index)
    #aggdf = aggdf.fillna(0)
    #aggdf = aggdf.groupby(lambda x:x, axis=1).sum()
    #aggdf = aggdf.groupby(aggdf.columns.values, axis=1).agg(lambda x: x.values.tolist()).sum().apply(pd.Series).T

    #print(aggdf)
    aggdf.to_csv('aggdf.csv')
    #df = pd.read_csv()
    #with open('ChartingProjectSparsity.json', 'w') as outfile:
    #     json.dump(result,outfile,indent=4)

if __name__ == "__main__":
    main()