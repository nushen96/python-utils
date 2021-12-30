def analyze(s):
    f=[9.42,1.02,2.64,3.39,15.87,0.95,1.04,0.77,8.41,0.89,0.00,5.34,3.24,7.15,5.14,2.86,1.06,6.46,7.90,7.26,6.24,2.15,0.00,0.30,0.24,0.32]
    df = dict(sorted(list(zip("abcdefghijklmnopqrstuvwxyz",f)),key=lambda x:x[1],reverse=True))
    d=dict(sorted([(x,s.count(x)) for x in set(s)],key=lambda l:l[1],reverse=True))
    del d[' ']
    l = list(df.keys())
    r={}
    for x in d.keys():
        r[x]=l.pop(0)
    result=''
    for x in s:
        result += r[x] if x!=" " else x
    return result

s='lzfwb cmmyt upuhn xyjul nuayl xymch zilgu ncihm myhmc vfym'
print(analyze(s))