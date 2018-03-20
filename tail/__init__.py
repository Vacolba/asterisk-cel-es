import os
import sys
import json
import time


class TailFile(object):

    def __init__(self, log_file, position_file=None):
        self.position = 0
        self.log_file = log_file
        self.callback = sys.stdout.write
        if position_file is not None:
            self.position_file = position_file

    def register_callback(self, func):
        self.callback = func

    def initial_pos(self):
        position = 0
        if not os.path.exists(self.position_file):
            return 0
        with open(self.position_file) as p:
            position = int(p.read())
        if position > self.final_position():
            return 0
        return position

    def final_position(self):
        position = 0
        with open(self.log_file, 'r') as file_:
            file_.seek(0, 2)
            position = file_.tell()
        return position

    def set_position(self, position):
        with open(self.position_file, 'w') as f:
            f.write(str(position))

    def follow(self, s=1):
        with open(self.log_file) as file_:
            file_.seek(self.initial_pos())
            while True:
                curr_position = file_.tell()
                self.set_position(curr_position)
                line = file_.readline()
                if not line:
                    if curr_position > self.final_position():
                        file_.seek(0, 0)
                    else:
                        time.sleep(s)
                else:
                    data = self.generate_dict(line)
                    self.callback(data)

    def generate_dict(self, line):
        json_str = line.replace("''", '""').replace("'", "")
        data = json.loads(json_str)
        data["@timestamp"] = time.strftime(
            "%Y-%m-%dT%H:%M:%S",
            time.gmtime(data['eventtime'])
        )
        if data['eventextra'] is "":
            del data["eventextra"]

        return data
