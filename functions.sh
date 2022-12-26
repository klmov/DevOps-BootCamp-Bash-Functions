#!/bin/bash
pow() {
echo $(($1**$2))
}
shortest() {
shortestArg=$(echo "${@}" | awk '{split($0,str," "); for (i in str) print length(str[i])}' | sort -n | head -n1)
for i in "$@"
 do
  if [[ "${#i}" -eq "$shortestArg" ]]
  then
   echo "$i" 
  fi
 done
}
print_log() {
echo "$(date +[\%Y-\%m-\%d" "\%R]) $@"
}
