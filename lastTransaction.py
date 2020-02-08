from pathlib import Path

def findTransaction():
    blockHashInfo = "/media/shashi/NO_ONE/RenoirData2/renoirData/blockHashInfo"
    block = {}
    count = 0
    with open(blockHashInfo) as fp:
        
        for line in fp:        
            count=count+1
            data = line.split()
            blockhash = data[1]
            blocktime = data[2]
            blockpeer = data[3]
            if blockhash in block:
                oldtime  = block[blockhash][1]
                if oldtime > blocktime:
                    block[blockhash] = (blockpeer,blocktime)
            else:
                block[blockhash] = (blockpeer,blocktime)
            
            if count == 100:
                break
    filecount=0            
    for key, value in block.items():
        blockfile = "/media/shashi/NO_ONE/RenoirData2/renoirData/blocks/"+ key
        print(blockfile)
        blocktrx ={}
        myblockfile = Path(blockfile)
        
        if myblockfile.is_file():
            filecount+=1
            with open(blockfile) as btx:
                peerfile = "/media/shashi/NO_ONE/RenoirData2/renoirData/transactions/transactionInfo_enode:__"+value[0][8:]
                print(peerfile)
                latesttxTime =0 
                for tx in btx:
                    print(tx)                  
                    with open(peerfile) as f:
                        for line in f:
                            txdata = line.split()
                            # print("transaction...",txdata[0],tx)
                            if txdata[0] == tx:
                                print("transaction found")
                                txtime = txdata[1]
                                if txtime>latesttxTime:
                                    latesttxTime=txtime
                                
                blocktrx[blockhash] =latesttxTime-int(value[1])  
                print("time.....",latesttxTime)
    
    for key,value in blocktrx.items():
        print(key,value)
    print(filecount)              
                            
                            
                        
                            
 

def main():
    findTransaction()

if __name__ == "__main__":
    main()
    
