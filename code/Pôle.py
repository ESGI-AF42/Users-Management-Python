from corp import Corp
    class Pôle(Corp):
    
        def_init_(self, Trades, Fonction, Members):
        self.trades = Trades
        self.fonction = Fonction
        self.members = Members

    def get_pôle_trades(self):
        return self.trades

    def get_pôle_fonction(self):
        return self.fontion

    def get_pôle_members(self):
        return self.members
