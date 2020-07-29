# # 문제 제목 : SHA -256
# # 문제 난이도 : 하
# # 문제 유형 : 해시, 구현
# # 추천 풀이 시간 15분
#
#
# 1. hashlib의 sha256 함수를 이용하면 sha 256 해시를 구할 수 있다.
# 2. hashlib.sha256(문자열의 바이트 객체).hexdigest(): 해시 결과 문자열


import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result) # e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855