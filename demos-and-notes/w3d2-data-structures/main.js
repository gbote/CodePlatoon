// const data = ['a', 'x', 'y', 'g', 'n', 'b', 'q']
// //             0    1 .  2 .  3 .  4 .  5 .  6
// // adding a new element to the end is just as easy, no matter how big the array is

// const locationOfG = data.indexOf('g') // we may have to check every single element to find g!


// const sortedData = ['a', 'c', 'l', 'm', 'r', 't', 'x']
// sortedData.addButKeepSorted('n') // this is harder depending on the length of the array
// a sorted list can be searched more efficiently than an unsorted list

class HashTable {
    constructor(){
        this.table = new Array(64) // an array with 64 empty elements
    }

    // given a key, this function should return a numerical index, which we can use to access the table above
    _hash(key){
        let hash = 0
        for ( let i = 0; i < key.length; i++ ) {
            hash += key.charCodeAt(i)
        }
        return hash % this.table.length
    }

    set(key, value){
        const index = this._hash(key)
        this.table[index] = value
    }

    get(key){
        const index = this._hash(key)
        return this.table[index]
    }
}

myHash = new HashTable()

myHash.set('age', 24)
myHash.set('name', 'alice')
console.log(myHash.get('age'))
console.log(myHash.get('name'))