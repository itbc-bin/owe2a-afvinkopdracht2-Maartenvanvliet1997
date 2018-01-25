import matplotlib.pyplot as plt

def main():
    l_status = read_file('yeast_genes.csv')
    process_status(l_status)

def read_file(file_name):
    l_status = {}
    
    with open(file_name, 'r') as f:
        file = f.readlines()

    for line in file:
        line = line.rstrip()
        t_list = line.split(',',2)

        if t_list[1] in l_status:
            l_status[t_list[1]] += 1
        else:
            l_status[t_list[1]] = 1

    return l_status

def process_status(l_status):
    barx = []
    bary = []

    for key, value in l_status.items():
        barx.append(key)
        bary.append(value)
    
    plt.bar(barx, bary)
    plt.xlabel('Status')
    plt.ylabel('Amount')
    plt.show()
    
main()
