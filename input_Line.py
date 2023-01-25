import sys

list1=[] #이차원 리스트로 저장하기위한 공간
rotation=0 # 몇줄 입력받을 건지

#map함수로 숫자자료형으로 한줄씩 리스트로 묶여 list1에 저장되며 최종적으로 이차원 리스트가 만들어진다
for i in range(rotation):
    list1.append(list(map(int, sys.stdin.readline().split())))