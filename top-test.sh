#!/bin/sh

if python testly.py
then
	echo Testly ran successfully
else
	echo Testly reported an error
fi
