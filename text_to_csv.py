#python to parse text file to csv file
#pattern: message followed with a 1 instead of a 0, you sent message
#if above holds true, then go one message above and copy the message instigating your reply

#regex pattern: (\d{5}\|\S{8}-\S{4}-\S{4}-\S{4}-\S{12}\|(.+)\|\d\|\|\d+\|\|\|(.+)\d{9}\|0\|1\|(.+)\n)(\d{5}\|\S{8}-\S{4}-\S{4}-\S{4}-\S{12}\|(.+)\|\d\|\|\d+\|\|\|(.+)\d{9}\|1\|1\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\|\|\d\|\|\d\|\d\|\d\|)
import re
import csv

def read_file(name):
    with open(name, 'r') as myfile:
        data = myfile.read()
        myfile.close()
        return data

def text_parse(text_data):
    received = []
    replied = []
    for m in re.finditer('(\d{5}\|\S{8}-\S{4}-\S{4}-\S{4}-\S{12}\|(.+)\|\d\|\|\d+\|\|\|(.+)\d{9}\|0\|1\|(.+)\n)(\d{5}\|\S{8}-\S{4}-\S{4}-\S{4}-\S{12}\|(.+)\|\d\|\|\d+\|\|\|(.+)\d{9}\|1\|1\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\d\|\d\|\d\|\d\|\d\|\d\|\d\|\|\|\|\d\|\|\d\|\d\|\d\|)', text_data):
        received.append(m.group(2))
        replied.append(m.group(6))
    return (received, replied)

def csv_out(received, replied):
    with open('..\messages.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for (i, j) in zip(received, replied):
            if (i.count(' ') < 20) and (j.count(' ') < 20):
                writer.writerow([i, j])
        csvfile.close()
    return

if __name__ == "__main__":
    #import text file
    text_data = read_file('..\my_text_messages.txt')
    #regex to parse file
    (received, replied) = text_parse(text_data)
    #output to csv file
    csv_out(received, replied)
