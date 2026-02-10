"use strict";
// javascript run time environment

// this in global space
console.log(this); // this refers to globalObject - window,global

// this inside a function
function x() {
  console.log(this);
}
x();
