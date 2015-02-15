# P1026.  For Pattern Recognition course.
'''
This file contains some functions created for the Pattern
Discovery course on Coursera.
create_dataset(n_tid,n_item,max_item,i_names)
- creates datasets.  The names part is only patrially implemented.
save_dataset(data_dict,filename)
- saves a dataset to file.
read_dataset(filemane)
- loads a file created with save above and returns a dict.
one_itemsets(data_dict,min_sup)
- returns a dictionary with item as key and count as value
  for items that meet or exceed min_sup.
'''

import random # only needed for dataset creation

def create_dataset(n_tid,n_item,max_item,i_names=[]):
    '''
    This function creates a random dataset which has
    n_tid entries.  These entries choose amongst n_item
    items (which can be given string names through a
    list in i_names).  Each transaction will have up to
    max_item items.

    The output is a dictionary such as:
    { 0:{1,2}, 1:{2,3}, 2:{1}, 3:{1,2,3}, ... }
    '''
    assert(n_item == len(i_names) or len(i_names) == 0)
    output = {}
    for i in range(n_tid):
        item_set = set()
        q = random.randint(1,max_item)
        for j in range(q):
            if i_names==[]:
                item_set.add(random.randint(1,n_item))
            else:
                item_set.add(i_names(1,n_item))
        output[i]=item_set
    return output

def save_dataset(data_dict,filename):
    strlist = []
    for x in data_dict:
        outstr = str(x)+" "
        for y in data_dict[x]:
            outstr = outstr+str(y)+" "
        strlist.append(outstr)
    f=open(filename,"w",encoding='utf-8')
    for x in strlist:
        f.write(x+"\n")
    f.close()

def read_dataset(filename):
    f = open(filename,"r",encoding = 'utf-8')
    data=f.read()
    line_data = data.splitlines()
    data_dict = {}
    for x in line_data:
        y = x.split()
        z = set()
        for i in range(1,len(y)):
            z.add(int(y[i]))
        data_dict[int(y[0])] = z
    f.close()
    return data_dict

'''
Some test code below:
my_data = create_dataset(5,5,3)
save_dataset(my_data,"trial.data")
saved_data = read_dataset('trial.data')
print(my_data)
print(saved_data)
'''
                          
def one_itemsets(data_dict,min_sup):
    # This first loop counts occurences and save them
    # into a dictionary.
    calc = {}
    for itemsets in data_dict.values():
        for items in itemsets:
            if items in calc:
                calc[items] += 1
            else:
                calc[items] = 1
    output = {}
    # This second loop checks that min_sup requirement
    # is met and prunes infrequent items.
    for itemset in calc:
        if calc[itemset] >= min_sup:
            output[itemset] = calc[itemset]
    return output

'''
Some test code below:
my_data = create_dataset(7,5,4)
print(my_data)
print(one_itemsets(my_data,3))
'''
    
