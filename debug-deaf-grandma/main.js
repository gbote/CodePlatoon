let talking = true;
let goodbyes = 0;

while (talking) {
    let statement = prompt();
    if ( statement === '' ) {
        alert('WHAT!?');
    } else if (statement.toUpperCase() !== statement) {
        alert('SPEAK UP, KID!');
    } else if ( statement === 'GOODBYE!' ) {
        goodbyes++;
        if (goodbyes === 1) {
            alert('LEAVING SO SOON?');
        } else if ( goodbyes === 2 ) {
            alert('LATER, SKATER!');
            talking = false;
        }
    } else if (statement.toUpperCase() === statement) {
        alert('NO, NOT SINCE 1946!');
    }
}