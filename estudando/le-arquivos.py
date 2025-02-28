f = open('file.txt', 'r')

# # Iterando linha por linha
# for l in f:
#     print(l, end='')

txt = f.readlines()
print(type(f))