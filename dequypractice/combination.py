from __future__ import print_function
class solution:
    def printCombination(self,input,index,output,outputLength):
        if len(input)==index:
            output[outputLength]='\0'
            print(*output[:outputLength],sep="")
            return
        output[outputLength]=input[index]
        output[outputLength+1]=" "
        self.printCombination(input,index+1,output,outputLength+2)
        if len(input)-1!= index:
            self.printCombination(input,index+1,output,outputLength+1)
        
output=[0]*100
output[0]='\0'
input="1234"
s=solution()
s.printCombination(input,0,output,0)