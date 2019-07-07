class Q2(object):

    TABLE = """
        あ  い  う  え  お  ま  み  む  め  も  や  ゆ
        か  き  く  け  こ  ら  り  る  れ  ろ  よ  わ
        さ  し  す  せ  そ  が  ぎ  ぐ  げ  ご
        た  ち  つ  て  と  ざ  じ  ず  ぜ  ぞ
        な  に  ぬ  ね  の  ば  び  ぶ  べ  ぼ
        は  ひ  ふ  へ  ほ  ぱ  ぴ  ぷ  ぺ  ぽ
    """.split()

    """Q2.

    ここからコードを書く
    """

    def b64encode(binary):
        """
        エンコード関数

        >>> Q2.b64encode('もょもと Lv48'.encode('utf-8'))
        'ふふやうふふやむふふやうふふみじめおばはきえげ'
        >>> Q2.b64encode('悪霊の神々'.encode('euc-jp'))
        'なやひくぱぜるくねぴうごぬこ'
        """
        # TODO: Your code goes here
        str_ascii_list = ['{:0>8}'.format(str(bin(binary[i])).replace('0b', ''))
                          for i in range(len(binary))]

        output_str = ''
        equal_num = 0
        while str_ascii_list:
            temp_list = str_ascii_list[:3]
            if len(temp_list) != 3:
                while len(temp_list) < 3:
                    equal_num += 1
                    temp_list += ['0' * 8]
            temp_str = ''.join(temp_list)
            temp_str_list = [temp_str[x:x + 6] for x in [0, 6, 12, 18]]
            temp_str_list = [int(x, 2) for x in temp_str_list]
            if equal_num:
                temp_str_list = temp_str_list[0:4 - equal_num]
            output_str += ''.join([Q2.TABLE[x] for x in temp_str_list])
            str_ascii_list = str_ascii_list[3:]
        return output_str

    def b64decode(spell):
        """
        デコード関数

        >>> from hashlib import sha1
        >>> spell = (
        ...     "ゆうて" "いみや" "おうきむ"
        ...     "こうほ" "りいゆ" "うじとり"
        ...     "やまあ" "きらぺ" "ぺぺぺぺ"
        ...     "ぺぺぺ" "ぺぺぺ" "ぺぺぺぺ"
        ...     "ぺぺぺ" "ぺぺぺ" "ぺぺぺぺ" "ぺぺ"
        ... )
        >>> sha1(Q2.b64decode(spell)).hexdigest()
        '3d5661aef713bac36801e8a022dd5f549b3583e4'
        """

        base64_bytes = ['{:0>6}'.format(str(bin(Q2.TABLE.index(s))).replace('0b', '')) for s in spell]
        resp = bytearray()
        nums = len(base64_bytes) // 4
        remain = len(base64_bytes) % 4
        integral_part = base64_bytes[0:4 * nums]

        while integral_part:
            tmp_unit = ''.join(integral_part[0:4])
            tmp_unit = [int(tmp_unit[x: x + 8], 2) for x in [0, 8, 16]]
            for i in tmp_unit:
                resp.append(i)
            integral_part = integral_part[4:]

        if remain:
            remain_part = ''.join(base64_bytes[nums * 4:])
            tmp_unit = [int(remain_part[i * 8:(i + 1) * 8], 2) for i in range(remain - 1)]
            for i in tmp_unit:
                resp.append(i)

        return resp

