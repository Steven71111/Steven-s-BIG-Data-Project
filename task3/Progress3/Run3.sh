hadoop jar /home/uic/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/mapper3.py -mapper /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/mapper3.py \
-file /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/reducer3.py -reducer /home/uic/Steven-s-BIG-Data-Project/task3/Progress3/reducer3.py \
-input /output/project/task3/step2/part-00000 -output /output/project/task3/step3