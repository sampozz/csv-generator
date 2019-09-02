def start_anonymizer(out_file_name, config, n=100):

    with open(out_file_name, 'w') as file:

        for i, col_name in enumerate(config.keys()):
            file.write(col_name)
            if i != len(config.keys())-1:
                file.write(',')
            else:
                file.write('\n')

        for i in range(n):
            for i, col_name in enumerate(config.keys()):
                file.write(config[col_name].generate())
                if i != len(config.keys())-1:
                    file.write(',')
                else:
                    file.write('\n')