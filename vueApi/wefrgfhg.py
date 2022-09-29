import copy
def a():
    # 浅拷贝第一层对象可以完全拷贝，但是子对象不能拷贝内存地址还是一样的
    a={'w':123,'b':34,'t':{'R':'深沉'}}
    v = a.copy()
    c=copy.deepcopy(a)
    print(id(a['t'])==id(v['t']))
    print(id(a)==id(c))
    a['w']=90
    a['t']['R']='变化'
    b = 1
    print(id(a),a)
    print(id(c),c)
    print(__name__)
    # print(id(a['w']))
    # print(id(a['b']))
    # print(id(b))
if __name__=='__main__':
    a()
else:
    print('我被别人调用了')

