def main(input_):
    lines = input_.split('\n')
    n_students = lines[0]
    scores_ = list(map(lambda x: x.split(' '), lines[1:]))
    scores = {name: int(score) for name, score in scores_}
    scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    return ' '.join(scores.keys())

if __name__ == '__main__':
    input_ = '''2
홍길동 95
이순신 77'''
    output = main(input_)
    print(output)