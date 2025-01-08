# key.txt 파일을 기반으로 복호화 매핑 생성
def make_reverse_mapping(key_file):
    try:
        # key.txt 파일 읽기
        with open(key_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 반전된 알파벳 매핑 생성
        new_order = [line.split('=')[0].strip() for line in lines]  # key.txt에서 알파벳 순서 추출
        reverse_mapping = {new_order[i]: chr(i + ord('a')) for i in range(26)}  # 대칭 매핑 반전

        return reverse_mapping
    except Exception as e:
        print(f"매핑 생성 오류: {e}")
        return None


# 복호화 함수
def decrypt_file(encrypted_file, output_file, reverse_mapping):
    try:
        with open(encrypted_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()  # 암호화된 내용 소문자로 변환

        # 복호화 진행
        decrypted = ''.join([reverse_mapping.get(c, c) for c in text])  # 반전 매핑을 사용해 변환

        # 복호화된 내용을 파일에 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted)
        print(f"{output_file}에 복호화된 텍스트 저장 완료")
    except Exception as e:
        print(f"복호화 오류: {e}")


# 복호화 실행
if __name__ == "__main__":
    source = 'encrypted.txt'  # 암호화된 파일
    key_file = 'key.txt'  # 키 파일
    target = 'decrypted.txt'  # 복호화된 결과 파일

    # 반전된 매핑 생성 및 복호화 실행
    reverse_mapping = make_reverse_mapping(key_file)
    if reverse_mapping:
        decrypt_file(source, target, reverse_mapping)
