class Calendar {
  constructor(domName, data, firstDay, state) {
    const { weekdays } = state;
    this.dom = null;
    this.firstDay = firstDay;
    this.data = data;
    this.weekdays = this.isValidWeekdays(weekdays)
      ? weekdays
      : [
          "Sunday",
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
        ];
    this.calendarData = null || [];
    this.init(domName, weekdays);
  }

  isValidDom(domName) {
    if (!domName) throw new Error("select dom first");
    var dom = document.querySelector(domName);
    var result =
      typeof HTMLElement === "object"
        ? dom instanceof HTMLElement
        : dom &&
          typeof dom === "object" &&
          dom.nodeType === 1 &&
          typeof dom.nodeName === "string";
    if (!result) throw new Error("need select one dom");
    else this.dom = dom;
  }

  isValidWeekdays(weakdays) {
    return (
      Array.isArray(weakdays) &&
      weakdays.length === 7 &&
      weakdays.every((w) => typeof w === "string")
    );
  }

  // Getter, 呼叫方法為 Calendar.getDom, 為一個屬性
  get getDom() {
    return this.getDomFun();
  }

  // Method // 呼叫方法為 Calendar.getDom()
  getDomFun() {
    if (!this.dom) return;
    return this.dom;
  }

  showWeekdays() {
    return this.weekdays;
  }

  showFinalData() {
    return this.calendarData;
  }

  // 靜態方法 不需要實體化即可呼叫 e.g. Calendar.getTotalDays
  static getTotalDays(firstDay) {
    var inputYear = firstDay.slice(0, 4);
    var inputMonth = firstDay.slice(4, 6);
    var date = new Date(`${inputYear}-${inputMonth}-01`);
    var nextMonth = new Date(date.getFullYear(), date.getMonth() + 1, 1);
    var daysInMonth =
      Math.floor((nextMonth - date) / (1000 * 60 * 60 * 24)) + 1;
    return {
      year: inputYear,
      month: inputMonth,
      daysInMonth,
    };
  }

  generateFirstWeekPart(date) {
    var year = date.slice(0, 4);
    var month = date.slice(4, 6) - 1;
    var day = date.slice(6, 8);
    var date = new Date(year, month, day);
    // how many grid we need to show in first row
    var firstPartHash = {
      0: 7, // Sunday
      1: 6, // Monday
      2: 5, // Tuesday,
      3: 4, // Wednesday
      4: 3, // Thursday
      5: 2, // Friday
      6: 1, // Saturday
    };
    var weekdayIndex = date.getDay();
    return firstPartHash[weekdayIndex];
  }

  generateParts(firstWeekPart, dataLen) {
    var parts = [];
    parts.push(firstWeekPart);
    dataLen -= firstWeekPart;
    while (dataLen > 0) {
      if (dataLen >= 7) {
        parts.push(7);
        dataLen -= 7;
      } else {
        parts.push(dataLen);
        dataLen = 0;
      }
    }
    return parts;
  }

  generateCalendar(parts, data) {
    var fillNullDay = 7 - parts[0];
    var prefixDayArr = new Array(fillNullDay).fill(null);
    var isNeedPrefix = true;
    let index = 0;
    var result = parts.map((part) => {
      const sliceDay = data.slice(index, index + part);
      const slicePart = isNeedPrefix
        ? [...prefixDayArr, ...sliceDay]
        : sliceDay;
      isNeedPrefix = false;
      index += part;
      return slicePart;
    });
    return result;
  }

  init(domName, weekdays) {
    this.isValidDom(domName);
    // 找到第一天是星期幾 用以判斷第一列該顯示幾天
    var firstWeekPart = this.generateFirstWeekPart(this.firstDay);
    // var firstWeekPart = firstPartHash[weekdays[weekdayIndex]]; // 1
    // 將第二行根據每七天拆成一列
    var parts = this.generateParts(firstWeekPart, this.data.length); // parts = [1, 7, 7, 7, 7, 1];
    var result = this.generateCalendar(parts, this.data);
    this.calendarData = result;
  }
}

function getTotalDays(input) {
  var inputYear = input.slice(0, 4);
  var inputMonth = input.slice(4, 6);
  var date = new Date(`${inputYear}-${inputMonth}-01`);
  var nextMonth = new Date(date.getFullYear(), date.getMonth() + 1, 1);
  var daysInMonth = Math.floor((nextMonth - date) / (1000 * 60 * 60 * 24)) + 1;
  return {
    year: inputYear,
    month: inputMonth,
    daysInMonth,
  };
}

// mounted()
var firstDay = "20230401";
var currentMonthInfo = Calendar.getTotalDays(firstDay);
var data = new Array(currentMonthInfo.daysInMonth).fill().map((_, i) => ({
  date: `${
    currentMonthInfo.year + currentMonthInfo.month + i + 1 > 9
      ? i + 1
      : `0${i + 1}`
  }`, // ex: 20220101
  price: (i + 1) * 100,
}));

var c = new Calendar("body", data, firstDay, {
  width: 100,
  height: 100,
  weekdays: [
    "星期天",
    "星期一",
    "星期二",
    "星期三",
    "星期四",
    "星期五",
    "星期六",
  ],
});

console.log(c.showWeekdays());
console.log(c.showFinalData());
console.log(c.getDomFun());
// console.log(c.getDom)
