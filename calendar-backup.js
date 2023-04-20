class Calendar {
  constructor(domName, data, state) {
    const { height, width } = state;
    this.dom = null;
    this.height = height;
    this.width = width;
    this.data = data;
    this.init(domName);
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

  // Getter, 呼叫方法為 Calendar.area, 為一個屬性
  get area() {
    return this.calcArea();
  }

  // Method
  calcArea() {
    // 呼叫方法為 Calendar.calcArea()
    return this.height * this.width;
  }

  // 靜態方法 不需要實體化即可呼叫 e.g. Calendar.distance
  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  generateFirstWeekPart(date, weekdays) {
    var year = date.slice(0, 4);
    var month = date.slice(4, 6) - 1;
    var day = date.slice(6, 8);
    var date = new Date(year, month, day);
    // calendar display order
    var weekdays = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];
    // how many grid we need to show in first row
    var firstPartHash = {
      Sunday: 7,
      Monday: 6,
      Tuesday: 5,
      Wednesday: 4,
      Thursday: 3,
      Friday: 2,
      Saturday: 1,
    };
    var weekdayIndex = date.getDay();
    return firstPartHash[weekdays[weekdayIndex]];
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

  init(domName) {
    this.isValidDom(domName);
    var firstWeekPart = generateFirstWeekPart("20230401");
    // var firstWeekPart = firstPartHash[weekdays[weekdayIndex]]; // 1
    var data = new Array(30).fill().map((_, i) => i + 1); // 創建長度為 30 的陣列
    // 如果輸入 '202304' 字串, 則跑程式碼生成 data
    // 如果輸入 array 陣列 則執行上面程式碼
    var parts = generateParts(firstWeekPart, data.length); // parts = [1, 7, 7, 7, 7, 1];
    var result = generateCalendar(parts, data);

    console.log(result); // [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30]]
  }
}

// 自定義 星期 名稱, 預設為英文
var data = new Array(30).fill().map((_, i) => i + 1);
var c = new Calendar("body", data, { width: 100, height: 100 });
