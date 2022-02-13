from unittest import TestCase, main

def compress_str(input_):

    input_len = len(input_)  
    max_unit_len = input_len//2 
    output = len(input_)

    for unit_len in range(1, max_unit_len + 1):

        pre_unit = input_[:unit_len]
        cnt = 1
        compressed_str = ''

        for pos in range(unit_len, input_len, unit_len):
            post_unit = input_[pos:pos+unit_len]

            if pre_unit == post_unit:
                cnt += 1
            
            else:
                compressed_str += str(cnt) + pre_unit if cnt > 1 else pre_unit
                pre_unit = input_[pos:pos+unit_len]
                cnt = 1
            
        compressed_str += str(cnt) + pre_unit if cnt > 1 else pre_unit
        output = min(output, len(compressed_str))
        
    return output

class UnitTester(TestCase):
    
    def testcase01(self):
        input_ = 'aabbaccc'
        output = compress_str(input_)
        print(input_, output)

    def testcase02(self):
        input_ = 'ababcdcdababcdcd'
        output = compress_str(input_)
        print(input_, output)

    def testcase03(self):
        input_ = 'abcabcdede'
        output = compress_str(input_)
        print(input_, output)

    def testcase04(self):
        input_ = 'abcabcabcabcdededededede'
        output = compress_str(input_)
        print(input_, output)

    def testcase05(self):
        input_ = 'xababcdcdababcdcd'
        output = compress_str(input_)
        print(input_, output)

    def testcase06(self):
        input_ = 'abcabcdede'
        output = compress_str(input_)
        print(input_, output)

    def testcase07(self):
        input_ = 'ababcdcdababcdcd'
        output = compress_str(input_)
        print(input_, output)   

if __name__ == '__main__':

    main()