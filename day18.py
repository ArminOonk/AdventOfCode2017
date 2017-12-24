class Program:
    def __init__(self, data, program_id):
        self.registers = dict()
        self.cnt = 0
        self.data = data
        self.program_id = program_id
        self.isFinished = False
        self.waitingRcv = False
        self.other = None
        self.rcv_queue = []
        self.send_cnt = 0
        self.registers['p'] = self.program_id

    def snd(self, v):
        if self.other:
            self.other.rcv(v)
            self.send_cnt += 1

    def rcv(self, v):
        self.rcv_queue.append(v)

    def get_value(self, v):
        try:
            ret = int(v)
        except:
            if v in self.registers:
                ret = self.registers[v]
            else:
                ret = 0
        return ret

    def set_value(self, reg, v):
        if reg not in self.registers:
            self.registers[reg] = 0
        self.registers[reg] = self.get_value(v)

    def run(self):
        if self.isFinished:
            return

        if self.waitingRcv and not self.rcv_queue:
            return

        try:
            command = [x.strip() for x in data[self.cnt].split(' ')]
            if command[0] == 'snd':
                self.snd(self.get_value(command[1]))
            elif command[0] == 'set':
                self.set_value(command[1], command[2])
            elif command[0] == 'add':
                self.set_value(command[1], self.get_value(command[1]) + self.get_value(command[2]))
            elif command[0] == 'mul':
                self.set_value(command[1], self.get_value(command[1]) * self.get_value(command[2]))
            elif command[0] == 'mod':
                self.set_value(command[1], self.get_value(command[1]) % self.get_value(command[2]))
            elif command[0] == 'rcv':
                if self.rcv_queue:
                    self.set_value(command[1], self.rcv_queue[0])
                    self.rcv_queue = self.rcv_queue[1:]
                    self.waitingRcv = False
                else:
                    print(str(self.program_id) + ' Waiting for value')
                    self.waitingRcv = True
                    return
            elif command[0] == 'jgz':
                val = self.get_value(command[1])
                if val > 0:
                    self.cnt += self.get_value(command[2])
                    return
            else:
                print("Unknown command")
                self.isFinished = True
                return
            self.cnt += 1

        except IndexError as ex:
            print("Index error: " + str(ex))
            print("Index cnt: " + str(self.cnt))
            self.isFinished = True
            return
        return


with open('day18Input.txt', 'r') as f:
    data = f.readlines()

a = Program(data, 0)
b = Program(data, 1)

a.other = b
b.other = a

run_cnt = 0
while True:
    a.run()
    b.run()

    if a.isFinished and b.isFinished:
        print('Finished')
        break

    if a.waitingRcv and b.waitingRcv:
        print('Deadlock')
        break

    if a.isFinished and b.waitingRcv:
        print('a finished and b waiting, we are done')
        break

    if a.waitingRcv and b.isFinished:
        print('a finished and b waiting, we are done')
        break

    run_cnt += 1
    if run_cnt % 100000 == 0:
        print('run_cnt: ' + str(run_cnt) + ' 0 queue: ' + str(len(a.rcv_queue)) + ' 1 queue: ' + str(len(b.rcv_queue)))
        # print('a rcv queue: ' + str(a.rcv_queue))
        # print('b rcv queue: ' + str(b.rcv_queue))

print('Program ' + str(b.program_id) + ' number of sends: ' + str(b.send_cnt))
