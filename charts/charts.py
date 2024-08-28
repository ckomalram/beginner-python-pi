import matplotlib.pyplot as plt

def generate_pie_chart():
    labels= ['A', 'B', 'C']
    values= [200, 300,400]

    fig, axes  = plt.subplots()
    axes.pie(values, labels=labels)
    #plt.show()
    plt.savefig('pie.png')
    plt.close()