import winsound
import time
from tkinter import *
from tkinter import ttk
import random
from sorting import Sortings

Sortings = Sortings()

# Dictionary to store algorithm descriptions
algorithm_descriptions = {
    'Bubble Sort': "Bubble Sort:\n\nStep 1: Start at the beginning of the list.\nStep 2: Compare the first two elements. If the first element is greater than the second element, swap them.\nStep 3: Move to the next pair of elements, and repeat Steps 1 and 2 until the end of the list is reached. After the first pass, the largest element will be at the end of the list.\nStep 4: Repeat Steps 1-3 for the remaining elements in the list, excluding the last element, which is already in its correct position.",
    'Selection Sort': "Selection Sort:\n\nStep 1: Divide the list into two sublists: sorted and unsorted.\nStep 2: Find the minimum element in the unsorted sublist.\nStep 3: Swap the minimum element with the first element of the unsorted sublist.\nStep 4: Move the boundary of the sorted sublist one element to the right.\nStep 5: Repeat Steps 2-4 until the entire list is sorted.",
    'Quick Sort': "Quick Sort:\n\nStep 1: Choose a pivot element from the list.\nStep 2: Partition the list into two sublists: elements less than the pivot and elements greater than the pivot.\nStep 3: Recursively apply Quick Sort to the two sublists.\nStep 4: Concatenate the sorted sublists and the pivot to form the final sorted list.",
    'Merge Sort': "Merge Sort:\n\nStep 1: If the list has only one element, return it (it is already sorted).\nStep 2: Divide the list into two halves.\nStep 3: Recursively apply Merge Sort to each half.\nStep 4: Merge the sorted halves to produce a single sorted list."
}

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(1000, 600)  # Increased horizontal size
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []

# function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 700  # Increased canvas width
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]), fill='white')
    
    root.update_idletasks()

def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal+1, maxVal+1))

    drawData(data, ['white' for x in range(len(data))])  # ['red', 'red' ,....]

    # Display algorithm description
    selected_algorithm = algMenu.get()
    algorithm_text.config(state=NORMAL)
    algorithm_text.delete(1.0, END)  # Clear previous text
    algorithm_text.insert(END, algorithm_descriptions[selected_algorithm])
    algorithm_text.config(state=DISABLED)

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        Sortings.quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        Sortings.bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        Sortings.selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        Sortings.merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])

# frame / base layout
UI_frame = Frame(root, width=300, height=300, bg='black')  # Increased width
UI_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=700, height=380, bg='black')  # Adjusted width
canvas.grid(row=1, column=0, padx=0, pady=0)

# Algorithm Information frame
algorithm_info_frame = Frame(root, width=300, height=300, bg='black')  # Adjusted height
algorithm_info_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=10)

# Add algorithm information labels or text widgets here
algorithm_label = Label(algorithm_info_frame, text="Algorithm", bg='black', fg='white', font=("Arial", 12))  # Reduced font size
algorithm_label.pack(side=TOP)

algorithm_text = Text(algorithm_info_frame, width=40, height=10, bg='white', wrap=WORD, font=("Arial", 10))  # Reduced font size
algorithm_text.pack(side=TOP)
algorithm_text.config(state=DISABLED)  # Disable editing

# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg='black', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, bg='white', label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='green').grid(row=1, column=3, padx=5, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='white', label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", bg='white')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", bg='white')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='grey').grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
