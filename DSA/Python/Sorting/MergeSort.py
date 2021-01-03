__author__ = "Mohamed Ismayil"
__credits__ = ["Abdul Bari"]
__version__ = "1.0"
__maintainer__ = "Mohamed Ismayil"
__email__ = "ismayil.ece@gmail.com"
__status__ = "Prototype"
__date__ = "03-Jan-2021"

'''
In Merge Sort, a list will be broken into smaller lists, each of length One.
Say for e.g., if an unsorted list of length 15 is given as an input for Merge
Sort, then that input list will be broken into 15 SubLists, each of length One.
And these Sublists will be passed as input to TwoWayMerge Sort with 2 lists at
a time.

15 13 2 45 22 1 3 45
--------------------
          |
     -----------
     |         |
15 13 2 45 22 1 3 45
---------- ---------
     |         |
   -----     ------
  |     |    |     |
15 13 2 45 22 1  3 45
----- ---- ----  ----
  |     |    |     |
----  ---- ----   ----
|  |  |  | |  |   |  |
15 13 2 45 22 1   3  45

'''
import math
from random import seed
from random import randint
from twoWayMergeSort import twoWayMergeSort

def mergeSort(list3: list):
    if(len(list3) > 1):
        mid = math.floor((len(list3))/2)
        list1 = list3[:mid]
        list2 = list3[mid:]
        mergeSort(list1)
        mergeSort(list2)
        list3 = twoWayMergeSort(list1, list2, list3)
        return list3
    
if __name__ == "__main__":
    
    mainList = [3,4,11,2,45,4,21,3,22]
    list1 = []
    list2 = []
    for _ in range(5):
        list1.append(randint(0, 100))
    
    for _ in range(5):
        list2.append(randint(90, 150))
    
    list1.sort()
    list2.sort()
    print("====== Two Way Merge Sort ======")
    print(f'INPUT List - 1 --> {list1}')
    print(f'INPUT List - 2 --> {list2}')
    Flist = twoWayMergeSort(list1, list2)
    print(f'Final Output --> {Flist}\n')

    print("====== Merge Sort - Recurssion ======")
    print(f'INPUT List --> {mainList}')
    Flist = mergeSort(mainList)
    print(f'Final Output --> {Flist}')