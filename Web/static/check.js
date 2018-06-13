function check() {
    let numLine = [];
    let boxs = document.getElementsByClassName("box");
    for (let box of boxs) {
        let num = box.value;
        if (num) {
            if (num > 9 || num < 1) {
                alert('位置 ' + box.title + ' 输入错误！');
                return false;
            }
            else if(numLine.indexOf(num) != -1){
                alert('数字 '+ num + ' 重复！');
                return false;
            }
            else {
                numLine.push(num);
            }
        }
    }
    if (numLine.length != 4) {
        alert('你需要输入4个数');
        return false;
    }
    return true;
}