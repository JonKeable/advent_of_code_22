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


function findBestTree(grid) {
  const scoreGrid = new Array();
  //init array of same size as grid
  // we start of assuming all trees have a score of 0, and will calc for each
  for (const row of grid) {
    scoreGrid.push(new Array(grid[0].length).fill(0))
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      const row = grid[i];
      const tree = grid[i][j];
      let [vl, vr, vu, vd] = [0, 0, 0, 0];
      //console.log(i +',' +j +': ' +tree);

      for (let p = j+1; p < row.length; p++) {
        vr++;
        if (row[p] >= tree) {
          break;
        }
      }

      for (let p = j-1; p >= 0; p--) {
        vl++;
        if (row[p] >= tree) {
          break;
        }
      }

      for (let q = i+1; q < grid.length; q++) {
        vd++;
        if (grid[q][j] >= tree) {
          break;
        }
      }

      for (let q = i-1; q >= 0; q--) {
        vu++;
        if (grid[q][j] >= tree) {
          break;
        }
      }

      const score = vl * vr * vd * vu;
      scoreGrid[i][j] = score;

    }
  }


  //console.log(scoreGrid.toString());

  let bestScore = 0;
  for (const row of scoreGrid) {
    for (const t of row) {
      bestScore = t > bestScore ?  t : bestScore;
    }
  }

  console.log(bestScore);
}

readInputFile(inputPath, function (d) {
  dataToGrid(d, findBestTree);
});