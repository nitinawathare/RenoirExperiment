
def main():
    sload = []
    sstore = []
    check=0
    last =0
    filename = '/home/shashi/renoir_exp/testData/readWrite'
    file = ""
    with open(filename) as f:
        for line in f:
            data = line.split(',')
            if data[0] == 'Block_num ':
                if last == 1:
                    with open(file, 'a+') as f:
                        f.write("SLOAD:\n")
                        for item in sload:
                            f.write(item)
                            f.write("\n")
                        f.write("SSTORE:\n")
                        for st in sstore:
                            f.write(st)
                            f.write("\n")
                        sload.clear()
                        sstore.clear()
                block = data[1]
                print(block)
                file = "/home/shashi/renoir_exp/block/" + block
                last=1
                check=0
            elif data[0] == 'Hash ':
                hash = data[1]
                if check==0:
                    with open(file, 'a+') as f:
                        f.write("Hash: "+ hash)
                        f.write("\n")
                    check=1
                elif check == 1:
                        with open(file, 'a+') as f:
                            f.write("SLOAD:\n")
                            for item in sload:
                                f.write(item)
                            f.write("\n")
                            f.write("SSTORE:\n")
                            for data in sstore:
                                f.write(data)
                                f.write("\n")
                            f.write("\n")
                            sload.clear()
                            sstore.clear()
                            f.write("hash:" + hash)

            elif data[0] == 'SLOAD':
                sload.append(data[1])

            elif data[0] == 'SSTORE':
                sstore.append(data[1])

            else:
                continue
            if '8433700' in line:
                break


if __name__ == "__main__":
    main()