function formatBottleString(n) {  
  if (n === 1) {
    return "bottle"
  } 
  return "bottles"
}

function formatCount(n) {
  if (n === 0) {
    return "no more"
  } 
  return n
}

function bottleSong() {
  for (let i = 99; i >= 1; i--) {
    let currentCountBottles = formatBottleString(i)
    let currentCount = formatCount(i)
    console.log(`${currentCount} ${currentCountBottles} of beer on the wall, ${currentCount} ${currentCountBottles} of beer.\nTake one down and pass it around, ${formatCount(i-1)} ${formatBottleString(i-1)} of beer on the wall.`)
  }
  console.log("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
};

bottleSong();