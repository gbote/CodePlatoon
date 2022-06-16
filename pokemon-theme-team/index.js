// get one pokemon
// get 5 more of the same type
    // get 1st type number
    // query api for type
    // as long as 5+ exist, grab 5 randomly
    // if not, try again with random
// probably store them all in an index
// loop through all 6, add info to the 6 cards

const randomNum = () =>{
  return Math.floor((Math.random()*898)+1)
}

const getPoke = async ()=>{
  // disable button
  let button = document.getElementById("button");
  button.disabled = true

  let pokemon = [];
  let pokeType = null;
  let url = '';

  //gets a pokemon with at least 5 others of same type
  do {
      let poke = await axios.get(`https://pokeapi.co/api/v2/pokemon/${randomNum()}/`);
      url = poke.data.types[0].type.url
      pokeType = await axios.get(url)
  } while (pokeType.data.pokemon.length<5)

  // get 6 pokemon of that type
  let index = [];
  let len = pokeType.data.pokemon.length;
  let next = null;
  for (let i=0; i<6; i++){
      // continues until a new pokemon is found
      while (true){
          next = Math.floor(Math.random()*len);
          if (index.includes(next)){ continue; }
          break;
      }
      index.push(next);
      url = pokeType.data.pokemon[next].pokemon.url;
      pokemon.push(await axios.get(url));
  }

  // read in each pokemon's data to the html cards
  for (let j=1; j<7; j++){
      let name = pokemon[j-1].data.name;
      name = name.charAt(0).toUpperCase() + name.slice(1);
      let picUrl = pokemon[j-1].data.sprites.front_default;
      document.getElementById(`card-title-${j}`).innerHTML = name;
      document.getElementById(`card-pic-${j}`).src = picUrl
      document.getElementById(`card-but-${j}`).href = `https://bulbapedia.bulbagarden.net/wiki/${name}_(Pok%C3%A9mon)`;
  }

  // read in the team type data to html page
  let type = pokeType.data.name
  type = type.charAt(0).toUpperCase() + type.slice(1);
  document.getElementById("team-type").innerHTML = `Your team's type is ${type}`;

  // activate button
  button.innerHTML="LETS GO!";
  button.disabled = false;
}
getPoke()

const updateButton = () => {
  let button = document.getElementById("button");
  if (button.innerHTML === "LETS GO!"){
      button.innerHTML = 'Reset'
  } else if (button.innerHTML === 'Reset'){
      getPoke()
  }
}