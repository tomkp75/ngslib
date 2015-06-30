#!/usr/bin/python
#Last-modified: 18 Mar 2014 03:55:46 PM

#         Module/Scripts Description
# 
# Copyright (c) 2008 Yunfei Wang <yfwang0405@gmail.com>
# 
# This code is free software; you can redistribute it and/or modify it
# under the terms of the BSD License (see the file COPYING included with
# the distribution).
# 
# @status:  experimental
# @version: 1.0.0
# @author:  Yunfei Wang
# @contact: yfwang0405@gmail.com

# ------------------------------------
# python modules
# ------------------------------------

import sys
import string
import pysam

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__=="__main__":
    if len(sys.argv)==1:
        sys.exit("Example:"+sys.argv[0]+" input.sam/bam unique.bam ")
    if sys.argv[0].endswith('sam'):
        sam=pysam.Samfile(sys.argv[1])
    elif sys.argv[0].endswith('bam'):
        sam = pysam.Samfile(sys.argv[1], 'rb')
    else:
        sys.exit("File type is not supported.")
    outsam=pysam.Samfile(sys.argv[2],'wb',template=sam)
    lastid=""
    lastcnt=0
    
    for read in sam:
        if read.qname!=lastid:
            if lastcnt==1:
                outsam.write(lastread)
            lastid=read.qname
            lastcnt=1
            lastread=read
        else:
            lastcnt+=1
    if lastcnt==1:
        outsam.write(lastread)
    
    sam.close()
    outsam.close()


