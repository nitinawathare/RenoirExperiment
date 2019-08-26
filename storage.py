import csv


def main():
    file = '/home/shashi/readWrite'
    blockrecord = {}
    tx = 0
    contx=0
    comp = 0
    store = 0
    with open(file) as f:
        for line in f:
            data = line.split(',')
            if data[0] == 'Block_num ':
                blockrecord[int(data[1])-1] = (tx, contx, store, comp)
                tx = 0
                contx=0
                comp = 0
                store = 0
                check = "block"

            elif data[0] == 'Hash ':
                if check == "hash":
                    contx = contx+1
                else:
                    tx += 1
                check="hash"
            elif data[0] in ('SLOAD ','SSTORE '):
                store = store + 1
                check="store"
            else:
                comp = comp + 1
                check="comp"

    with open("/home/shashi/data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["Blocknum", "SimpleTrx", "contractTrx", "Sopcode", "otherOpcode"])
        writer.writeheader()
        csv.writer(f).writerows((k,) + v for k, v in blockrecord.items())


if __name__ == "__main__":
    main()