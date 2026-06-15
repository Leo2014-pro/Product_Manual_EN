# Collection

collection是merchantmanagement所有向usercollection（代收）order、跟踪资金status的核心功能模块。

链接list

Feature Description：本模块display已create的所有collection链接。

Operations：

filter：通过标识、productname、time等条件进行filtersearch。

view：view某个支付链接详细information，以及支付链接对应order。

delete：delete链接后，该支付链接失效。

copy：click“copy链接”button，即可将该URLshare给买家进行payment。

add：生成一个面向买家的固定collection链接，并support灵活configuration参数，包含以下

链接基本information：

productname、productdescription：将于支付收银pagedisplay所settingsinformation

图片：若不settings，则displaymerchantlogo

高级settings：如configuration后，user在支付收银page需要填写对应information

计价currency：该支付链接用于计算pricecurrency

计价amount：user需要支付的amount字段，如不填写则由user在收银page自己填写

链接configuration：

type：可选数币或fiat currency（单选），user实际支付时可使用支付方式

currency/amount：根据所选type，选择具体currency及orderamount

链接type：单次有效/多次有效，这将决定本链接可发起一次或可重复发起transaction

链接有效期：当前support4种方式，24h/48h/长期有效，自定义（半年内区间）

Feature Description：This page集中display您数字currency代收orderrecords，便于查询、跟踪和management。包含API下单以及支付链接下单data。

Operations：

filter：order号、type、transactionstatus、timesearch。

view：orderdeposit详细字段。

orderstatus：ordersuccess后，才会入账到merchant冻结assets中。

结算status：结算变为success时，才会入账到merchant可用assets中。

回调notifications：回调success后，表示已notifications下游interface。

切换status：该Operations仅沙河environment存在，用于API对接时，调试使用。

尽情期待！
