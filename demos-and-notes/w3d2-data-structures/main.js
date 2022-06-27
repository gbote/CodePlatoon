// const data = ['a', 'x', 'y', 'g', 'n', 'b', 'q']
// //             0    1 .  2 .  3 .  4 .  5 .  6
// // adding a new element to the end is just as easy, no matter how big the array is

// const locationOfG = data.indexOf('g') // we may have to check every single element to find g!


// const sortedData = ['a', 'c', 'l', 'm', 'r', 't', 'x']
// sortedData.addButKeepSorted('n') // this is harder depending on the length of the array
// a sorted list can be searched more efficiently than an unsorted list


class HashTable {
    constructor(){
        this.table = new Array(64).fill(0)
        this.table = this.table.map((el)=>{
            return []
        })
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
        // console.log('set!')
        const index = this._hash(key)
        this.table[index].push([key,value])
    }

    get(key){
        const index = this._hash(key)
        for ( let data of this.table[index] ) {
            if ( data[0] == key ) {
                return data[1]
            }
        }
    }
}

myHash = new HashTable()
// console.log(myHash.table)

myHash.set('name', 'alice')
// myHash.set('age', 24)
// myHash.set('mane', 'luxurious')
myHash.set('star', 'bright')
myHash.set('rats', 23)
myHash.set('tars', 'sticky')
myHash.set('arts', 'refined')
console.log(myHash.table)
console.log(myHash.get('name'))
console.log(myHash.get('age'))
console.log(myHash.get('mane'))
// console.log(myHash.get('name'))


// console.log(myHash.table)

