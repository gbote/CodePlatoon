export default function(genre) {
  return fetch(
    `https://api.themoviedb.org/3/genre/${genre}/movies?api_key=4b834ffb8f75337d8b82599980fffa3a&language=en-US&include_adult=false&sort_by=created_at.asc`
  )
    .then(res => res.json())
    .then(res => res.results.map(result => result.title));
}
