s = input()

def compress(s):
    answer = len(s)
    #1개 단위부터(step) 압축단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서 step만큼 추출
        count = 1
        # 단위 크기(step)만큼 증가하면서 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        # 남은 문자열에 대해 처리
        compressed += str(count) + prev if count >= 2 else prev # 15 ~ 18 코드와 동일
        answer = min(answer, len(compressed))
    return answer

print(compress(s))