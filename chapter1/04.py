def main():
  giv_str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. '\
            'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
  wor_lis = giv_str.replace(',', '').replace('.', '').split(' ')
  ext_dic = {wor_lis[i][0] if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]\
              else wor_lis[i][:2]: i +1 for i in range(len(wor_lis))}
  print(ext_dic)

if __name__ == "__main__":
  main()