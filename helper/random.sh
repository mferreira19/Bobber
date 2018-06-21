#!/usr/bin/env bash
echo "time,temp,hum">>~/PycharmProjects/Bobber/HTML/data.csv;
for i in `seq 1 100`; do
  my_random_temp1=$((RANDOM%100))
  my_random_temp2=$((RANDOM%120))
  echo "2018-06-06T11:10:"$i".000Z,$my_random_temp1,$my_random_temp2" >> ~/PycharmProjects/Bobber/HTML/data.csv;
  sleep 2;
done