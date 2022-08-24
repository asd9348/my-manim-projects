#
# def bit_string_to_mobject(bit_string):
#     line = Tex("0" * 32)
#     pre_result = VGroup(*[
#         line.copy() for row in range(8)
#     ])
#     pre_result.arrange(DOWN, buff=SMALL_BUFF)
#     result = VGroup(*it.chain(*pre_result))
#     result.scale(0.7)
#     bit_string = (256 - len(bit_string)) * "0" + bit_string
#     result
#
#     for i, (bit, part) in enumerate(zip(bit_string, result)):
#         if bit == "1":
#             one = Tex("1")[ 0 ]
#             one.replace(part, dim_to_match=1)
#             result.submobjects[ i ] = one
#
#     return result
#

def sha256_bit_string(message):
    hexdigest = sha256(message.encode('utf-8')).hexdigest()
    return bin(int(hexdigest, 16))[ 2: ]

def msg_to_mob(msg, width, rows, buff=0.2):
    if rows % 2 != 0:
        raise Exception('2의 배수가 아닙니다.')

    msg = sha256_bit_string(msg)

    half_rows = int(rows / 2)
    i = 0
    chopped_list = [ msg[ i: i + width ] for i in range(0, len(msg), width) ]
    starts = chopped_list[ :half_rows - 1 ]
    ends = chopped_list[ -half_rows - 1: ]

    starts.extend(ends)
    starts.insert(half_rows, r"\vdots")

    mobs = VGroup()
    for row in range(rows + 1):
        mobs.add(MathTex(starts[ row ]))
        # if row= half_rows:
        # mobs.add(MathTex(""))

    mobs.arrange_in_grid(6, 1, buff=buff)

    return mobs

