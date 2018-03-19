class bin2dec:
    def __bin2dec__( self, *args, **kwargs ):
        for k,v in kwargs.items():
            if k == 'data':
                self.data = kwargs[v]
