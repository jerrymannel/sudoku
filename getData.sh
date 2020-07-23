#!/bin/bash

rm data.out || true
for i in {1..100}
do
  curl https://sudoku.com/api/getLevel/easy -s | cut -f2 -d[ | cut -f1,2 -d, >> data.easy.out
  curl https://sudoku.com/api/getLevel/medium -s | cut -f2 -d[ | cut -f1,2 -d, >> data.medium.out
  curl https://sudoku.com/api/getLevel/hard -s | cut -f2 -d[ | cut -f1,2 -d, >> data.hard.out
  curl https://sudoku.com/api/getLevel/expert -s | cut -f2 -d[ | cut -f1,2 -d, >> data.expert.out
done