def func9(arg87, arg88):
    var93 = func10(arg87, arg88)
    result = arg87 ^ var93 & arg87
    return result
def func10(arg89, arg90):
    var91 = 0
    for var92 in [arg90 | arg90 + var91 ^ i for i in range(45)]:
        var91 += arg90 + -10
    return var91
def func8(arg61, arg62):
    var63 = (785 ^ 17750074 & arg61) + -648
    var64 = -810 | -284
    if var64 < arg62:
        var65 = var63 & 1128383774
    else:
        var65 = arg61 ^ arg61
    var66 = -719025729 ^ (arg62 | arg62 ^ arg62)
    var67 = ((arg61 & arg61) ^ 656) + var66
    if arg61 < var64:
        var68 = -1021520333 & var66
    else:
        var68 = var64 | var64
    var69 = var66 + (var64 & var66 - var63)
    var70 = var67 | var64 | arg61 - var63
    var71 = -624279381 + var63
    var72 = 497187712 & -671016832 + var66
    var73 = -16297113 ^ var66 & 2038787872 - var72
    var74 = (-517366799 - (arg61 & -1499785964)) - var67
    var75 = var73 | (769 & var69 + arg61)
    var76 = (var74 | (var69 - var75)) + var69
    var77 = var64 ^ (var66 | arg62) & var74
    var78 = var72 - 1670808776
    var79 = var78 & var70
    var80 = var77 | arg62 & var73 - var66
    var81 = var77 | ((var78 + var70) & 880)
    var82 = var76 ^ var72
    var83 = var81 & var82
    var84 = var78 | (var79 - var82 ^ 1320603181)
    var85 = var83 | (var79 - arg61) | var73
    var86 = (var71 | arg62) & arg61
    result = var70 | var76
    return result
def func5(arg36, arg37):
    var42 = func6(arg36, arg37)
    var47 = func7(var42, arg36)
    var48 = arg36 - (172 - var42 & 950)
    var49 = 740856659 ^ var48
    var50 = -725098199 & var42 + arg36 | var49
    var51 = ((var42 & var49) + var42) | var49
    var52 = arg36 | var49 & var49 & var49
    var53 = 275 - var50 & arg37 ^ var42
    var54 = var51 + (var42 + arg36) ^ var53
    var55 = arg37 + var47 & 427450984 | var52
    var56 = var55 | arg36 | var48
    var57 = (var56 | arg37 + arg37) ^ var53
    var58 = var51 + var53 ^ arg36 & var50
    var59 = var51 ^ var56 & var51 & var47
    var60 = var51 & ((var50 + var50) & arg36)
    result = var57 - var50
    return result
def func7(arg43, arg44):
    var45 = 0
    for var46 in xrange(23):
        var45 += var45 ^ var46
    return var45
def func6(arg38, arg39):
    var40 = 0
    for var41 in xrange(19):
        var40 += var40 ^ arg38 + arg38
    return var40
def func1(arg1, arg2):
    var11 = var5(arg2, arg1)
    var12 = (632090877 + 659) & -846539450 ^ var11
    var13 = (867 & (arg1 | var12)) + var11
    var14 = var11 - (-832981308 - var12) ^ arg1
    var15 = (var13 + -31 + var14) | 476
    var16 = -942 | -1000
    if var16 < var16:
        var17 = arg1 | var15 - var14
    else:
        var17 = var16 | 1100614846 ^ arg1 - var12
    var18 = (var13 & var11) ^ var16 & var11
    var19 = ((var11 - 1574919981) + var18) + var13
    var20 = var11 | var11 | var12 - var11
    var21 = ((713 + var13) - var16) + var20
    var22 = (var11 | var16 + var12) + var13
    var23 = (var14 - var13 - var20) & -606
    var24 = var19 & var20 ^ var23 | var18
    var25 = arg1 ^ var14 & arg2 + var13
    if var19 < var13:
        var26 = var20 - ((arg2 ^ var11) - var16)
    else:
        var26 = (var18 - (var21 | var15)) | var19
    var27 = var14 & (var21 + var15 | var16)
    var28 = (var12 - var11 | var23) + var12
    var29 = (arg1 & var16) - 571096960 - var12
    if var20 < var12:
        var30 = var16 & var16
    else:
        var30 = 1090879795 - var25
    var31 = (var24 - var27) & var23
    var32 = var19 & var29
    var33 = (-1481630403 | var21 & var27) & var27
    var34 = var19 & (var18 | var24) - var24
    var35 = -470 | (var18 & var20) ^ var21
    result = var16 | var23 & var28
    return result
def func4(arg6, arg7):
    var8 = 306 - (arg7 - arg7)
    var9 = -889 & arg7
    var10 = (162 + 122271973) & var9
    result = var8 + arg7 & (arg6 | 214 - arg7 + var10 ^ ((var10 | var10 + var9) - var10 ^ var9) & 1853644917)
    return result
def func3():
    closure = [5]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 5'
    print 'arg_number: 36'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 3'
    print 'func_number: 8'
    print 'arg_number: 61'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
    print 'prog_size: 3'
    print 'func_number: 9'
    print 'arg_number: 87'
    for i in xrange(25000):
        x = 5
        x = func8(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 94'
    for i in xrange(25000):
        x = 5
        x = func9(x, i)
        print x,
