__author__ = "Mohamed Ismayil"
__credits__ = ["Abdul Bari"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "03-Jan-2021"

def twoWayMergeSort(list1: list, list2: list, list3 : list = None):
    '''
    Two Way Merge Sort works on the principle of merging Two sorted lists into 
    One
    '''
    if not list3:
        list3 = (len(list1) + len(list2))*[None]

    i = j = k =0
    while(i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            list3[k] = list1[i]
            i += 1
        else:
            list3[k] = list2[j]
            j += 1
        k += 1
    while(i < len(list1)):
        list3[k] = list1[i]
        i += 1
        k += 1
    while(j < len(list2)):
        list3[k] = list2[j]
        j += 1
        k += 1
    return list3