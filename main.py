import os
import argparse
from tail import TailFile
from es import send_to_es

ES_URL = None


def check_file_validity(log_file):
    ''' Check whether the a given file exists, readable and is a file '''
    if not os.access(log_file, os.F_OK):
        raise Exception("File '%s' does not exist" % (log_file))
    if not os.access(log_file, os.R_OK):
        raise Exception("File '%s' not readable" % (log_file))
    if os.path.isdir(log_file):
        raise Exception("File '%s' is a directory" % (log_file))


def send_data(data):
    if ES_URL is not None:
        send_to_es(ES_URL, data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Read Asterisk CEL pseudo-json and send to Elastic')
    parser.add_argument('log_file', help='Log File')
    parser.add_argument('--pos', dest='log_pos',
                        help='File containing the last read position')
    parser.add_argument('--es', dest='es_url', help='Elastic URL')

    args = parser.parse_args()

    log_file = args.log_file
    check_file_validity(log_file)
    if args.log_pos:
        log_pos = args.log_pos
    else:
        position_filename = log_file.split('/')[-1].split('.')[0]
        log_pos = '/tmp/tailed-' + position_filename + '.pos'

    ES_URL = args.es_url
    tf = TailFile(log_file, log_pos)
    tf.register_callback(send_data)
    tf.follow()
