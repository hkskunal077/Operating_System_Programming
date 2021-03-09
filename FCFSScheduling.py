def FCFS(arr, head, len_array):
    counter = 0
    distance, current_track =0,0

    for i in range(len_array):
        current_track = arr[i]
        distance = abs(current_track-head)
        counter += distance
        head = current_track


    print("TOTAL HEAD MOVEMENTS = ", counter)
    print("SEEK SEQUENCE IS: ")

    print(arr)        
if __name__ == '__main__':

    print("Enter Number of Points to visit")
    num_points = int(input())
    print("Enter Request Array")
    request_array = []
    for i in range(num_points):
        request_array.append(int(input()))

    print("Enter the head value")
    head = int(input())

    FCFS(request_array, head, num_points)
