"""전부 1로 바꾸는 경우와 0으로 바꾸는 경우 중, 적은 변경 횟수 출력
"""
def reverse_str(input_):

    cnt_cvt_0, cnt_cvt_1 = 0, 0
    
    if input_[0] == "1":
        cnt_cvt_0 += 1
    else:
        cnt_cvt_1 += 1

    # 0으로 바꿀 때
    for i in range(len(input_)-1):
        if input_[i] != input_[i+1]:
            if input_[i+1] == "1":
                cnt_cvt_0 += 1
            else:
                cnt_cvt_1 += 1
    output = min(cnt_cvt_0, cnt_cvt_1)
    
    return output

if __name__ == "__main__":
    input_ = "1110011"
    output = reverse_str(input_)
    print(output)