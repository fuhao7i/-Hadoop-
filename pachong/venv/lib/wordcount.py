from pyspark import SparkConf, SparkContext





conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext(conf=conf)
inputFile =  "file://home/linziyu/word.txt"
textFile = sc.textFile(inputFile)
wordCount = textFile.flatMap(lambda line : line.split(" ")).map(lambda word : (word, 1)).reduceByKey(lambda a, b : a + b)
wordCount.foreach(print)