let numLine = [];

Array.prototype.remove = function (val) {
    let index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};

function submitEvt() {
    let newNumLine = [];
    let boxes = document.getElementsByClassName("box");
    for (let box of boxes) {
        let num = box.value;
        if (num) {
            if (num > 9 || num < 1) {
                alert('位置 ' + box.title + ' 输入错误！');
                return false;
            }
            else if (newNumLine.indexOf(num) !== -1) {
                alert('数字 ' + num + ' 重复！');
                return false;
            }
            else {
                newNumLine.push(num);
            }
        }
    }
    if (newNumLine.length !== 4) {
        alert('你需要输入4个数');
        return false;
    }
    return true;
}

function resetEvt() {
    let boxes = document.getElementsByClassName("box");
    for (let box of boxes) {
        box.style.borderStyle = null;
        box.style.borderColor = null;
        box.style.background = null;
    }
    numLine = [];
}

function focusEvt(e) {
    if (e.target.value) {
        numLine.remove(e.target.value)
    }

    numLine = numLine.sort();
    let repeatNum = [];
    for (let i = 0; i < numLine.length - 1; i++) {
        if (numLine[i] === numLine[i + 1]) {
            repeatNum.push(numLine[i])
        }
    }
    let boxes = document.getElementsByClassName("box");
    for (let box of boxes) {
        let num = box.value;
        if (num) {
            if (1 <= num && num <= 9 && repeatNum.indexOf(num) === -1) {
                box.style.borderStyle = 'solid';
                box.style.borderColor = '#15c26b';
            }
        }
    }
    e.target.style.borderStyle = null;
    e.target.style.borderColor = null;
}

function blurEvt(e) {
    let num = e.target.value;
    if (num) {
        if (num > 9 || num < 1) {
            e.target.style.borderStyle = 'solid';
            e.target.style.borderColor = '#f04546';
        }
        else if (numLine.indexOf(num) !== -1) {
            let boxes = document.getElementsByClassName("box");
            for (let box of boxes) {
                if (box.value === num) {
                    box.style.borderStyle = 'solid';
                    box.style.borderColor = '#f04546';
                }
            }
        }
        else {
            e.target.style.borderStyle = 'solid';
            e.target.style.borderColor = '#15c26b';
        }
        numLine.push(num);
    }
}
