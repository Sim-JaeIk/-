# key.txt 파일을 읽어서 알파벳 매핑을 만드는 함수
def make_mapping(key_file):
    try:
        # key.txt 파일 읽기
        with open(key_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 알파벳 매핑 생성
        new_order = [line.split('=')[0].strip() for line in lines]  # key.txt에서 알파벳 추출
        mapping = {chr(i + ord('a')): new_order[i] for i in range(26)}  # 알파벳 매핑 생성

        return mapping
    except Exception as e:
        print(f"매핑 생성 오류: {e}")
        return None


# 매핑을 이용해 텍스트 변환
def convert_text(input_file, output_file, mapping):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()  # 소문자로 변환

        # 매핑을 통해 변환
        converted = ''.join([mapping.get(c, c) for c in text])  # 변환

        # 변환된 내용을 파일에 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted)
        print(f"{output_file}에 변환된 텍스트 저장 완료")
    except Exception as e:
        print(f"변환 오류: {e}")


# 실행 부분
if __name__ == "__main__":
    source = 'alphabet.txt'  # 원본 파일
    key_file = 'key.txt'  # 매핑 정보가 담긴 파일
    target = 'encrypted.txt'  # 결과 파일

    # 매핑 생성 및 텍스트 변환
    mapping = make_mapping(key_file)
    if mapping:
        convert_text(source, target, mapping)
