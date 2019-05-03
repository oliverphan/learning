function allCurrents() {
  var currents = [];
  for (i = 0; i < GRID.length; i++) {
    var num = i + 1;
    for (k = 0; k < GRID[i].length; k++) {
      var coor = String.fromCharCode(k+65) + num.toString()
      if (isCurrent(coor)) {
        currents.push(coor);
      }
    }
  }
  return currents;
}