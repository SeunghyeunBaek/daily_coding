
def main(input_:str):

    half_len = len(input_) // 2
    left = input_[:half_len]
    right = input_[half_len:]

    left_sum, right_sum = 0, 0

    for i in left:
        left_sum += int(i)

    for i in right:
        right_sum += int(i)

    res = 'LUCKY' if left_sum == right_sum else "READY"
    return res

def main(input_:str):
    mid = len(input_) // 2
    left_sum, right_sum = 0, 0 
    
    for i in range(mid):
        left_sum += int(input_[i])
        right_sum += int(input_[mid+i])

    res = 'LUCKY' if left_sum == right_sum else "READY"
    return res

if __name__ == '__main__':
    
    inputs = ['123402', '7755']

    for input_ in inputs:

        print(main(input_))