# Asset Center

assets中心主要用于managementmerchant资金。

Feature Description：This page集中displaymerchant在平台的所有assetsbalance概览，并提供fiat currency、cryptocurrency的deposit与withdrawal入口。VAaccount（development中，尽情期待！）

Operations：

viewassets概览：

enterpage后，system以list形式分类display以下assetsbalance：

fiat currencyassets：按不同currency（如CNY、USD等）分别显示“可用balance”、“frozen amount”、“rolling reserve”。

数字assets：按不同currency（如USDT、BTC等）分别显示“可用balance”、“frozen amount”、

VAaccount：敬请期待

U卡account：只有USDT，用于开卡、卡deposit等能力。

depositOperations：

在对应currency的assets卡片上，click“deposit”button。

system将根据currencytype引导至不同deposit流程：

fiat currencydeposit：暂不support。

cryptocurrencydeposit：system将生成一个专属的depositaddress（或QR code），merchant向该addresstransfer即可。

withdrawalOperations：

在对应currency的assets卡片上，click“withdrawal/withdraw”button。

system将引导至“向external进行payment”page，并预选相应currency，merchant需填写withdrawalamount、选择collectionaddress等informationverify资金password及谷歌verify并submitapply。

fiat currencywithdrawal：

指定payment人:可不选，指定payment人时，fee会更高。

批量withdrawalOperations

fiat currencyaccount板块才能进行批量withdrawalOperations

exc填写得information，必须是已review得fiat currencywithdrawaddressinformation

明细：view某个currencyassets的资金流水。

Feature Description：This page用于查询和management所有merchantcryptocurrency的depositrecords，便于merchant核对入账情况。fiat currency/VAaccountdeposit暂不support。

Operations：

filter：order号、address、orderstatus、time等search。

view：viewdeposit详细information。

Feature Description：This page用于查询和management所有fiat currency与cryptocurrency的withdrawalrecords。

Operations：

view：viewfiat currency、数币的merchantwithdrawalrecords。VAaccount尽情期待！

filter：order号、address、orderstatus、time等search。

view：viewdeposit详细information。

水单：当有fiat currency转出时，orderstatus已complete，可view以及download水单。

Feature Description：本模块用于merchantmanagement其用于withdrawal时接收fiat currency和数字assets的collectionaddress以及fiat currency指定payment人management。merchantsubmitaddress需要平台review通过后，才能使用。

数字assetsaddressOperations：

filter：通过currencyfiltersearch。

edit：modifycollectionaddressinformation。

add:

受益人name：collectionaddressname

currency：currencyname

链type：该currency归属公链

currencyaddress：collection钱包address。

fiat currencyassetsaddressOperations：

filter：通过currencyfiltersearch。

view：view已添加fiat currencycollectionaddressinformation。

add:addfiat currencycollection银行information。

payment人Operations：

filter：通过currency、姓名、country等filtersearch。

view：view已添加fiat currencycollectionaddressinformation。

add：add指定payment人

Feature Description：本模块用于merchantview已enable其support的collection/paymentcurrency及其对应的费率和结算rules。如需增加新currency请contact平台。

Operations：

filter：通过currency、支付type、status等进行search。

view：view单一currency的详细information。

merchantfiat currencyaccount、数币account进行currency兑换、viewexchange rate行情及management所有兑换order的功能集合。

Feature Description：This pagedisplay平台support的所有currency兑换transaction对，提供实时exchange rateinformation，并允许merchant进行currency兑换Operations。

Operations：

filter：type、currencysearch。

兑换：

选择transactiontype：买入[goalcurrency] 或 卖出[基准currency]。

在“amount”框中输入您要付出的currencyquantity，system会根据实时exchange rate在“获得”框中自动计算您将收到的currencyquantity。

confirm显示的exchange rate、预计fee和预计到账amount。

输入资金password、谷歌verify后，click“confirm”buttonsubmitorder。

Feature Description：This page集中display您所有的currency兑换orderrecords，便于查询、跟踪和management。

Operations：

filter：order号、type、transactionstatus、timesearch。

