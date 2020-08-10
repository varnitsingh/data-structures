import random,time,sys,csv
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def update_progress(progress):
    barLength = 40 # Modify this to change the length of the progress bar

    status = ''
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Completed                                                      \r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), int(progress*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            return mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def linearSearch(input_list,val):
    index=0
    for value in input_list:
        if value == val:
            return index
        index+=1
    return -1

def callSearch(array_to_search):
    print('Binary Search')
    for i in range(10):
        limit = (i+1)*100000
        start_time=time.time()
        BinarySearch(array_to_search[:limit],array_to_search[limit-1])
        xbin.append(limit)
        ybin.append(time.time()-start_time)
        update_progress((i+1)/10)
    
    print('Linear Search')
    for i in range(10):
        limit = (i+1)*100000
        start_time=time.time()
        linearSearch(array_to_search[:limit],array_to_search[limit-1])
        xlin.append(limit)
        ylin.append(time.time()-start_time)
        update_progress((i+1)/10)

if __name__ == "__main__":
    total_time = time.time()
    array=[]
    xbin=[]
    ybin=[]
    xlin=[]
    ylin=[]
    
    '''with open('array.csv','r') as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            array.append(row[0])'''

    for i in range(1000000):
        array.append(i)
    
    callSearch(array)
    plt.plot(xbin, ybin, label = "Binary Search",marker='o')
    plt.plot(xlin, ylin, label = "Linear Search",marker='o')
    plt.xlabel('Elements -->')  
    plt.ylabel('Time taken  -->')  
    plt.title('Searching algorithms')
    plt.legend()
    plt.show()
    print('Total Time = '+str(time.time()-total_time))