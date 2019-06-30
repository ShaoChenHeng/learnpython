try:
    f = open('/home/scheng/PYcode/bfs_test/input.txt', 'r')
    print('text is reading..\n')
    print(f.read())
    print('\n')
    print('text printed')

finally:
    if f:
        f.close()

print('another version\n')

with open('/home/scheng/PYcode/bfs_test/input.txt','r') as f:
    print('text is reading..\n')
    print(f.read())
    print('\n')
    print('text printed')


with open('/home/scheng/PYcode/bfs_test/input.txt','w') as f:
   f.write('aaaaa')

# f = open('/home/scheng/PYcode/bfs_test/input.txt', 'w')
# f.write('Hello, world!')
# f.close()


