'''
--Source--
python-sentianalysis-id/stopwordsID.txt at master · yasirutomo/python-sentianalysis-id (github.com)
'''
stopword_list = open("stopwords.txt").readlines()
stopword_list = list(map(lambda s: s.strip(), stopword_list))
