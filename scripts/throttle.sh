#!/bin/bash
DEV=lo
if [ "$1" == "del" ]
then
	sudo tc qdisc del dev $DEV root
fi

if [ "$1" == "lan" ]
then
sudo tc qdisc del dev $DEV root
sudo tc qdisc add dev $DEV root handle 1: tbf rate 2320mbit burst 100000 limit 10000
sudo tc qdisc add dev $DEV parent 1:1 handle 10: netem delay 0msec
fi
if [ "$1" == "wan" ]
then
sudo tc qdisc del dev $DEV root
sudo tc qdisc add dev $DEV root handle 1: tbf rate 200mbit burst 100000 limit 10000
sudo tc qdisc add dev $DEV parent 1:1 handle 10: netem delay 10msec
fi