#!/bin/bash
for i in $(seq 0 0.5 30); do
  echo | awk -v t=$i '{print 100 -5*t*t}'
done

