# Imports
from sys import stdout

def start_generator(out_file_name, config, n=100):

    with open(out_file_name, 'w') as file:

        for i, col_name in enumerate(config.keys()):
            file.write(col_name)
            if i != len(config.keys())-1:
                file.write(',')
            else:
                file.write('\n')

        for i in range(int(n)):
            for j, col_name in enumerate(config.keys()):
                file.write(config[col_name].generate())
                if j != len(config.keys())-1:
                    file.write(',')
                else:
                    file.write('\n')
            # print progress bar
            progress(i+1, n, str("   " + str(i+1) + "/" + str(n)))    
        print()        


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '>' + '-' * (bar_len - filled_len)
    stdout.write('[%s] %s%s%s\r' % (bar, percents, '%', suffix))
    stdout.flush()