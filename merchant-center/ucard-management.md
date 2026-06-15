# UCard Management

平台supportenable虚拟卡、实体卡，同时兼容多子卡共用共享projectassets的共享卡/

U 卡资金链路总览

merchant数币account → 划转至 U 卡account → U 卡account下分两路：

路 1：直接deposit到单张 U 卡（开卡费、fee、单卡balance扣减）

路 2：deposit到共享project → 共享project下所有子卡共用同一资金池

资金只能从数币account进来，U 卡account不接收external入金。

Feature Description：

U 卡account是merchant在 U 卡体系下的资金载体，资金均有数币account进来。U卡体系下开卡、fee、deposit都在该account下扣除。

Operationsdescription：

划转：support数币accountassets与U卡account资金划转。

account明细：viewU卡account资金流水。

Feature Description：

多张子卡共享同一project资金池的机制，supportprojectcreate、子卡add、projectdeposit/withdrawal。

Operationsdescription：

addproject：共享project → 添加project → 填写name/depositamount/选择卡段等 → confirmcreate。

deposit：共享project → details → deposit → 输入amount → confirm。

转出：共享project → details → withdrawal → 输入amount → confirm。

add子卡：共享project →  添加共享卡 → 选择 U 卡→选择持卡人并configuration消费quota → confirm。

冻结/activate子卡：共享project → details → 选择子卡 → 冻结/activate。冻结后子卡不可用。

冻结：共享project → details → 更多 → 冻结。 冻结后所有子卡均不可用。

view：

details-子卡list：view所有子卡information，以及management子卡。

transaction流水：显示共享project的资金流水。

卡type对比

维度

虚拟卡

实体卡

共享卡

开卡入口

卡片management

卡片management

共享project（不在卡片management开）

资金来源

U 卡account

U 卡account

共享project资金池

适用场景

线上支付、即开即用

线下刷卡、实体邮寄

team/project共用资金

statusmanagement

冻结/解冻/注销

冻结/解冻/注销

在共享project下management

Feature Description：

management所有 U 卡（虚拟卡/实体卡）的全生命周期，包括开卡、statusmanagement、查询。list会同时display共享卡（共享卡的开卡及deposit入口在「共享project」模块，本模块仅supportview与statusmanagement）。

Operationsdescription：

add（开卡）：

实体卡：卡片management → 开卡 → 选择卡type（虚拟卡/实体卡）→  选择卡 BIN/卡organization → 选择持卡人 →输入卡号→ settingspin → confirm开卡（system自动扣开卡费）。

虚拟卡：卡片management → 开卡 → 选择卡type（虚拟卡/实体卡） → 选择卡 BIN/卡organization→ 选择持卡人→ depositamount → confirm开卡（system自动扣开卡费）。

ps：共享卡开卡通过共享project下进行开卡。

details：卡片management → list → click某张卡 → view完整information（卡号/持卡人/balance/limit/status/transactionrecords）。

statuschange：卡片management → list → Operations列 →冻结/解冻/copy/注销。

deposit：

常规卡：deposit则扣除U卡account资金

共享卡：modify总授信quota，并不adjust资金。

转出：

常规卡：转出到U卡account中。

共享卡：modify总授信quota，并不adjust资金。

filter：卡片management → list → 按status/卡type/持卡人/卡号/所属projectfilter。

Feature Description：

records U 卡在网络支付时触发的 3DS 二次verifyinformation，supportverifyrecords查询。

Operationsdescription：

filter：3DS verify → verifyrecords → settingstime/卡号/持卡人/verify结果/amount范围 → 查询/export。

Feature Description：

查询 U 卡所有消费records的入口，support多维filter、detailsview、export对账。

Operationsdescription：

filter：transaction查询 → list → settingstime/卡号/持卡人/卡type/所属project/status/type/amount/merchant/关键字 → 查询/export。

Feature Description：

management U 卡持卡人information，是开卡的前置模块，需先create持卡人。

Operationsdescription：

add：持卡人management → add持卡人 → 填写基本information（姓名/证件/手机/address）→ upload证件 → submit。

details：view完整information及关联卡片。

冻结/activate： deactivate/activate。

delete（注销）：持卡人management → list → Operations列 → 注销（需先handle名下所有卡片）。

filter：持卡人management → list → 按 KYC status/国籍/持卡人status/姓名/手机号/证件号filter。
