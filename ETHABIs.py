univ2PairAbi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"sender","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":False,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":True,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"sync","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"}]

lendingPoolAbi = [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowRateMode","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowRate","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_originationFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowBalanceIncrease","type":"uint256"},{"indexed":True,"internalType":"uint16","name":"_referral","type":"uint16"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"Borrow","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":True,"internalType":"uint16","name":"_referral","type":"uint16"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_target","type":"address"},{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_totalFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_protocolFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"FlashLoan","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_collateral","type":"address"},{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_purchaseAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_liquidatedCollateralAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_accruedBorrowInterest","type":"uint256"},{"indexed":False,"internalType":"address","name":"_liquidator","type":"address"},{"indexed":False,"internalType":"bool","name":"_receiveAToken","type":"bool"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"LiquidationCall","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_collateral","type":"address"},{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_feeLiquidated","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_liquidatedCollateralForFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"OriginationFeeLiquidated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_newStableRate","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowBalanceIncrease","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"RebalanceStableBorrowRate","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"RedeemUnderlying","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":True,"internalType":"address","name":"_repayer","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amountMinusFees","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_fees","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowBalanceIncrease","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"Repay","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"}],"name":"ReserveUsedAsCollateralDisabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"}],"name":"ReserveUsedAsCollateralEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_reserve","type":"address"},{"indexed":True,"internalType":"address","name":"_user","type":"address"},{"indexed":False,"internalType":"uint256","name":"_newRateMode","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_newRate","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_borrowBalanceIncrease","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"Swap","type":"event"},{"constant":True,"inputs":[],"name":"LENDINGPOOL_REVISION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"UINT_MAX_VALUE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"addressesProvider","outputs":[{"internalType":"contract LendingPoolAddressesProvider","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"core","outputs":[{"internalType":"contract LendingPoolCore","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"dataProvider","outputs":[{"internalType":"contract LendingPoolDataProvider","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"parametersProvider","outputs":[{"internalType":"contract LendingPoolParametersProvider","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"contract LendingPoolAddressesProvider","name":"_addressesProvider","type":"address"}],"name":"initialize","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint16","name":"_referralCode","type":"uint16"}],"name":"deposit","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"address payable","name":"_user","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_aTokenBalanceAfterRedeem","type":"uint256"}],"name":"redeemUnderlying","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_interestRateMode","type":"uint256"},{"internalType":"uint16","name":"_referralCode","type":"uint16"}],"name":"borrow","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address payable","name":"_onBehalfOf","type":"address"}],"name":"repay","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"}],"name":"swapBorrowRateMode","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"address","name":"_user","type":"address"}],"name":"rebalanceStableBorrowRate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"bool","name":"_useAsCollateral","type":"bool"}],"name":"setUserUseReserveAsCollateral","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_collateral","type":"address"},{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_purchaseAmount","type":"uint256"},{"internalType":"bool","name":"_receiveAToken","type":"bool"}],"name":"liquidationCall","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_params","type":"bytes"}],"name":"flashLoan","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_reserve","type":"address"}],"name":"getReserveConfigurationData","outputs":[{"internalType":"uint256","name":"ltv","type":"uint256"},{"internalType":"uint256","name":"liquidationThreshold","type":"uint256"},{"internalType":"uint256","name":"liquidationBonus","type":"uint256"},{"internalType":"address","name":"interestRateStrategyAddress","type":"address"},{"internalType":"bool","name":"usageAsCollateralEnabled","type":"bool"},{"internalType":"bool","name":"borrowingEnabled","type":"bool"},{"internalType":"bool","name":"stableBorrowRateEnabled","type":"bool"},{"internalType":"bool","name":"isActive","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_reserve","type":"address"}],"name":"getReserveData","outputs":[{"internalType":"uint256","name":"totalLiquidity","type":"uint256"},{"internalType":"uint256","name":"availableLiquidity","type":"uint256"},{"internalType":"uint256","name":"totalBorrowsStable","type":"uint256"},{"internalType":"uint256","name":"totalBorrowsVariable","type":"uint256"},{"internalType":"uint256","name":"liquidityRate","type":"uint256"},{"internalType":"uint256","name":"variableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"stableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"averageStableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"utilizationRate","type":"uint256"},{"internalType":"uint256","name":"liquidityIndex","type":"uint256"},{"internalType":"uint256","name":"variableBorrowIndex","type":"uint256"},{"internalType":"address","name":"aTokenAddress","type":"address"},{"internalType":"uint40","name":"lastUpdateTimestamp","type":"uint40"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserAccountData","outputs":[{"internalType":"uint256","name":"totalLiquidityETH","type":"uint256"},{"internalType":"uint256","name":"totalCollateralETH","type":"uint256"},{"internalType":"uint256","name":"totalBorrowsETH","type":"uint256"},{"internalType":"uint256","name":"totalFeesETH","type":"uint256"},{"internalType":"uint256","name":"availableBorrowsETH","type":"uint256"},{"internalType":"uint256","name":"currentLiquidationThreshold","type":"uint256"},{"internalType":"uint256","name":"ltv","type":"uint256"},{"internalType":"uint256","name":"healthFactor","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"address","name":"_user","type":"address"}],"name":"getUserReserveData","outputs":[{"internalType":"uint256","name":"currentATokenBalance","type":"uint256"},{"internalType":"uint256","name":"currentBorrowBalance","type":"uint256"},{"internalType":"uint256","name":"principalBorrowBalance","type":"uint256"},{"internalType":"uint256","name":"borrowRateMode","type":"uint256"},{"internalType":"uint256","name":"borrowRate","type":"uint256"},{"internalType":"uint256","name":"liquidityRate","type":"uint256"},{"internalType":"uint256","name":"originationFee","type":"uint256"},{"internalType":"uint256","name":"variableBorrowIndex","type":"uint256"},{"internalType":"uint256","name":"lastUpdateTimestamp","type":"uint256"},{"internalType":"bool","name":"usageAsCollateralEnabled","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getReserves","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"}]