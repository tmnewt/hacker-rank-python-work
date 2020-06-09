import os 
import numpy as np
import sys

# DO NOT RUN this script until you are CERTAIN you'd like to generate a test file

def writeout(loc, text):
    fp = open(loc,'w')
    fp.write(text)
    fp.close()


os.chdir('Algorithm problems\\Sorting\\tests')

# create huge pool of ints for testing sorting speed

spam = ['for single test', 'lines', 'replace this',]
# recommend using numpy to generate random stuff
# for example
# 
#   spam = list(np.random.choice(range(-10000000, 10000000), 200, replace=False))
# 
# generates 200 unique integers between the above range of  -10,000,000 and 10,000,000
# (note that it takes a good moment to create the above range generator)

spam_text = ' '.join(map(str, spam))
size = sys.getsizeof(spam_text)

file_name = input('Name the test file. Additionally, provide name of an already existing file to overwrite. ')
control = True
while control:
    prompt = input(f'Test file is {size} Bytes. Do you want to write to file? (Y or N) ')
    if prompt == 'Y':
        prompt_yes = input('Are you absolutely sure? (Y to continue) ')
        if prompt_yes == 'Y':
            if size > 100000000:
                prompt_size = input(f'This test file is {size} Bytes!! Type \"YES I WANT THIS FILE\" to confirm writeout ')
                if prompt_size == 'YES I WANT THIS FILE':
                    writeout(file_name, spam_text)
                    break
                else: 
                    print('Confirmation failed. Assuming you don\'t want this data?')
                    prompt = 'N'
            else:
                control = False
                writeout(file_name, spam_text)
                print('The file has been written.')
    elif prompt == 'N':
        prompt_no = input('The data will be deleted. Are you sure? (Y or N) ')
        if prompt_no == 'Y':
            control = False
            print('No data will be written.')
    else:
        print('Please answer with Y (Yes) or N (No)')

print('This script has finished')


