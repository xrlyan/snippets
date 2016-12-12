#!/bin/bash

## no space between numbers
val1=2;
val2=5;

let res=val1+val2

echo $res
echo ${#res}

let res++
echo $res


