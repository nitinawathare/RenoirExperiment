
def main():
    sload = []
    sstore = []
    check=0
    last =0
    txcount=0
    filename = '/home/shashi/renoir_exp/testData/readWrite'
    file = ""
    with open(filename) as f:
        for line in f:
            data = line.split(',')
            if data[0] == 'Block_num ':
                if last == 1:
                    with open(file, 'a+') as f:
                        for item in sload:
                            f.write("SLOAD:,"+item)
                            f.write("\n")
                        f.write("\n")
                        for st in sstore:
                            f.write("SSTORE:,"+st)
                            f.write("\n")
                        f.write("\n")
                        sload.clear()
                        sstore.clear()
                        f.write("Txcount, ")
                        f.write(str(txcount))
                        txcount = 0

                block = data[1]
                print(block)
                file = "/home/shashi/renoir_exp/block/" + block
                last=1
                check=0
            elif data[0] == 'Hash ':
                txcount=txcount+1
                hash = data[1]
                if check==0:
                    with open(file, 'a+') as f:
                        f.write("hash:,"+ hash)
                    check=1
                elif check == 1:
                        with open(file, 'a+') as f:
                            for item in sload:
                                f.write("SLOAD:,"+item)
                                f.write("\n")
                            f.write("\n")
                            for data in sstore:
                                f.write("SSTORE:,"+data)
                                f.write("\n")
                            f.write("\n")
                            sload.clear()
                            sstore.clear()
                            f.write("hash:," + hash)


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