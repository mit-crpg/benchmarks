#!/usr/bin/env bash

cd pin
python build-xml-pin.py
openmc > results.txt

cd ../2d
python build-xml-2d.py
openmc > results.txt

cd ../3d
python build-xml-3d.py
openmc > results.txt

cd ../unrodded
python build-xml-unrodded.py
openmc > results.txt

cd ../rodded-A
python build-xml-rodded-A.py
openmc > results.txt

cd ../rodded-B
python build-xml-rodded-B.py
openmc > results.txt
