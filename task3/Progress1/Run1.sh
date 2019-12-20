hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/mapper1.py -mapper /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/mapper1.py \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/reducer1.py -reducer /home/uic/Steven-s-BIG-Data-Project/task3/Progress1/reducer1.py \
-input /data/project/* -output /output/project/task3/step1