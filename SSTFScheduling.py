def SSTF(arr, head, len_array):
    local_arr = list(arr)
    movement = 0
    seek_list = []
    position = head
    
    while len(local_arr) != 0:
        closest_point = abs(head-local_arr[0])
        closest_index = 0       

        for x in range(1, len(local_arr)):
            if abs(position-local_arr[x]) < closest_point:
                closest_point = abs(position-local_arr[x])
                closest_index = x

        movement += abs(position-local_arr[closest_index])
        seek_list.append(local_arr[closest_index])        
        position = local_arr[closest_index]
        local_arr.remove(position)
        


    print("TOTAL HEAD MOVEMENTS",movement)
    print("SEEK SEQUENCE IS")
    print(seek_list)
    return
    
    

if __name__ == '__main__':

    print("Enter Number of Points to visit")
    num_points = int(input())
    print("Enter Request Array")
    request_array = []
    for i in range(num_points):
        request_array.append(int(input()))

    print("Enter the head value")
    head = int(input())

    SSTF(request_array, head, num_points)


#Test Case
#head = 50
#disk-req = 95, 180, 34, 119, 11, 123, 62, 64
