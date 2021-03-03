from brownie import interface

QUICKSWAP_ROUTER = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"

USDC_WETH_STAKING = interface.StakingRewards("0x9732E1cC876d8D0B61389385fC1FC756920404fd")
DAI_WETH_STAKING = interface.StakingRewards("0xDFc1b89b6184DfCC7371E3dd898377ECBFEf7058")
USDC_maUSDC_STAKING = interface.StakingRewards("0x68910d18332fFDc1D11caEA4fE93C94Ccd540732")
ETH_wBTC_STAKING = interface.StakingRewards("0x74aF83811468d7a51452128727AB14507B7DC57E")
maUSDC_maTUSD_STAKING = interface.StakingRewards("0x5AE1e3Af79270e600D0e86609bB56B6c6CE23Ee8")
maUSDC_maUSDT_STAKING = interface.StakingRewards("0x66aCCDc838F563D36D0695539c5A01E651eAAEC9")
maUSDC_maDAI_STAKING = interface.StakingRewards("0x0A8E11C2C9B89285e810A206D391CE480dbA7562")

MATIC_ETH = interface.IERC20("0x7ceb23fd6bc0add59e62ac25578270cff1b9f619")
MATIC_BTC = interface.IERC20("0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6")
MATIC_QUICK = interface.IERC20("0x831753dd7087cac61ab5644b308642cc1c33dc13")
MATIC_MATIC = interface.IERC20("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")

TOKEN_PRICES = {
  "Quickswap": (
    QUICKSWAP_ROUTER,
    [
      ("ETH", MATIC_ETH),
      ("BTC", MATIC_BTC),
      ("QUICK", MATIC_QUICK),
      ("MATIC", MATIC_MATIC)
    ]
  )
}

MASTER_CHEF_FARMS = {
}

STAKING_REWARDS_FARMS = {
  "QuickSwap": (
    QUICKSWAP_ROUTER,
    [
      ("USDC_ETH", USDC_WETH_STAKING),
      ("DAI_ETH", DAI_WETH_STAKING),
      ("USDC-maUSDC", USDC_maUSDC_STAKING),
      ("ETH-wBTC", ETH_wBTC_STAKING),
      ("maUSDC-maTUSD", maUSDC_maTUSD_STAKING),
      ("maUSDC-maUSDT", maUSDC_maUSDT_STAKING),
      ("maUSDC-maDAI", maUSDC_maDAI_STAKING),
    ]
  ),
}
