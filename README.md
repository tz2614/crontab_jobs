## Crontab jobs
  - By Tengyue Zheng
  - 07/02/2020
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

  1. Delete all '.bam' and 'bam.bai' in <path/to/dir>

## Instructions:

  1. Put requirements under the "User Requirements:"
  E.g. see above
  
  2. Load dependencies

  ```Bash
  $ module add apps/python/2.7.8/gcc-4.8.5
  ``` 
  3. Test your script

  ```Bash
  $ python crontab_jobs/file_deletion.py <path/to/dir> .bam 90 <path/to/dir>/2020-01-24.bam.deletion.log

  $ sh crontab_jobs/temp_dir_bam_bai_deletion.sh
  ```

  4. Set crontab job
  ```Bash
  $ cd /etc/cron/.d
  $ sudo crontab -e 
  $ 00 00 01 * * tz1 crontab/temp_dir_bam_bai_deletion.sh
  ```
  5. Check the output of crontab job

  It should display the information on terminal:

  ```Bash
  $ CORRECT tmp_dir: /mnt/cmftgen5/temp/
  $ file types: ['.bam', '.bam.bai', '.bai']
  $ generate a list of files with above file types
  $ list of files in /mnt/cmftgen5/temp/ generated
  $ CORRECT dirpath: /mnt/cmftgen5/temp/APC/
  $ CORRECT dirpath: /mnt/cmftgen5/temp/APC_MUTYH/
  $ CORRECT dirpath: /mnt/cmftgen5/temp/BEST1_LLM/
  $ CORRECT dirpath: /mnt/cmftgen5/temp/BRCA/
  $ CORRECT dirpath: /mnt/cmftgen5/temp/Breast_cancer_LLM/
  $ ...
  $ CORRECT dirpath: /mnt/cmftgen5/temp/X_linked_RP_LLM/
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
  $ LOG for modified dates and file paths created: <root/path>/crontab_jobs/2020-01-24.bam.bai.deletion.log```

6. When the job is completed, check that log files have been generated.
   If in doubt consult Tengyue Zheng or senior member of the bioinformatics team.

   ```Bash
   $ less <path/to/dir>/2020-01-24.bam.bai.deletion.log
   ```

   You should see the outputs as above
