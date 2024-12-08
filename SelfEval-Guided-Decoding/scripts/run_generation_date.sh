#!/bin/bash

set -x

split=test
dtname=date_understanding

mkdir -p ${OUTPUTHOME}

cd ${EXEHOME}


python generate_code.py \
    --dt_name ${dtname} \
    --input_file ${DATAHOME}/${dtname}_${split}.jsonl \
    --output_dir ${OUTPUTHOME} \
    --use_mini_n --mini_n_samples 8 --max_tokens 256 \
    --sleep_time 5 \
    --reject_sample --bs_min_score 0.5 \
    --bs_temperature 0.0 \
    --temperature 0.1 --n_samples 16 --conf_ratio 0
