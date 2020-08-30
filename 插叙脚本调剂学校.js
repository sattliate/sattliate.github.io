

(function() {
    'use strict';
    console.log("-------------------开始执行脚本-------------");

    var timeId = setInterval(clickSign,5000);
})();

function clickSign() {

    var time1 = new Date();
    console.log("执行时间 "+time1);
    'use strict';
    $("#dwxx").val( '北京交通大学');
     $("#zyxx").val( '电子信息');
     $("a[class='ttj-btn-middle tj-seach-btn']").click();
     //没找到
     if($(".tj-table tbody tr td")[0].innerText!="该条件下没有查询到调剂意向余额信息"){

    //找到发送QQ邮箱
     alert($(".tj-table tbody tr td")[0].innerText);
     }




}