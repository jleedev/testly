#!/bin/bash

cd "$(dirname "$0")"

if python testly.py
then
	echo Testly ran successfully
else
	echo Testly reported an error
fi
