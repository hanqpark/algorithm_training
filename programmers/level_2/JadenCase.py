''' Python 문자열 함수 정리해 둔 사이트
    https://jimmy-ai.tistory.com/62
    
    1. 대소문자 변환: str.upper(), str.lower(), str.title(), str.capitalize()
    2. 탐색: str.count(), str.find(), str.index()
    3. 구성 파악: str.isdigit(), str.isalpha(), str.isupper(), str.islower()
    4. 공백 제거: str.strip(), str.rstrip(), str.lstrip()
    5. 기타: str.replace('a', 'b'), str.split(), str.join()
'''

def solution(s):
    # return s.title() -> 3People~ 이런식으로 돼서 오류 뜸
    return " ".join([st.capitalize() for st in s.split(" ")])