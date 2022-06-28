# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:30:20 2022

@author: kikic
"""

import csv
from functools import reduce
import argparse

def dataPreprocess(filename):
    try:
        reader = csv.DictReader(open(filename,encoding='utf-8-sig')) # encoding removes 'ï»¿'
        data = list(reader)
        
        cleaned_data=list(filter(lambda d: d['zip_code']!=0 and 
                                        d['neighborhood']!='' and 
                                        d['totalresponsetime']!='' and 
                                        d['dispatchtime']!='' and 
                                        d['totaltime']!='', data))
        
        return cleaned_data
    except FileNotFoundError as e:
        print (e)

def averageResponse(data):
    print('Average response time: ', reduce(lambda result, r: result+float(r['totalresponsetime']), data, 0) / len(data))
    
def averageDispatch(data):
    print('Average dispatch time: ', reduce(lambda result, r: result+float(r['dispatchtime']), data, 0) / len(data))
    
def averageTotal(data):
    print('Average total time: ', reduce(lambda result, r: result+float(r['totaltime']), data, 0) / len(data))
    
                                                                                                        
    
                                                                                                        
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-filename',help='Prints the supplied argument.',type=str)   
    parser.add_argument('-option',help='Prints the supplied argument.',type=int, default=0)
    args=parser.parse_args()
    
    clean=dataPreprocess(args.filename)
    
    if args.option == 0:
        averageResponse (clean)
    elif args.option == 1:
        averageDispatch (clean)
    elif args.option == 2:
        averageTotal (clean)
    else:
        print('Invalid option, please select from 0, 1, or 2')
    