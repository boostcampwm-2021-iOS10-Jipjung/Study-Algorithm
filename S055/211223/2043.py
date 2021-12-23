class Bank {

    var balance = [0]
    init(_ balance: [Int]) {
        self.balance += balance
    }
    
    func transfer(_ account1: Int, _ account2: Int, _ money: Int) -> Bool {
        if withdraw(account1, money) {
            if deposit(account2, money) {
                return true
            } else {
                deposit(account1, money)
                return false
            }
        }
        return false
    }
    
    func deposit(_ account: Int, _ money: Int) -> Bool {
        if balance.count > account && balance[account] <= Int.max - money {
            balance[account] += money
            return true
        }
        return false
    }
    
    func withdraw(_ account: Int, _ money: Int) -> Bool {
        if balance.count > account && balance[account] >= money {
            balance[account] -= money
            return true
        } else {
            return false
        }
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank(balance)
 * let ret_1: Bool = obj.transfer(account1, account2, money)
 * let ret_2: Bool = obj.deposit(account, money)
 * let ret_3: Bool = obj.withdraw(account, money)
 */