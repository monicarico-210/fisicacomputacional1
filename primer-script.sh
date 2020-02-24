#!/bin/bash

for i in $(seq 1 10);do
  if [ "$i" == 1 ]; then
  echo "hola id-$i"
else
  echo "jum, tarde id-$i"
fi
done
echo " final, chao"
