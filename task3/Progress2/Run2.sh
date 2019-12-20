hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/mapper2.py -mapper /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/mapper2.py \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/reducer2.py -reducer /home/uic/Steven-s-BIG-Data-Project/task3/Progress2/reducer2.py \
-input /output/project/task3/step1/part-00000 -output /output/project/task3/step2
