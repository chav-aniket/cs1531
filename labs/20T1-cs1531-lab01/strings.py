'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']

ret = ''
for word in strings:
    ret+=word
    ret+=' '
print(ret.strip())
print(' '.join(strings))