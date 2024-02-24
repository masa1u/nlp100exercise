def main():
  giv_str = 'Now I need a drink, alcoholic of course,'\
            'after the heavy lectures involving quantum mechanics.'
  wor_lis = giv_str.replace(',', '').replace('.', '').split(' ')
  len_lis = []
  for word in wor_lis:
     len_lis.append(len(word))
  print(len_lis)

if __name__ == "__main__":
  main()