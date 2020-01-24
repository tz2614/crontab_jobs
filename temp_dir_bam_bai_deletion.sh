#!/bin/bash

# deletion of .bam and .bam.bai files in /mnt/cmftgen5/temp/

module add apps/python/2.7.8/gcc-4.8.5

ft1=".bam"
ft2=".bai"
ft3=".log"
date_time=$(date -I)

script_path="/users/tz1/bin/crontab/file_deletion.py"
# WHEN TESTING change the following dir
# tmp_dir="/mnt/cmftgen5/temp/"

# test dir containing dummy data
tmp_dir="/mnt/repository/Bioinformatics/tengyue_zheng_projects/crontab/test_data/"

duration="90"
action=".deletion"

log_fp1=$tmp_dir$date_time$ft1$action$ft3
log_fp2=$tmp_dir$date_time$ft1$ft2$action$ft3

#echo $log_fp1
#echo $log_fp2

# WHEN READY UNCOMMENT THE  FOLLOWING TO START EXECUTING THE PYTHON SCRIPT
python $script_path $tmp_dir $ft1 $duration $log_fp1
python $script_path $tmp_dir $ft1$ft2 $duration $log_fp2