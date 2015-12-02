from pydatapub import get_data
import matplotlib.pyplot as plt 

# main() function
def main():
    columns = (0,14,16,17)
    filename = "sample.data"
    start = 1070
    end = 1400
    
    time,force,displacement,amag = get_data(filename, use_columns=columns, start=start, end=end)

    plt.figure(1)
    plt.subplot(311)
    plt.plot(time, force, 'b-')

    plt.subplot(312)
    plt.plot(time, displacement, 'g-')

    plt.subplot(313)
    plt.plot(time, amag, 'r-')
    plt.show()
    
# call main
if __name__ == '__main__':
  main()
