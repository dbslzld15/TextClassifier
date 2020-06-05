from konlpy.tag import Okt
from gensim.models import Word2Vec
import csv

"""
@author: lumyjuwon
"""

twitter = Okt()

file = open("텍스트_형용사_notnull.csv", 'r', encoding='euc-kr')
line = csv.reader(file)
token = []
embeddingmodel = []

for i in line:
    content = i[1]  # csv에서 뉴스 제목 또는 뉴스 본문 column으로 변경
    sentence = twitter.pos(i[1], norm=True, stem=True)
    temp = []
    temp_embedding = []
    all_temp = []
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category = i[0]  # csv에서 category column으로 변경
    category_number_dic = {'단맛': 0, '신맛': 1, '매운맛': 2, '담백한맛': 3, '감칠맛': 4, '식감': 5,
                           '온': 6, '냉': 7, '가성비': 8,'감성': 9, '활동적인': 10,
                           '조용한': 11, '교훈적인': 12, '데이트': 13}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp)
print("토큰 처리 완료")

embeddingmodel = []
for i in range(len(token)):
    temp_embeddingmodel = []
    for k in range(len(token[i][0])):
        temp_embeddingmodel.append(token[i][0][k])
    embeddingmodel.append(temp_embeddingmodel)
embedding = Word2Vec(embeddingmodel, size=300, window=5, min_count=10, iter=5, sg=1, max_vocab_size=360000000)
embedding.save('post.embedding')
