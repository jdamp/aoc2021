import numpy as np
transmission = open("input.txt").read().strip()

class DataStream:
    def __init__(self, data):
        # ensure 4 bits for every hexadecimal character
        self.data = np.binary_repr(int(data, 16), width=4*len(data))
        print(self.data)
        self.pos = 0
        self.versions = []

    def read(self, n):
        """
        Read n bits
        """
        self.pos += n
        return int(self.data[self.pos - n: self.pos], 2)

    def operator(self, id, values):
        match id:
            case 0:
                return np.sum(values)
            case 1:
                return np.prod(values)
            case 2:
                return np.min(values)
            case 3:
                return np.max(values)
            case 5:
                return np.greater(*values)
            case 6:
                return np.less(*values)
            case 7:
                return np.equal(*values)

    def parse_packet(self):
        self.versions.append(self.read(3))
        typeid = self.read(3)
        values = []
        if typeid == 4:
            value = 0
            while True:
                first = self.read(1)
                value = (value << 4) | self.read(4)
                if first == 0: #last group
                    return value

        length_type_id = self.read(1)
        if length_type_id == 0:
            length = self.read(15)
            end = self.pos + length
            while self.pos < end:
                values.append(self.parse_packet())
        else:
            num_packets = self.read(11)
            for i in range(num_packets):
                values.append(self.parse_packet())
        return self.operator(typeid, values)


p = DataStream(transmission)
result = p.parse_packet()
print("Part 1:", sum(p.versions))
print("Part 2:", result)