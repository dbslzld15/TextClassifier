## BiLSTM을 이용한 음식점 리뷰 분류 감성분석 모델

### 텍스트 형용사 분류 
* ``` 단맛, 신맛, 매운맛, 담백한맛, 감칠맛, 식감, 온, 냉, 가성비, 감성, 활동적인, 조용한, 교훈적인, 데이트```
* 총 14가지의 형용사 분류

### 필요 패키지
* konlpy: https://hyrama.com/?p=456
* gensim: https://hyrama.com/?p=456
* tensorflow: 1.15.2 버전

### 사용법
* unify.py 실행 후 shuffle.py 실행 후 csvDeleteNull.py 실행
* CsvWord2Vec.py 실행 후 나온 post.embedding 파일을 Bi_LSTM/.Data 폴더 안에 붙여 넣어줌
* Bi_LSTM_csv_train.py 실행 후 Bi_LSTM 모델을 Bi_LSTM/.Data 폴더 안에 넣어줌 
* Classifier.py 실행
* 각각의 코드에서 커스텀 해서 사용

### 성능
* F1 Score : 90.93%
* Accuracy : 91%

### HELP
* https://github.com/MSWon/Sentimental-Analysis
