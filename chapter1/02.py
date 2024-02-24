def main():
  giv_str1 = 'パトカー'
  giv_str2 = 'タクシー'
  joi_str = ''
  for i in range(max([len(giv_str1), len(giv_str2)])):
    joi_str += giv_str1[i] + giv_str2[i]
  print(joi_str)

if __name__ == "__main__":
  main()