const money = {
    6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252,
    12: 108, 13: 72, 14: 54, 15: 180, 16: 72, 17: 180,
    18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800, 24: 3600
};
const line = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];

Array.prototype.remove = function (val) {
    let index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};

const permutator = (inputArr) => {
    let result = [];
    const permute = (arr, m = []) => {
        if (arr.length === 0) {
            result.push(m)
        } else {
            for (let i = 0; i < arr.length; i++) {
                let curr = arr.slice();
                let next = curr.splice(i, 1);
                permute(curr.slice(), m.concat(next))
            }
        }
    };
    permute(inputArr);
    return result;
};

const calEveryLine = (num, poss) => {
    for (let pos in poss) {
        num.splice(pos, 0, poss[pos])
    }
    let everyLineSum = [];
    for (let i of line) {
        let sum = 0;
        for (let j of i) {
            sum += num[j];
        }
        everyLineSum.push(money[sum]);
    }
    return everyLineSum;
};
const calculate = (nums, poss) => {
    for (let pos in poss) {
        nums.remove(poss[pos]);
    }
    let newNums = permutator(nums);
    let allLineSum = [0, 0, 0, 0, 0, 0, 0, 0];
    for (let num of newNums) {
        let everyLineSum = calEveryLine(num, poss);
        for (let i = 0; i < 8; i++) {
            allLineSum[i] += everyLineSum[i];
        }
    }
    let maxLine = [];
    let maxMoney = 0;
    for (let key in allLineSum) {
        if (allLineSum[key] > maxMoney) {
            maxMoney = allLineSum[key];
            maxLine = [];
            maxLine.push(key);
        }
        else if (allLineSum[key] === maxMoney) {
            maxLine.push(key);
        }
    }
    return maxLine;
};

function subm() {
    let newNumLine = [];
    const boxes = document.getElementsByClassName("box");
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

    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    let poss = {};
    for (let box of boxes) {
        if (box.value && box.value !== 0) {
            poss[parseInt(box.id)] = parseInt(box.value);
        }
    }
    let bestLines = calculate(nums, poss);
    for (let bestLine of bestLines) {
        let i = 0;
        for (let box of boxes) {
            if (box.id == line[bestLine][i]) {
                box.style.background = '#67e401';
                i++;
            }
        }
    }
}