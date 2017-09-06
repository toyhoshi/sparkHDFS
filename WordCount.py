#!/usr/bin/env python
import findspark
findspark.init()

from operator import add
from pyspark import SparkContext
from pyspark import SparkConf

    sc = SparkContext(appName="WordCount")
    lines = sc.textFile("hdfs:///marco/README.txt")
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print str(word) +": "+ str(count);

    sc.stop()
