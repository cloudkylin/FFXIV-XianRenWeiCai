function login() {
    $.ajax({
        //几个参数需要注意一下
        type: "POST",//方法类型
        dataType: "json",//预期服务器返回的数据类型
        url: "127.0.0.1:8000" ,//url
        data: $('#myform').serialize(),
        success: function (result) {
            console.log(result);//打印服务端返回的数据(调试用)
            if (result.resultCode == 200) {
                alert("提交成功");
            }
        },
        error : function() {
            alert("异常！");
        }
    });
}
function truenum(num) {
    if (0<num && num<10) return true;
    return false;
}

function check() {
    var sum = 0;
    var num = new Array();
    num[0] = document.getElementById("pos1").value;
    num[1] = document.getElementById("pos2").value;
    num[2] = document.getElementById("pos3").value;
    num[3] = document.getElementById("pos4").value;
    num[4] = document.getElementById("pos5").value;
    num[5] = document.getElementById("pos6").value;
    num[6] = document.getElementById("pos7").value;
    num[7] = document.getElementById("pos8").value;
    num[8] = document.getElementById("pos9").value;

    var lis = new Array();
    for (var i=0;i<num.length;i++)
    {
        if (num[i] == "")
            continue;
        else if (!truenum(num[i]))
            {
                var str = "位置 ";
                str += i+1;
                str +=" 输入错误。";
                alert(str);
                return false;
            }
            else
            {
                for(var j=0;j<lis.length;j++)
                {
                    if(lis[j]==num[i])
                    {
                        var str = "位置 ";
                        str += i+1;
                        str +=" 输入重复。";
                        alert(str);
                        return false;
                    }
                }
                lis.push(num[i]);
                sum++;
            }
    }
    if (sum != 4)
    {
        alert("输入错误，你需要输入4个数");
        return false
    }
    else
        return true
}