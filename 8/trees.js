"use strict";

const fs = require('fs');
const inputPath = 'input.txt';

function readInputFile(fPath, callback) {
  fs.readFile(fPath, function (err, data) {
    if (err) {
      console.error(err);
      return;
    }
    return callback(data);
  });
}

console.log("df".length);

function dataToGrid(data, callback) {
  const lineArr = data.toString().split(/\r?\n/);
  lineArr.pop();
  //console.log(lineArr);
  const gridArr = new Array(0);
  //console.log(gridArr.toString());
  for (const line of lineArr) {
    const thisLine = new Array(0);
    for (const c of line) {
      thisLine.push(parseInt(c));
    }
    gridArr.push(thisLine);
  }
  console.log(gridArr.toString());
  callback(gridArr);
}


function findVisible(grid) {
  const boolGrid = new Array();
  //init array of same size as grid
  // we start of assuming all trees are visible, then switch to true as we test
  for (const row of grid) {
    boolGrid.push(new Array(grid[0].length).fill(false))
  }

  for (let i = 0; i < grid.length; i++){
    let rowMax = -1;
    for (let j = 0; j < grid[i].length; j++) {
      const tree = grid[i][j];
      if (tree > rowMax) {
        //console.log(tree);
        rowMax = tree;
        boolGrid[i][j] = true;
      }
    }
    rowMax = -1;
    for (let j = grid[i].length-1; j >= 0; j--) {
      const tree = grid[i][j];
      if (tree > rowMax) {
        //console.log(tree);
        rowMax = tree;
        boolGrid[i][j] = true;
      }
    }
  }

  console.log(grid[0].length)
  for (let j =0; j < grid[0].length; j++){
    let colMax = -1;
    for (let i = 0; i < grid.length; i++) {
      const tree = grid[i][j];
      if (tree > colMax) {
        colMax = tree;
        boolGrid[i][j] = true;
      }
    }
    colMax = -1;
    for (let i = grid.length-1; i >= 0; i--) {
      const tree = grid[i][j];
      //console.log(i + " , " + j)
      //console.log(tree);
      if (tree > colMax) {
        colMax = tree;
        boolGrid[i][j] = true;
      }
    }
  }

  console.log(boolGrid.toString());
  //console.log(boolGrid[].toString());

  let noVisible = 0;
  for (const line of boolGrid) {
    noVisible += line.filter(Boolean).length;
  }

  console.log(noVisible);
}

readInputFile(inputPath, function(d){
  dataToGrid(d, findVisible);
});