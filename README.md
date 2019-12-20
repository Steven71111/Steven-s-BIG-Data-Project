# Steven-s-BIG-Data-Project


## Assignment Task

### Task 1
This program is written by Python in Spyder.   
The following steps show the progress which run the python program by hadoop:
```shell script

hadoop fs -mkdir -p /data/project
hadoop fs -put /home/uic/Steven-s-BIG-Data-Project/data/* /data/project

hadoop fs -mkdir -p /output/

chmod +x /home/uic/Steven-s-BIG-Data-Project/task1/mapper.py /home/uic/Steven-s-BIG-Data-Project/task1/reducer.py /home/uic/Steven-s-BIG-Data-Project/task1/run.sh

sh /home/uic/Steven-s-BIG-Data-Project/task1/run.sh
```

Then check for the output:
```shell script
hadoop fs -cat /output/project/task1/part-00000
```

Complete this task, time spent by all maps is 2798265 ms, time spent by all reduces is 2798265 ms.

### Task 2
Run the python program by the shell command:
```shell script

chmod +x /home/uic/Steven-s-BIG-Data-Project/task2/mapper.py /home/uic/Steven-s-BIG-Data-Project/task2/reducer.py /home/uic/Steven-s-BIG-Data-Project/task2/run.sh

sh /home/uic/Steven-s-BIG-Data-Project/task2/run.sh
```

### Task 3

The task3 was finished by 3 steps.

#### Step 1:
```shell script

chmod +x /home/uic/Steven-s-BIG-Data-Project/task3/Progresss1/mapper1.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/reducer1.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/run1.sh


sh /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/run1.sh
```

To see the output:
```shell script
hadoop fs -cat /output/project/task3/step1/part-00000
```

#### Step 2:
```shell script

chmod +x /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/mapper2.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/reducer2.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/run2.sh


sh /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/run2.sh
```

We put the output of Step1 into Step2 to get the output of Step2.

See the output using by:
```shell script
hadoop fs -cat /output/project/task3/step2/part-00000
```

#### Step 3:
```shell script

chmod +x /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/mapper3.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/reducer3.py /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/run3.sh


sh /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/run3.sh
```
We also put the output of Step2 into Step3 to get the output of Step3.

See the output using by:
```shell script
hadoop fs -cat /output/project/task3/step3/part-00000
```
