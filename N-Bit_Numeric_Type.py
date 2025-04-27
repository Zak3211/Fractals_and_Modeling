

class customFloat:
    def __init__(self, prefix_bits, suffix_bits, isSigned):
        self.bits = [False]*(prefix_bits + suffix_bits)
        self.suffix_bits = suffix_bits
        self.prefix_bits = prefix_bits
        
        if isSigned:
            self.sign = True
    
    def add(self, other):

        #Ensuring both numbers are of the same structure
        try :
            assert other.type == self.type, "Cannot add different types"
            assert self.prefix_bits == other.prefix_bits, "Cannot add different prefix bits"
            assert self.suffix_bits == other.suffix_bits, "Cannot add different suffix bits"
            assert self.sign == other.sign, "Cannot add different sign types"
        except AssertionError as error:
            print(error)
            return None
        
        #Adding the two numbers
        res = customFloat(self.prefix_bits, self.suffix_bits, self.sign)
        
        carry = False
        for i in range(len(res.bits) - 1, -1, -1):

            if not carry:
                if self.bits[i] and other.bits[i]:
                    carry = True
                elif self.bits[i] or other.bits[i]:
                    res.bits[i] = True
                continue
            
            if self.bits[i] and other.bits[i]:
                res.bits[i] = True
            elif not (self.bits[i] and other.bits[i]):
                carry = False
                res.bits[i] = True
            
        return res


        
