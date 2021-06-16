# lang 변수에 들어온 문자열이 "안녕" 이라면 콘솔창에 "한국어"
# 로 출력을, "헬로"라면 "영어"를, "니하오"라면 "중국어"를
# "싸왓디" 라면 "태국어"를 출력하도록 if~elif 문을 작성해주세요

print("단어를 입력하세요")
print("안녕, 헬로, 니하오, 사왓디")
lang = input("> ")

if lang == "안녕":
    print("한국어")
elif lang == "헬로":
    print("영어")
elif lang == "니하오":
    print("중국어")
elif lang == "싸왓디":
    print("태국어")