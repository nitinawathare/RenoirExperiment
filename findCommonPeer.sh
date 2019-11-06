#!/bin/bash


trust_file=pList1
ip_file=pList2

while ip= read -r line
do
       test=`grep -w "$line" $ip_file`
       # echo " "
       if [ "$ip" = "$test" ] ; then
           echo "$line" 
      
       fi
done < "$trust_file"