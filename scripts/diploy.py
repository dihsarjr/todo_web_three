from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_accounts
from web3 import Web3


def deploy_fund_me():
    account = get_accounts()
    if network.show_active() != "development":
        price_field = config["networks"][network.show_active()]["eth_usd_price_field"]
    else:
        print(f"The network is {network.show_active()}")
        print("deploying fund me on the development network")
    if len(MockV3Aggregator) <= 0:
        moke_aggregator = MockV3Aggregator.deploy(
            18, Web3.toWei(2000, "ether"), {"from": account}
        )
        price_field = moke_aggregator.address
    fund_me = FundMe.deploy(
        price_field,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"FundMe contract address: {fund_me.address}")


def main():
    deploy_fund_me()
