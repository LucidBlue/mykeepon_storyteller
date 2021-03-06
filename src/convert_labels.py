import sys

def convert_labels(filename, chunk, frames, rate, delay):
    num_bins = float(frames)/float(chunk)
    duration = float(frames)/float(rate)
    sec_per_frame = duration/num_bins
    frame_delay = int(delay/sec_per_frame)
    
    print("bins %f dur %f sec/frame %f frame_delay %d" %(num_bins, duration, sec_per_frame, frame_delay))
    
    array_length = int(num_bins) + frame_delay + 1
    label_array = [['none', 'none', 'none'] for x in range(array_length)]
    
    label_file = open(filename, 'rb')
    
    for line in label_file:
        elements = line.split()
        time = float(elements[0])
        
        label = elements[2]
        if len(elements) == 4:
            label = label + ' ' + elements[3]
        frameno = int(time/sec_per_frame) - frame_delay
        
        print("time %f label %s frameno %d" %(time, label, frameno))
        
        label_array[frameno][2] = label
    
    new_label_array = [(x[0], x[1], x[2]) for x in label_array]
    
    """
    for elem in new_label_array:
        print(elem)
    """
    return new_label_array

def main():
    filename = sys.argv[1]
    chunk = float(sys.argv[2])
    frames = float(sys.argv[3])
    rate = float(sys.argv[4])
    delay = float(sys.argv[5])
    convert_labels(filename, chunk, frames, rate, delay)


if __name__ == "__main__":
    main()
