import random,time,sys
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

def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list

def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
    return input_list

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

def callsort(array_to_sort):
    print('Selection Sort')
    for i in range(10):
        start_time=time.time()
        limit = (i+1)*1000
        selection_sort(array_to_sort[:limit])
        xsel.append(limit)
        ysel.append(time.time()-start_time)
        update_progress((i+1)/10)

    print('Bubble Sort')
    for i in range(10):
        start_time=time.time()
        limit = (i+1)*1000
        bubblesort(array_to_sort[:limit])
        xbub.append(limit)
        ybub.append(time.time()-start_time)
        update_progress((i+1)/10)
    
    print('Merge Sort')
    for i in range(10):
        start_time=time.time()
        limit = (i+1)*1000
        merge_sort(array_to_sort[:limit])
        xmer.append(limit)
        ymer.append(time.time()-start_time)
        update_progress((i+1)/10)


if __name__ == "__main__":
    array=[]
    xbub=[]
    xsel=[]
    ybub=[]
    ysel=[]
    xmer=[]
    ymer=[]
    for i in range(10000):
        array.append(int(random.random()*10000))
    callsort(array)
    
    plt.plot(xbub, ybub, label = "Bubble Sort",marker='o')
    plt.plot(xsel, ysel, label = "Selection Sort",marker='o')
    plt.plot(xmer, ymer,label = 'Merge Sort',marker='o')
    plt.xlabel('Elements -->')  
    plt.ylabel('Time taken  -->')  
    plt.title('Sorting algorithms')
    plt.legend()
    plt.show()