## Crontab jobs
  - By Tengyue Zheng
  - 24/01/2020
  email: tengyue.zheng@mft.nhs.uk

## Description
  
  Regular jobs to do on the cluster, put into /etc/cron.daily or /etc/cron.weekly /etc/cron.monthly

## Getting Started

  1. Format of crontab files:
  ```Bash
  59 23 31 12 7 tz1 /users/tz1/bin/crontab/temp_dir_bam_bai_deletion.sh
  ```
  MIN HOUR DM MONTH DW USER FULL_PATH_TO_PROGRAM

## Prerequisites
  1. Make sure you have all the dependencies for your program loaded either in your script or beforehand

  2. Perform a thorough code review for the script before setting the crontab for the job

  3. for instructions on how to set the crontab job, visit
  - URL: https://linuxconfig.org/linux-crontab-reference-guide

## Main scripts:
  - /users/tz1/bin/crontab/file_deletion.py
  - /users/tz1/bin/crontab/temp_dir_bam_bai_deletion.sh

## Unit testing scripts:
  
  
## Reference files


## User Requirements:

  1. Delete all '.bam' and 'bam.bai' in /mnt/cmftgen5/temp/

## Instructions:

  1. Put requirements under the "User Requirements:"
  E.g. see above
  
  2. Load dependencies

  ```Bash
  $ module load apps/python/2.7.8/gcc-4.8.5
  ``` 
  3. Test your script

  ```Bash
  $ python /users/tz1/bin/crontab/file_deletion.py /mnt/cmftgen5/temp/ .bam 90 /mnt/repository/Bioinformatics/tengyue_zheng_projects/crontab/2020-01-24.bam.bai.deletion.log

  $ sh /users/tz1/bin/crontab/temp_dir_bam_bai_deletion.sh
  ```

  4. Set crontab job
  ```Bash
  $ cd /etc/cron/.d
  $ sudo crontab -e 
  $ 00 00 01 * * tz1 /users/tz1/bin/crontab/temp_dir_bam_bai_deletion.sh
  ```
  5. Check the output of crontab job

  It should display the information on terminal:

  ```Bash
  $ list of files in /mnt/cmftgen5/temp/ generated
  $ file type: .bam
  $ START checking modified date of each file:
  $ over_duration: 2017-04-24 16:40:51.991517 /mnt/cmftgen5/temp/AZ_project/WS64688/118BM13.sorted.nodup.bam
  $ over_duration: 2017-04-24 16:41:36.413676 /mnt/cmftgen5/temp/AZ_project/WS64688/142M13B.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:16.582681 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ1.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:09.895652 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ10.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:10.692471 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ11.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:10.989325 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ12.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:11.629905 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ13.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:12.223613 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ14.sorted.nodup.bam
  $ over_duration: 2014-06-11 14:24:12.645458 /mnt/cmftgen5/temp/Andrew/AZ/WS59488/AZ15.sorted.nodup.bam
  $ ...
  $ check COMPLETE
  $ LOG for modified dates and file paths created: /mnt/repository/Bioinformatics/tengyue_zheng_projects/crontab/2020-01-24.bam.bai.deletion.log
  ```

6. When the job is completed, check that log files have been generated.
   If in doubt consult Tengyue Zheng or senior member of the bioinformatics team.

   ```Bash
   $ less /users/tz1/crontab/2020-01-24.bam.bai.deletion.log
   ```

   You should see the outputs as above
