class functions:    
    def censor(values):
        for i in range(len(values)):
            values[i] = '*'
        return values
    
    def pseudonymization(values, column_name):
        import names
        if column_name == 'first_name':
            for i in range(len(values)):
                values[i] = names.get_first_name()
        elif column_name == 'name':
            for i in range(len(values)):
                values[i] = names.get_full_name()
        else:
            for i in range(len(values)):
                values[i] = names.get_last_name()
        return values
        
    def shuffle(values):
        import random
        #random.shuffle(values)
        for i in range(len(values)-1, 0, -1):
     
             # Pick a random index from 0 to i
            j = random.randint(0, i + 1)
            # Swap arr[i] with the element at random index
            values[i], values[j] = values[j], values[i]
        return values
    
    #def scramble(values):
        