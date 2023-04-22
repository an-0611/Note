// implement graph
class Graph {
  constructor() {
    this.adjacencyList = new Map();
  }
  addVertex(vertex) {
    if (!this.adjacencyList.has(vertex)) {
      this.adjacencyList.set(vertex, []);
    }
  }
  addEdge(vertex1, vertex2) {
    this.adjacencyList.get(vertex1).push(vertex2);
    this.adjacencyList.get(vertex2).push(vertex1);
  }
  findNeighbours(vertex) {
    if (!this.adjacencyList.has(vertex)) return null;
    return this.adjacencyList.get(vertex);
  }
}

var graph = new Graph();
var dom = {
  name: "a",
  children: [
    {
      name: "b",
      children: [
        {
          name: "d",
          children: [],
        },
        {
          name: "e",
          children: [],
        },
      ],
    },
    {
      name: "c",
      children: [
        {
          name: "f",
          children: [],
        },
        {
          name: "g",
          children: [],
        },
      ],
    },
  ],
};
var bfsDOM = (dom) => {
  const queue = [];
  const nodeList = [];
  if (dom) {
    queue.push(dom);
    while (queue.length) {
      const node = queue.shift();
      nodeList.push(node.name);
      node.children.forEach((child) => {
        queue.push(child);
      });
    }
  }
  return nodeList;
};
var result = bfsDOM(dom);
console.log(result.join("=>"));

// ================================================================================

// try to write terry yt question answer

var mockData = {
  1: [2, 3, 4],
  2: [1, 5],
  3: [1, 5],
  4: [1, 6],
  5: [2, 3, 7],
  6: [4, 7],
  7: [5, 6],
};

async function getGraph(startNode) {
  const graph = {};
  const queue = [startNode];
  while (queue.length) {
    const currentNode = queue.shift();
    // const res = await fetch(`https://api/${currentNode}`);
    const res = mockData[currentNode];
    if (!res) return;
    //   if (!res.ok) {
    //     console.error(`Error fetching node ${currentNode}`);
    //     continue;
    //   }
    // const neighbors = await res.json();
    const neighbors = res; // [2,3,4]
    // graph[currentNode] = neighbors.filter(
    //   (neighbor) => graph[neighbor] !== undefined || queue.includes(neighbor)
    // );
    graph[currentNode] = neighbors;
    graph[currentNode].forEach((neighbor) => {
      if (graph[neighbor] === undefined && !queue.includes(neighbor)) {
        queue.push(neighbor);
      }
    });
  }
  return graph;
}

async function createGraphClosure(startNode) {
  const graph = await getGraph(startNode);
  return {
    findNeighbors: (targetNode) => {
      if (graph[targetNode] === undefined) return null;
      return graph[targetNode];
      // function (targetNode) {
      //     if (graph[targetNode] === undefined) return null;
      //     return graph[targetNode];
      // }
    },
    show: () => {
      return graph;
    },
  };
}

var graph = await createGraphClosure(1);
console.log(graph.findNeighbors(5));
console.log(
  await Promise.resolve(createGraphClosure(1)).then((res) =>
    res.findNeighbors(2)
  )
);
