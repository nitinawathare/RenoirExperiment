#!/bin/bash
for run in {1..100}
do
  # shuf -n165 /home/user/newdependencyData | awk -F, '{printf "%.0f\n", $2}'| awk '{ sum += $1; n++ } END { if (n > 0) print sum / n; }'
  ls;
  echo "*******"
done