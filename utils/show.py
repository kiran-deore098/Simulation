import matplotlib.pyplot as mat

def scatter(x_coord):
    y_coord = x_coord[1:]+[x_coord[0]]
    mat.scatter(x_coord,y_coord,marker='p')
    mat.show()
    

def histogram(x_coord,y_coord,x_label,y_label):
    mat.plot(x_coord,y_coord,color='orange')
    mat.bar(x_coord,y_coord,width=0.5)
    mat.xlabel(x_label)
    mat.ylabel(y_label)
    mat.show()


def plot_it(x_coord,y_coord):
    pass


#scatter([20,90,34,5,6,7,8],7)

