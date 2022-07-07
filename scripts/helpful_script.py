from brownie import accounts, config, network

def get_accounts():
    if network.show_active() == 'development':
        print("Using accounts from config file");
        return accounts[0]
    else:
        print("Using accounts from config file network");
        return accounts.add(config["wallets"]["from_key"])