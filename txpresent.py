import pandas as pd
import numpy as np
from pathlib import Path


def main():
    # File to read block information, time and peers
    prev="0x00000"
    file = pd.read_csv("/home/shashi/renoir_exp/testData/blocks/data.csv",sep=',', header=None)
    filedata = file.iloc[1:, :].values
    for i in range(800, 900):
        blockhash = str(filedata[i][2])
        if prev==blockhash:
            continue
        else:
            print(blockhash)
            prev = blockhash
        # get block data i.e transaction present in block
            j = Path("/home/shashi/renoir_exp/testData/blockdata/" + "\""+blockhash+"\"" + ".csv")

            if j.is_file():
                block = pd.read_csv(j, sep=',', header=None)
                block = block.iloc[:,0].values.T
            else:
                continue
            arr=np.zeros(len(block))
            p = filedata[i]

            for peer in range(4, len(p)):
                if str(p[peer]) != 'nan':
                    # Taking individual peer transactions list
                    trxPath = Path("/home/shashi/renoir_exp/testData/transactions/" + "\"" + str(p[peer])+"\"" + ".csv")
                    if trxPath.is_file():
                        trx = pd.read_csv(trxPath,sep=',',header=None)
                        trx1 = trx.iloc[:,0].values.T

                        for t in range(len(block)):
                            if block[t] in trx1:
                                arr[t] += 1

                else:
                    continue
            print(arr)


if __name__ == "__main__":
    main()

