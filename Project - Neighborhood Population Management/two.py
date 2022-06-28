# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:22:44 2022

@author: kikic
"""

from one import dataPreprocess
from functools import reduce
import json
import argparse

# unique neighbor list
def uniqueNeighborList(data):
    uniq_neigbor=list(set(d['neighborhood'] for d in data))
    return uniq_neigbor

# data for all unique neighborhoods as a list of dictionaries
def uniqueNeigborData(data, lst):
    for name in lst:
        uniq_neigbor_data = list(filter(lambda r: r['neighborhood'] == name, data))
    return uniq_neigbor_data

def averageTime(column, data):
    return reduce(lambda result, r: result+float(r[column]), data, 0) / len(data)

def neigborAvgTime(lst1, lst2):
    d1 = dict()
    for name in lst1:
        d2 = dict()
        for d in lst2:
            if d['neighborhood'] == name:
                d2['average_response_time'] = averageTime('totalresponsetime', lst2)
                d2['average_dispatch_time'] = averageTime('dispatchtime', lst2)
                d2['average_total_time'] = averageTime('totaltime', lst2)
                d1[name]=d2
    return d1

def jsonOutput(input_file,output_file):
    with open(output_file,'w') as outputfile:
        outputfile.write(json.dumps(input_file, indent=1))


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-input_filename",type=str,required=False)
    parser.add_argument("-output_filename",type=str,required=False)
    args=parser.parse_args()
    
    clean=dataPreprocess(args.input_filename)
    uniq_neigbor_list=uniqueNeighborList(clean)
    data2=uniqueNeigborData(clean, uniq_neigbor_list)
    jsonOutput(data2,args.output_filename)