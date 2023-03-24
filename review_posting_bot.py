#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 22:12:19 2023

@author: partaze aka Cheryl
Small script to post reviews to a specified website. It makes use of text files containing the
review, and parses it to the required format.
"""

import os
import requests

def make_dicts(path):
    '''From given path creates a list of files,iterates through them and creates dictionaries'''
    files = []
    for file in os.listdir(path):
        absp = os.path.join(path, file)
        files.append(absp)
        idx=1
    for file in files:
        idx+=1
        with open(file,'r')as f:
            lines = f.readlines()
            rev_dict={}
            rev_dict['id']=idx
            for i in range(len(lines)):
                if i==0:
                    rev_dict['title']=lines[i].strip()
                elif i==1:
                    rev_dict['name']=lines[i].strip()
                elif i==2:
                    rev_dict['date']=lines[i].strip()
                elif i==3:
                    rev_dict['feedback']=lines[i].strip()
                else:
                    rev_dict['feedback']+=lines[i].strip()
            post_to_web(rev_dict)
    
                
def post_to_web(dic):
    '''Posts reviews to a webpage. Displays any error code received.''' 
    response = requests.post('http://34.136.207.140/feedback/', json=dic)
    if response.status_code == '201':
            print("Review successfully uploaded.") 
    else:
            print(response.status_code)                 
                    
if __name__=='__main__':
    path = '/data/feedback'
    make_dicts(path)

    