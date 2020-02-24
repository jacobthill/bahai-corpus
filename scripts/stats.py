import matplotlib.pyplot as plt
import numpy as np

def main():
    # Plot table
    data = [[4242, 15, 1927, 2],
            [30000, 2000, 20000, 22000]]

    columns = ("`Abdu'l-Bahá", "Báb", "Bahá'u'lláh", "Shoghi Effendi")
    rows = ["Sample", "Extant"]

    values = np.arange(0, 2500, 500)
    value_increment = 1000

    colors = ['gray', '#d9e6f2']
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))


    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
    plot = plt.table(cellText=data,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.xticks([])
    plt.savefig('/Users/jtim/Dropbox/Academic/research/dissertation/research/output/figures/works-table.png')

if __name__ == "__main__":
    main()
