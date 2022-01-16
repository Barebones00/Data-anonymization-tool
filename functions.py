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
        
    