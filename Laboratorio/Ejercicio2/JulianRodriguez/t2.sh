#!/bin/bash

wget http://openmv.net/file/room-temperature.csv

mkdir Dir_Room
mv room-temperature.csv Dir_Room
mv pca_room.py Dir_Room
cd Dir_Room
python pca_room.py
rm -rf Dir_Room
