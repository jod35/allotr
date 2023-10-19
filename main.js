// Your array of items
const originalArray = [1, 2, 3, 4, 5];

// Create a single string with array members
const joinedString = originalArray.join(', ');

console.log(joinedString);


const convertArrayToString = (array) => {
    return array.join(', ')
}