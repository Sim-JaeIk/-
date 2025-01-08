import string

# alphabet.txt 파일에서 알파벳 빈도를 계산하고 base_key.txt와 key.txt 파일을 생성하는 함수
def generate_keys(input_file, base_key_file, key_file):
    try:
        # 알파벳 카운터
        counts = [0] * 26

        # 파일 읽기
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()  # 소문자로 변환

            # 알파벳 빈도 계산
            for char in text:
                if char in string.ascii_lowercase:
                    idx = ord(char) - ord('a')
                    counts[idx] += 1

        # a~z 순으로 base_key.txt 파일에 저장
        with open(base_key_file, 'w', encoding='utf-8') as f:
            for i in range(26):  # 알파벳 a~z 순으로 기록
                f.write(f"{chr(i + ord('a'))} = {counts[i]}\n")

        # 빈도 순으로 정렬해서 key.txt 파일에 저장
        sorted_idx = sorted(range(26), key=lambda i: counts[i])
        with open(key_file, 'w', encoding='utf-8') as f:
            for i in sorted_idx:  # 빈도 순으로 기록
                f.write(f"{chr(i + ord('a'))} = {counts[i]}\n")

        print(f"{base_key_file} 및 {key_file} 파일이 성공적으로 생성되었습니다.")
    except Exception as e:
        print(f"파일 생성 오류: {e}")

# 실행 부분
if __name__ == "__main__":
    source_file = 'alphabet.txt'  # 원본 파일
    base_key_file = 'base_key.txt'  # a~z 순서로 저장할 파일
    key_file = 'key.txt'  # 빈도 순으로 저장할 파일

    # base_key.txt 및 key.txt 파일 생성
    generate_keys(source_file, base_key_file, key_file)
