import numpy as np
def knearestneighbors(k,x,y,ques):
    eucl_distance = []
    predict = []
    result = x-ques
    # Euclidean Distance calculation
    for i in result:
        eucl_distance.append(np.linalg.norm(i))
    zip_list = list(zip(eucl_distance,y))
    # Sort tuple on the basis of smallest k value
    zip_list.sort(key=lambda elem: elem[0])
    for i,j in zip_list:
        predict.append(j)
    #Extract only k values
    predict = predict[:k]
    #Count the value of 0 and 1
    if predict.count(0)>predict.count(1):
        print("LABEL 0")
    else:
        print("LABEL 1")

a = np.array([[4,7,4],
                  [6,3,7],
                  [7,8,7],
                  [8,9,1],[4,2,2],[7,4,5],[1,6,3]
                  ])
b = np.array([1,0,1,0,1,0,0])
ques = np.array([2,1,8])
knearestneighbors(3,a,b,ques)